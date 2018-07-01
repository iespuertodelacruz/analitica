"""
Extract academic data from several input files and save them to new one.

Usage:
    extract.py --year=<year> --eval=<eval> [--type=<type>]

Options:
    --year=<year>   School year to work with (1516 or 1617 or 1718...)
    --eval=<eval>   Evaluation/trimester (1, 2, 3)
    --type=<type>   Type of data (academic, cohabitation, absence, all)
                    [default: all]
"""
from docopt import docopt
import xlrd
import config
import os
import openpyxl
import pyexcel_ods
import coloredlogs
import logging
import PyPDF2
import re
import sys
import utils


logger = logging.getLogger(__name__)
coloredlogs.install(
    fmt="%(asctime)s %(filename)s:%(lineno)d %(levelname)s %(message)s",
    level="DEBUG",
    logger=logger
)


class DataLoader:
    def __init__(self, year, evaluation):
        year = f"C{year}"
        evaluation = f"E{evaluation}"
        self.year = year
        self.evaluation = evaluation
        self.eval_index = int(evaluation[1]) - 1
        self.basename = f"{year}{evaluation}"
        self.path_target = os.path.join("data", f"{year}.xlsx")
        self.wb = openpyxl.load_workbook(self.path_target)
        self.sh = self.wb[evaluation]

    def load_academic(self):
        logger.info("Cargando información de rendimiento...")
        for group, value in config.GROUPS.items():
            # source
            source = value["source"][self.eval_index]
            if not source:
                continue
            filename = f"{self.basename}{source['file_suffix']}.xls"
            path = os.path.join("data_tmp", filename)
            try:
                wb = xlrd.open_workbook(path)
            except FileNotFoundError:
                logger.error(f"No se encuentra el fichero '{path}'")
                sys.exit()
            sh = wb.sheet_by_name(source["sheet"])
            success = sh.cell_value(*source["success"])
            # ratio
            ratio_row = source["success"][0]
            ratio_col = source["success"][1] - 2
            ratio = 0
            for i in range(ratio_row, ratio_row + 5):
                ratio += float(sh.cell_value(i, ratio_col))
            # target
            c = utils.get_target_cell(group, "success")
            self.sh[c] = f"{success:.2f}"
            c = utils.get_target_cell(group, "ratio")
            self.sh[c] = ratio
        self.wb.save(self.path_target)

    def load_cohabitation(self):
        logger.info("Cargando información de convivencia...")
        filename = f"{self.basename}_CONVIVENCIA.ods"
        path = os.path.join("data_tmp", filename)
        try:
            data = pyexcel_ods.get_data(path)
        except FileNotFoundError:
            logger.error(f"No se encuentra el fichero '{path}'")
            sys.exit()
        data = list(data.values())[0]
        for row in data:
            group = row[0]
            if group not in config.GROUPS.keys():
                logger.warning(f"Grupo '{group}' no encontrado...")
            else:
                if len(row) > 1:
                    reports = int(row[1])
                    if reports > 0:
                        c = utils.get_target_cell(group, "reports")
                        self.sh[c] = reports
                if len(row) > 2:
                    non_attendance = int(row[2])
                    if non_attendance > 0:
                        c = utils.get_target_cell(group, "non_attendance")
                        self.sh[c] = non_attendance
        self.wb.save(self.path_target)

    def load_absence(self):
        logger.info("Cargando información de absentismo...")
        filename = f"{self.basename}_ABSENTISMO.pdf"
        path = os.path.join("data_tmp", filename)
        try:
            source = PyPDF2.PdfFileReader(open(path, "rb"))
        except FileNotFoundError:
            logger.error(f"No se encuentra el fichero '{path}'")
            sys.exit()
        for page in source.pages:
            text = page.extractText()
            r = re.search(r"Grupo:([\dA-Z]+)", text)
            if r:
                group = r.groups()[0]
                r = re.search(r"\(SI\)(\d+,\d\d)(\d+,\d\d).*MOTIVOS", text)
                if r:
                    justified_absence = \
                        float(r.groups()[0].replace(",", "."))
                    unjustified_absence = \
                        float(r.groups()[1].replace(",", "."))
                    if group not in config.GROUPS.keys():
                        logger.warning(f"Grupo '{group}' no encontrado...")
                    else:
                        c = utils.get_target_cell(group, "justified_absence")
                        self.sh[c] = f"{justified_absence:.2f}"
                        c = utils.get_target_cell(group, "unjustified_absence")
                        self.sh[c] = f"{unjustified_absence:.2f}"
        self.wb.save(self.path_target)


if __name__ == "__main__":
    arguments = docopt(__doc__)
    data_loader = DataLoader(arguments["--year"], arguments["--eval"])
    if arguments["--type"] == "all":
        data_loader.load_academic()
        data_loader.load_cohabitation()
        data_loader.load_absence()
    elif arguments["--type"] == "academic":
        data_loader.load_academic()
    elif arguments["--type"] == "cohabitation":
        data_loader.load_cohabitation()
    elif arguments["--type"] == "absence":
        data_loader.load_absence()

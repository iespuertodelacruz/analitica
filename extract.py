"""
Extract academic data from several input files and save them to new one.

Usage:
    extract.py --year=<year> --eval=<eval>

Options:
    --year=<year>   School year to work with (1516 or 1617 or 1718...)
    --eval=<eval>   Evaluation/trimester (1, 2, 3)
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
            target = value["target"]
            self.sh[target["success"]] = f"{success:.2f}"
            self.sh[target["ratio"]] = ratio
        self.wb.save(self.path_target)

    def load_cohabitation(self):
        logger.info("Cargando información de convivencia...")
        filename = f"{self.year}_CONVIVENCIA.ods"
        path = os.path.join("data_tmp", filename)
        try:
            data = pyexcel_ods.get_data(path)
        except FileNotFoundError:
            logger.error(f"No se encuentra el fichero '{path}'")
            sys.exit()
        for row in data[self.evaluation]:
            group = row[0]
            try:
                target = config.GROUPS[group]["target"]
            except KeyError:
                logger.warning(f"Grupo '{group}' no encontrado...")
            else:
                if len(row) > 1:
                    reports = int(row[1])
                    if reports > 0:
                        self.sh[target["reports"]] = reports
                if len(row) > 2:
                    non_attendance = int(row[2])
                    if non_attendance > 0:
                        self.sh[target["non_attendance"]] = non_attendance
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
                    non_justified_absence = \
                        float(r.groups()[1].replace(",", "."))
                    total_absence = justified_absence + non_justified_absence
                    try:
                        target = config.GROUPS[group]["target"]
                    except KeyError:
                        logger.warning(f"Grupo '{group}' no encontrado...")
                    else:
                        self.sh[target["absence"]] = f"{total_absence:.2f}"
        self.wb.save(self.path_target)


if __name__ == "__main__":
    arguments = docopt(__doc__)
    data_loader = DataLoader(arguments["--year"], arguments["--eval"])
    data_loader.load_academic()
    data_loader.load_cohabitation()
    data_loader.load_absence()

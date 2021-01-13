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
import os
import openpyxl
import pyexcel_ods
import coloredlogs
import logging
import PyPDF2
import re
import sys
from pathlib import Path


logger = logging.getLogger(__name__)
coloredlogs.install(
    fmt="%(asctime)s %(filename)s:%(lineno)d %(levelname)s %(message)s",
    level="DEBUG",
    logger=logger,
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
        self._load_groups()
        self._load_columns()

    def _load_groups(self):
        self.groups = {}
        for i, row in enumerate(self.sh):
            if row[0].value == 'grupo':
                continue
            self.groups[row[0].value] = i + 1

    def _load_columns(self):
        self.columns = {
            'grupo': 1,
            'etapa': 2,
            'éxito': 3,
            'absentismo_justificado': 4,
            'absentismo_injustificado': 5,
            'partes': 6,
            'suspensión_asistencia': 7,
            'ratio': 8,
        }

    def _get_target_cell(self, group, column):
        return self.groups[group], self.columns[column]

    def _set_target_value(self, group, column, value):
        cell = self._get_target_cell(group, column)
        self.sh.cell(*cell, value)

    def _grab_group_academics(self, academics):
        fields = [f.strip('"') for f in academics.split(';')]
        group = fields[3]
        if group not in self.groups.keys():
            logger.warning(
                (f"Grupo '{group}' no encontrado en " "el fichero de configuración")
            )
            return
        success_abs = int(fields[9])
        success_pct = float(fields[10].replace(',', '.'))
        try:
            ratio = round(success_abs * 100 / success_pct)
        except ZeroDivisionError:
            logger.error(f"Grupo '{group}' no tiene alumnado!")
            ratio = 0

        self._set_target_value(group, 'éxito', success_pct)
        self._set_target_value(group, 'ratio', ratio)

    def load_academic(self):
        logger.info("Cargando información de rendimiento...")
        for file in Path('./data_tmp').glob('*.csv'):
            with open(file, encoding='ISO-8859-1') as f:
                for line in f.readlines():
                    if re.search('TODO APROBADO', line):
                        self._grab_group_academics(line)
        self.wb.save(self.path_target)

    def _grab_group_cohabitation(self, cohabitation):
        group = cohabitation[0]
        if group not in self.groups.keys():
            logger.warning(
                (f"Grupo '{group}' no encontrado en " "el fichero de configuración")
            )
            return
        if len(cohabitation) > 1:
            reports = int(cohabitation[1])
            if reports > 0:
                self._set_target_value(group, 'partes', reports)
        if len(cohabitation) > 2:
            non_attendance = int(cohabitation[2])
            if non_attendance > 0:
                self._set_target_value(group, 'suspensión_asistencia', non_attendance)

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
            if row:
                self._grab_group_cohabitation(row)
        self.wb.save(self.path_target)

    def _grab_group_absence(self, absence, page):
        group = absence.groups()[0]
        if group not in self.groups.keys():
            logger.warning(
                (f"Grupo '{group}' no encontrado en " "el fichero de configuración")
            )
            return
        r = re.search(r"\(SI\)(\d+,\d\d)(\d+,\d\d).*MOTIVOS", page)
        if r:
            justified_absence = float(r.groups()[0].replace(",", "."))
            unjustified_absence = float(r.groups()[1].replace(",", "."))
            self._set_target_value(group, 'absentismo_justificado', justified_absence)
            self._set_target_value(group, 'absentismo_injustificado', unjustified_absence)

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
            r = re.search(r"Grupo:(\S+)", text)
            if r:
                self._grab_group_absence(r, text)
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

from prettyconf import config

FIGURE_DPI = config('FIGURE_DPI', default=72, cast=int)

COMPETENCE_CRITERIA = {'PA-%': 'PA', 'AD-%': 'AD', 'MA-%': 'MA', 'EX-%': 'EX'}

STUDIES = {
    '1º Educación Secundaria Obligatoria (LOMCE)': '1ESO',
    '2º Educación Secundaria Obligatoria (LOMCE)': '2ESO',
    '3º Educación Secundaria Obligatoria (LOMCE)': '3ESO',
    '4º Educación Secundaria Obligatoria (LOMCE)': '4ESO',
    (
        'Primer curso del Programa de Mejora del Aprendizaje y el ' 'Rendimiento (LOMCE)'
    ): '1PMAR',
    (
        'Segundo curso del Programa de Mejora del Aprendizaje y el ' 'Rendimiento (LOMCE)'
    ): '2PMAR',
}

COMPETENCE_ITEMS = {
    'Comunicación lingüística': 'CL',
    ('Competencia matemática y competencias básicas en ' 'ciencia y tecnología'): 'CMCT',
    'Competencia digital': 'CD',
    'Aprender a aprender': 'AAP',
    'Competencias sociales y cívicas': 'CSC',
    'Sentido de iniciativa y espíritu emprendedor': 'SIEE',
    'Conciencia y expresiones culturales': 'CEC',
}

COMPETENCE_WEIGHTS = {'PA': 0.025, 'AD': 0.050, 'MA': 0.075, 'EX': 0.1}

COLUMNS = {
    'GRUPO': 'grupo',
    'ESTUDIO': 'nivel',
    'ITEM': 'item',
}

MAX_RATIO = {
    'ESO1': 27,
    'ESO2': 27,
    'ESO': 30,
    'FPB': 12,
    'BACH': 30,
    'CFGM': 20,
    'CFGS': 30,
    '1ARI': 20,
    '2ARI': 20,
    'PMAR': 12,
    'DIVER': 15,
}

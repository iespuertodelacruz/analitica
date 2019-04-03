# Basic competences
import pandas as pd

COMPETENCE_CRITERIA = {
    'PA-%': 'PA',
    'AD-%': 'AD',
    'MA-%': 'MA',
    'EX-%': 'EX'
}

STUDIES = {
    '1º Educación Secundaria Obligatoria (LOMCE)': '1ESO',
    '2º Educación Secundaria Obligatoria (LOMCE)': '2ESO',
    '3º Educación Secundaria Obligatoria (LOMCE)': '3ESO',
    '4º Educación Secundaria Obligatoria (LOMCE)': '4ESO',
    ('Primer curso del Programa de Mejora del Aprendizaje y el '
        'Rendimiento (LOMCE)'): '1PMAR',
    ('Segundo curso del Programa de Mejora del Aprendizaje y el '
        'Rendimiento (LOMCE)'): '2PMAR'
}

COMPETENCE_ITEMS = {
    'Comunicación lingüística': 'CL',
    ('Competencia matemática y competencias básicas en '
        'ciencia y tecnología'): 'CMCT',
    'Competencia digital': 'CD',
    'Aprender a aprender': 'AAP',
    'Competencias sociales y cívicas': 'CSC',
    'Sentido de iniciativa y espíritu emprendedor': 'SIEE',
    'Conciencia y expresiones culturales': 'CEC'
}

COMPETENCE_WEIGHTS = {
    'PA': 0.025,
    'AD': 0.050,
    'MA': 0.075,
    'EX': 0.1
}

COLUMNS = {
    'GRUPO': 'grupo',
    'ESTUDIO': 'nivel',
    'ITEM': 'item',
}


def load_bc(path):
    df = pd.read_csv(
        path,
        encoding='cp1252',
        sep=';',
        skipfooter=9,
        engine='python')

    df = df[df['GRUPO'] != 'TOTAL ESTUDIO']

    df = df.rename(columns=COMPETENCE_CRITERIA)
    df = df.rename(columns=COLUMNS)

    df = df[['nivel', 'grupo', 'item', *COMPETENCE_CRITERIA.values()]]
    df['nivel'].replace(STUDIES, inplace=True)
    df['item'].replace(COMPETENCE_ITEMS, inplace=True)

    # summary value for each group-item
    df['marca'] = COMPETENCE_WEIGHTS['PA'] * df['PA'] + \
        COMPETENCE_WEIGHTS['AD'] * df['AD'] + \
        COMPETENCE_WEIGHTS['MA'] * df['MA'] + \
        COMPETENCE_WEIGHTS['EX'] * df['EX']

    return df

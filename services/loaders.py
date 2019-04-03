import pandas as pd
import os

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


def load_data(year, evaluation):
    df = pd.DataFrame()
    df_bc = pd.DataFrame()
    labels = []
    for y in range(year - 2, year + 1):
        year_label = 'C' + str(y)[2:] + str(y + 1)[2:]
        path = os.path.join('../data', year_label + '.xlsx')
        if y == year:
            num_evaluations = evaluation
        else:
            num_evaluations = 3
        for ev in range(1, num_evaluations + 1):
            evaluation_label = f'E{ev}'
            partial_df = pd.read_excel(path, sheet_name=evaluation_label)
            partial_df['curso'] = year_label
            partial_df['evaluación'] = evaluation_label
            partial_df['absentismo'] = partial_df[
                'absentismo_justificado'] + partial_df[
                    'absentismo_injustificado']
            partial_df['éxito_abs'] = round(
                partial_df['ratio'] * (partial_df['éxito'] / 100))
            partial_df.set_index(['curso', 'evaluación', 'grupo'],
                                 inplace=True)

            # Loading basic competences
            filename_bc = year_label + evaluation_label + '_ESO_CCBB.csv'
            path_bc = os.path.join('../data/ccbb', filename_bc)
            partial_df_bc = load_bc(path_bc)
            partial_df_bc['curso'] = year_label
            partial_df_bc['evaluación'] = evaluation_label
            partial_df_bc.set_index(['curso', 'evaluación', 'grupo'],
                                    inplace=True)

            # grouping basic competences by groups (summary value)
            partial_df_bc_grouped = partial_df_bc.groupby(
                'grupo').mean()['marca']
            partial_df = pd.merge(
                partial_df,
                pd.DataFrame(partial_df_bc_grouped),
                left_index=True,
                right_index=True,
                how='outer',
                sort=False).rename(columns={'marca': 'ccbb'})
            partial_df_bc.index.name = 'grupo'

            df = df.append(partial_df)
            df_bc = df_bc.append(partial_df_bc)

            labels.append((year_label, evaluation_label))

    df.fillna(0, inplace=True)
    df_bc.fillna(0, inplace=True)

    return df, df_bc, labels


def get_data_by_stages(df, stages):
    if not isinstance(stages, list):
        stages = [stages]
    return df[df['etapa'].isin(stages)]

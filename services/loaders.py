import os

import pandas as pd

from . import settings, utils


def get_year_label(year: str):
    return 'C' + str(year)[2:] + str(year + 1)[2:]


def load_bc(path):
    df = pd.read_csv(path, encoding='cp1252', sep=';', skipfooter=9, engine='python')

    df = df[df['GRUPO'] != 'TOTAL ESTUDIO']

    df = df.rename(columns=settings.COMPETENCE_CRITERIA)
    df = df.rename(columns=settings.COLUMNS)

    df = df[['nivel', 'grupo', 'item', *settings.COMPETENCE_CRITERIA.values()]]
    df['nivel'].replace(settings.STUDIES, inplace=True)
    df['item'].replace(settings.COMPETENCE_ITEMS, inplace=True)

    # summary value for each group-item
    df['marca'] = (
        settings.COMPETENCE_WEIGHTS['PA'] * df['PA']
        + settings.COMPETENCE_WEIGHTS['AD'] * df['AD']
        + settings.COMPETENCE_WEIGHTS['MA'] * df['MA']
        + settings.COMPETENCE_WEIGHTS['EX'] * df['EX']
    )

    return df


def load_data(year, evaluation):
    df = pd.DataFrame()
    df_bc = pd.DataFrame()
    labels = []
    for y in range(year - 2, year + 1):
        year_label = get_year_label(y)
        path = os.path.join('../../data_staged', year_label + '.xlsx')
        if y == year:
            num_evaluations = evaluation
        else:
            num_evaluations = 3
        for ev in range(1, num_evaluations + 1):
            evaluation_label = f'E{ev}'
            partial_df = pd.read_excel(path, sheet_name=evaluation_label)
            partial_df['curso'] = year_label
            partial_df['evaluación'] = evaluation_label
            partial_df['absentismo'] = (
                partial_df['absentismo_justificado']
                + partial_df['absentismo_injustificado']
            )
            partial_df['éxito_abs'] = round(
                partial_df['ratio'] * (partial_df['éxito'] / 100)
            )
            partial_df.set_index(['curso', 'evaluación', 'grupo'], inplace=True)
            # null values
            partial_df['partes'].fillna(0, inplace=True)
            partial_df['suspensión_asistencia'].fillna(0, inplace=True)

            # Loading basic competences
            filename_bc = year_label + evaluation_label + '_ESO_CCBB.csv'
            path_bc = os.path.join('../../data_staged/ccbb', filename_bc)
            partial_df_bc = load_bc(path_bc)
            partial_df_bc['curso'] = year_label
            partial_df_bc['evaluación'] = evaluation_label
            partial_df_bc.set_index(['curso', 'evaluación', 'grupo'], inplace=True)

            # grouping basic competences by groups (summary value)
            partial_df_bc_grouped = partial_df_bc.groupby('grupo').mean()['marca']
            partial_df = pd.merge(
                partial_df,
                pd.DataFrame(partial_df_bc_grouped),
                left_index=True,
                right_index=True,
                how='outer',
                sort=False,
            ).rename(columns={'marca': 'ccbb'})
            partial_df_bc.index.name = 'grupo'

            df = df.append(partial_df)
            df_bc = df_bc.append(partial_df_bc)

            labels.append((year_label, evaluation_label))

    # Establecemos las ratios máximas
    # Ojo porque para cursos anteriores no tienen por qué ser las mismas!!
    df = df.reset_index().apply(utils.fill_max_ratio, axis=1)
    # PMAR (último grupo de 2ESO)
    pmar_group = (
        df['grupo'][df['grupo'].str.startswith('ESO2')].sort_values(ascending=False).iloc[0]
    )
    df.loc[df['grupo'] == pmar_group, 'max_ratio'] = settings.MAX_RATIO['PMAR']
    # DIVER (último grupo de 3ESO)
    diver_group = (
        df['grupo'][df['grupo'].str.startswith('ESO3')].sort_values(ascending=False).iloc[0]
    )
    df.loc[df['grupo'] == diver_group, 'max_ratio'] = settings.MAX_RATIO['DIVER']
    df = df.set_index(['curso', 'evaluación', 'grupo'])

    return df, df_bc, labels


def get_data_by_stages(df, stages):
    if not isinstance(stages, list):
        stages = [stages]
    return df[df['etapa'].isin(stages)]

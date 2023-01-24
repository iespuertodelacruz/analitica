import itertools

import numpy as np
from scipy.interpolate import interp1d

from . import settings


def make_colorscale(colors, thresholds=None, discrete=False):
    if discrete:
        if thresholds is None:
            ls = np.linspace(0, 1, len(colors) + 1)
        else:
            ls = thresholds
        window = ls[1:-1]
        thresholds = [ls[0]]
        thresholds += list(itertools.chain(*zip(window, window)))
        thresholds.append(ls[-1])
        colors = list(itertools.chain(*zip(colors, colors)))
    else:
        thresholds = np.linspace(0, 1, len(colors))

    colorscale = list(zip(thresholds, colors))
    return colorscale


def normalize_thresholds(df, thresholds):
    df_min = df.values.min()
    df_max = df.values.max()
    m = interp1d([df_min, df_max], [0, 1])
    thresholds.insert(0, df_min)
    thresholds.append(df_max)
    return m(thresholds)


@np.vectorize
def format_value(value, is_percentage=True):
    r = f'{value:.2f}'
    if is_percentage:
        r += '%'
    return r


def fill_max_ratio(row):
    grupo = row['grupo']
    etapa = row['etapa']
    row['max_ratio'] = settings.MAX_RATIO.get(grupo) or settings.MAX_RATIO[etapa]
    return row

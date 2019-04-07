import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import pandas as pd
from prettyconf import config

FIGURE_DPI = config('FIGURE_DPI', default=72, cast=int)

sns.set(style='whitegrid')


def set_custom_style(context='notebook'):
    sns.set()
    sns.set(style='whitegrid')
    sns.set_context(context)


def makeup_chart(fontsize, value_margin, is_percentage, show_integer):
    if is_percentage:
        percentage_symbol = '%'
    else:
        percentage_symbol = ''
    plt.xlabel('')
    plt.ylabel('')
    plt.xticks(fontsize=fontsize)
    plt.yticks(fontsize=fontsize * 0.75)
    ax = plt.gca()
    if show_integer:
        annotation = '{:.0f}{}'
    else:
        annotation = '{:.2f}{}'
    # show values in bars
    for p in ax.patches:
        ax.annotate(
            annotation.format(p.get_height(), percentage_symbol),
            (p.get_x() + p.get_width() / 2., p.get_height() - value_margin),
            ha='center', va='center', fontsize=fontsize, color='white'
        )
    # hide right and top spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)


def bar_chart(serie, is_percentage=True, show_integer=True):
    FONTSIZE = 25
    serie = serie.sort_values()
    plt.figure(figsize=(30, 10), dpi=FIGURE_DPI)
    sns.barplot(serie.index, serie)
    makeup_chart(FONTSIZE, serie.max() / 20, is_percentage, show_integer)


def factor_chart(data,
                 y,
                 value_margin=2,
                 is_percentage=True,
                 estimator=np.mean,
                 show_integer=True):
    FONTSIZE = 14
    plt.figure(figsize=(30, 10), dpi=FIGURE_DPI)
    colors = ['orange red', 'windows blue', 'amber']
    custom_palette = sns.xkcd_palette(colors)
    sns.catplot(
        x='etapa',
        y=y,
        hue='curso',
        height=7,
        aspect=2,
        legend=False,
        estimator=estimator,
        data=data.reset_index(),
        kind='bar',
        palette=custom_palette,
        ci=None)
    plt.legend(
        loc='best', prop={'size': FONTSIZE}, frameon=True, framealpha=0.9)
    makeup_chart(FONTSIZE, value_margin, is_percentage, show_integer)


def color_gradient(serie, palette_name, inverse=False):
    unique_values = np.sort(serie.unique())
    if inverse:
        unique_values = unique_values[::-1]
    pal = sns.color_palette(palette_name, unique_values.size)
    cmap = {v: c for v, c in zip(unique_values, pal)}
    return np.array(serie.map(lambda x: cmap[x]))


def delta_chart(*args, label, inverse=False):
    CONFIG = ({
        'color': 'Greens',
        'verb': 'mejorado'
    }, {
        'color': 'Reds_r',
        'verb': 'empeorado'
    })

    fig, axes = plt.subplots(1, 2, figsize=(15, 5), dpi=FIGURE_DPI)
    for ix, ax in enumerate(axes):
        serie = args[ix]['delta']
        if len(serie) == 0:
            continue
        sns.barplot(
            serie.index,
            serie,
            ax=axes[ix],
            palette=color_gradient(serie, CONFIG[ix]['color'], inverse))
        ax.set_axisbelow(True)
        ax.yaxis.grid(color='gray', linestyle='-', alpha=0.5)
        verb = CONFIG[ix]['verb']
        title = f'Grupos que han {verb} en {label}'
        ax.set_title(title)


def stacked_chart(data, y, x1, x2, x1_label=None, x2_label=None):
    f, ax = plt.subplots(figsize=(6, 15), dpi=FIGURE_DPI)

    sns.set_color_codes('pastel')
    if not x1_label:
        x1_label = x1
    sns.barplot(x=x1, y=y, data=data, label=x1_label, color='b')

    sns.set_color_codes('muted')
    if not x2_label:
        x2_label = x2
    sns.barplot(x=x2, y=y, data=data, label=x2_label, color='b')

    ax.legend(ncol=1, loc='upper right', frameon=True)
    ax.set(ylabel='', xlabel='')

    sns.despine()


def rgb_heatmap(data, center=5):
    cdict = {
        'red': ((0.0, 1.0, 0.7), (0.5, 1.0, 0.7), (1.0, 0.0, 0.0)),
        'green': ((0.0, 0.0, 0.0), (0.5, 1.0, 0.4), (1.0, 1.0, 0.4)),
        'blue': ((0.0, 0.0, 0.0), (1.0, 0.0, 0.0))
    }

    plt.figure(figsize=(5, 5), dpi=FIGURE_DPI)
    cmap = LinearSegmentedColormap('custom_cmap', cdict, 4)
    sns.heatmap(data, annot=True, cmap=cmap, center=center)
    # hide axis labels
    plt.xlabel('')
    plt.ylabel('')
    # hide ticks
    plt.tick_params(top=False, bottom=False, left=False,
                    right=False, labelleft=True, labelbottom=True)


def bc_evolution_chart(data):
    plt.figure(figsize=(5, 5), dpi=FIGURE_DPI)
    sns.lineplot(
        x='curso',
        y='marca',
        hue='item',
        markers=True,
        style='item',
        dashes=False,
        data=data)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    sns.despine(left=True)


def magic_groups(data):
    fig, (ax1, ax2) = plt.subplots(
        1, 2, figsize=(15, 5), sharey=True, dpi=FIGURE_DPI)

    best_magic = pd.melt(
        data.head(5).reset_index(),
        id_vars='grupo',
        value_vars=['éxito', 'absentismo', 'partes'])
    g = sns.catplot(x='grupo', y='value', hue='variable',
                    data=best_magic, kind='bar', ax=ax1)
    ax1.set_title('Mejores grupos mágicos')
    ax1.set(ylabel='', xlabel='')
    ax1.legend(loc='best', frameon=True, framealpha=0.9)
    plt.close(g.fig)

    worse_magic = pd.melt(
        data.tail(5).reset_index(),
        id_vars='grupo',
        value_vars=['éxito', 'absentismo', 'partes'])
    g = sns.catplot(x='grupo', y='value', hue='variable',
                    data=worse_magic, kind='bar', ax=ax2, legend_out=True)
    ax2.set_title('Peores grupos mágicos')
    ax2.set(ylabel='', xlabel='')
    ax2.legend(loc='best', frameon=True, framealpha=0.9)
    plt.close(g.fig)

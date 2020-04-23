import itertools

import colorlover as cl
import numpy as np
import pandas as pd
import plotly
import plotly.graph_objs as go
import plotly.io as pio
from plotly.offline import init_notebook_mode, iplot
from scipy import stats

from . import utils

init_notebook_mode(connected=True)
pio.templates.default = 'plotly_white'


def hbar(x_values,
         y_values,
         trace_names=None,
         colors=None,
         title='',
         fig_size=(700, 1000)):
    ''' Horizontal stacked barchart '''
    if trace_names is None:
        trace_names = [x.name for x in x_values]
    if colors is None:
        colors = cl.scales['9']['qual']['Paired'][:len(x_values)]

    data = []
    for x, trace_name, color in zip(x_values, trace_names, colors):
        trace = go.Bar({
            'x': x,
            'y': y_values,
            'name': trace_name,
            'orientation': 'h',
            'marker': {
                'color': color
            }
        })
        data.append(trace)

    layout = go.Layout(
        barmode='overlay',
        width=fig_size[0],
        height=fig_size[1],
        yaxis={
            'type': 'category',
            'autorange': 'reversed'
        },
        title=title)

    fig = go.Figure(data=data, layout=layout)
    iplot(fig)


def bar_simple(x_values,
               y_values,
               title='',
               colormap='Greens',
               is_percentage=True,
               yaxis_range=None,
               mark_colors=False):
    ''' Barchart with single bars '''

    if mark_colors:
        colors = y_values.apply(lambda x: 'green' if x >= 5 else 'red')
        colorscale = None
    else:
        colors = y_values
        cs = cl.scales['5']['seq'][colormap][1:]
        ls = np.linspace(0, 1, len(cs))
        colorscale = list(zip(ls, cs))

    trace_config = {
        'x': x_values,
        'y': y_values,
        'marker': {
            'color': colors,
            'colorscale': colorscale
        }
    }
    if is_percentage:
        trace_config['text'] = utils.format_value(y_values)
        trace_config['hoverinfo'] = 'x + text'
    trace = go.Bar(trace_config)

    layout = go.Layout(
        title=title,
        yaxis={'range': yaxis_range}
    )

    data = [trace]

    fig = go.Figure(data=data, layout=layout)
    iplot(fig)


def cbar(x_labels, series, is_percentage=True, barmode='group'):
    ''' Barchart with multiple bars '''
    data = []
    for name, values in series.items():
        trace_config = {
            'x': x_labels,
            'y': values,
            'name': name,
        }
        if is_percentage:
            trace_config['text'] = utils.format_value(values)
            trace_config['hoverinfo'] = 'x + text + name'
        trace = go.Bar(trace_config)
        data.append(trace)

    layout = go.Layout(barmode=barmode)
    fig = go.Figure(data=data, layout=layout)
    iplot(fig)


def scatter(xi, y, dot_labels, x_title=None, y_title=None):
    ''' Scatter plot with regression line '''
    # get lineal regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(xi, y)
    line = slope*xi + intercept

    if x_title is None:
        x_title = xi.name
    if y_title is None:
        y_title = y.name

    trace1 = go.Scatter(
        x=xi,
        y=y,
        mode='markers',
        text=dot_labels,
        marker={
            'size': 12,
        },
        showlegend=False,
        name='')

    trace2 = go.Scatter(
        x=xi, y=line, mode='lines', name=f'Regresión', hoverinfo='skip')

    data = [trace1, trace2]

    layout = go.Layout(
        hovermode='closest',
        width=600,
        height=600,
        xaxis={
            'title': x_title,
        },
        yaxis={
            'title': y_title,
        },
    )

    fig = go.Figure(data=data, layout=layout)
    iplot(fig)


def dbar(x_values,
         y_values,
         title='',
         is_percentage=True,
         inverted_colors=False):
    ''' Barchart for displaying deltas (differences) '''

    invf = -1 if inverted_colors else 1
    trace_config = {
        'x': x_values,
        'y': y_values,
        'marker': {
            'color':
            y_values.apply(lambda x: 'green' if x * invf >= 0 else 'red'),
        }
    }
    if is_percentage:
        trace_config['text'] = utils.format_value(y_values)
        trace_config['hoverinfo'] = 'x + text'
    trace = go.Bar(trace_config)

    layout = go.Layout(
        title=title
    )

    data = [trace]

    fig = go.Figure(data=data, layout=layout)
    iplot(fig)


def bc_bar(df):
    ''' Barplot for comparing acquisition of basic competences '''
    levels = pd.unique(df['nivel'])

    trace_colors = dict(
        zip(['PA', 'AD', 'MA', 'EX'], cl.scales['4']['div']['Spectral']))
    plot_num_cols = 3
    plot_num_rows = levels.size // plot_num_cols
    subplot_ids = list(
        itertools.product(
            range(1, plot_num_rows + 1), range(1, plot_num_cols + 1)))

    fig = plotly.subplots.make_subplots(
        rows=plot_num_rows,
        cols=plot_num_cols,
        subplot_titles=levels,
        shared_yaxes=True,
        print_grid=False)

    for i, level in enumerate(levels):
        aux = df.groupby(['nivel', 'item']).mean().loc[level].drop(
            'marca', axis=1).to_dict()

        for bc_acq_label, bc_acq_data in aux.items():
            x_values = list(bc_acq_data.keys())
            y_values = list(bc_acq_data.values())
            trace_config = {
                'x': x_values,
                'y': y_values,
                'name': bc_acq_label,
                'legendgroup': bc_acq_label,
                'marker': {
                    'color': trace_colors[bc_acq_label]
                },
                'text': utils.format_value(y_values),
                'hoverinfo': 'x + text + name'
            }
            if i > 0:
                trace_config['showlegend'] = False
            trace = go.Bar(trace_config)
            fig.append_trace(trace, *subplot_ids[i])

    layout = go.Layout(
        barmode='group',
        height=800
    )

    fig.layout.update(layout)
    iplot(fig)


def heatmap(x_values, y_values, z_values, colorscale, width=600, height=600):
    ''' Heatmap '''
    trace = go.Heatmap(
        x=x_values,
        y=y_values,
        z=z_values,
        colorscale=colorscale,
        colorbar={'ticks': 'outside'})
    data = [trace]
    layout = go.Layout(width=width, height=height)
    fig = go.Figure(data=data, layout=layout)
    iplot(fig)


def bc_evolution(df):
    ''' Lineplot for showing evolution of basic competences acquisition '''
    items = np.sort(pd.unique(df['item']))

    data = []
    for item in items:
        aux = df.groupby(['curso',
                          'item']).mean().swaplevel().loc[item]['marca']
        trace = go.Scatter(
            x=aux.index,
            y=aux.values,
            name=item,
            text=utils.format_value(aux.values, is_percentage=False),
            hoverinfo='x+name+text',
            line={'width': 3},
            marker={'size': 8})
        data.append(trace)

    layout = {
        'xaxis': {'title': 'Curso escolar'},
        'yaxis': {'title': 'Valoración CCBB'},
        'width': 600,
        'height': 600
    }

    fig = dict(data=data, layout=layout)
    iplot(fig)


def bc_extremes(df):
    ''' Plot miminum and maximum marks of basic competences for each group '''

    # build data series
    worst_marked = {'items': [], 'marks': []}
    best_marked = {'items': [], 'marks': []}
    groups = df.index.unique()
    for group in groups:
        aux = df.loc[group].reset_index()
        row_min = aux.loc[aux['marca'].idxmin()]
        worst_marked['items'].append(row_min['item'])
        worst_marked['marks'].append(row_min['marca'])
        row_max = aux.loc[aux['marca'].idxmax()]
        best_marked['items'].append(row_max['item'])
        best_marked['marks'].append(row_max['marca'])

    # build traces
    trace1 = go.Scatter(
        x=groups,
        y=best_marked['items'],
        mode='markers',
        text=np.around(best_marked['marks'], decimals=2),
        marker=dict(size=np.array(best_marked['marks']) * 3),
        marker_color='green',
        name='Mejor valoración'
    )
    trace2 = go.Scatter(
        x=groups,
        y=worst_marked['items'],
        mode='markers',
        text=np.around(worst_marked['marks'], decimals=2),
        marker=dict(size=np.array(worst_marked['marks']) * 3),
        marker_color='red',
        name='Peor valoración'
    )

    # plot data
    data = [trace1, trace2]

    layout = go.Layout(
        hovermode='closest',
        width=600,
        height=600,
    )

    fig = go.Figure(data=data, layout=layout)
    iplot(fig)


def num_students_evolution(df, stages, years, ratio=False):
    ''' Lineplot for showing evolution of number of students '''

    if ratio:
        agg_func, ytitle = 'mean', 'Ratio'
    else:
        agg_func, ytitle = 'sum', 'Núm. alumnado'

    data = []
    for stage in stages:
        values = df.query(f'etapa == "{stage}"').groupby(
            'curso').agg({'ratio': agg_func})['ratio'].values
        data.append(go.Scatter(
            x=years,
            y=values,
            name=stage,
            text=np.around(values, decimals=2),
            hoverinfo='name+text',
            line={'width': 3},
            marker={'size': 8}
        ))

    layout = {
        'xaxis': {'title': 'Curso escolar'},
        'yaxis': {'title': ytitle},
        'width': 700,
        'height': 500
    }

    fig = dict(data=data, layout=layout)
    iplot(fig)

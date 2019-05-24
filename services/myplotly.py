import colorlover as cl
import numpy as np
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
from scipy import stats

init_notebook_mode(connected=True)


def hbar(x_values,
         y_values,
         trace_names=None,
         colors=None,
         title='',
         fig_size=(700, 1000)):
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
               is_percentage=True):

    cs = cl.scales['5']['seq'][colormap][1:]
    ls = np.linspace(0, 1, len(cs))
    colorscale = list(zip(ls, cs))

    trace_config = {
        'x': x_values,
        'y': y_values,
        'marker': {
            'color': y_values,
            'colorscale': colorscale
        }
    }
    if is_percentage:
        trace_config['text'] = [f'{y:.2f}%' for y in y_values]
        trace_config['hoverinfo'] = 'x + text'
    trace = go.Bar(trace_config)

    layout = go.Layout(
        title=title
    )

    data = [trace]

    fig = go.Figure(data=data, layout=layout)
    iplot(fig)


def cbar(x_labels, series, is_percentage=True):
    data = []
    for name, values in series.items():
        trace_config = {
            'x': x_labels,
            'y': values,
            'name': name,
        }
        if is_percentage:
            trace_config['text'] = [f'{y:.2f}%' for y in values]
            trace_config['hoverinfo'] = 'x + text + name'
        trace = go.Bar(trace_config)
        data.append(trace)

    layout = go.Layout(
        barmode='group'
    )

    fig = go.Figure(data=data, layout=layout)
    iplot(fig)


def scatter(xi, y, dot_labels, x_title=None, y_title=None):
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
        trace_config['text'] = [f'{y:.2f}%' for y in y_values]
        trace_config['hoverinfo'] = 'x + text'
    trace = go.Bar(trace_config)

    layout = go.Layout(
        title=title
    )

    data = [trace]

    fig = go.Figure(data=data, layout=layout)
    iplot(fig)

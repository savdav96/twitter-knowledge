import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools


class PlotlyClient:

    def __init__(self):
        plotly.tools.set_credentials_file(username='JohnDoe23', api_key='i53chdtaMo0EL8JwSyZ9')

    def print_lines_graph(self, x, y):
        trace0 = go.Scatter(
            x=x,
            y=y,
            mode='lines',
            name='lines'
        )
        data = [trace0]

        py.plot(data, filename='line-mode')
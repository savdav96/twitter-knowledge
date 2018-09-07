import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools


class PlotlyClient:

    def __init__(self):
        plotly.tools.set_credentials_file(username='JohnDoe23', api_key='i53chdtaMo0EL8JwSyZ9')

    def print_lines_graph(self, x, y, x_name, y_name):
        trace0 = go.Histogram(
            x=x,
            y=y,
            name='lines'
        )
        data = [trace0]

        # Edit the layout
        layout = dict(xaxis=dict(title=x_name),
                      yaxis=dict(title=y_name),
                      )

        fig = dict(data=data, layout=layout)

        py.plot(fig, filename='line-mode')

    def print_lines_markers_graph(self, x, y, x_name, y_name):
        trace0 = go.Scatter(
            x=x,
            y=y,
            mode='lines+markers',
            name='lines+markers'
        )
        data = [trace0]

        # Edit the layout
        layout = dict(xaxis=dict(title= x_name),
                      yaxis=dict(title= y_name),
                      )

        fig = dict(data=data, layout=layout)

        py.plot(fig, filename='line-mode')
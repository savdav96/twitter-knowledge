from src.models.PlotlyClient import PlotlyClient


class GraphController:

    def __init__(self):

        self.plotlyClient = PlotlyClient()

    def print_graph(self, graph, x, y):
        if graph == "lines":
            self.plotlyClient.print_lines_graph(x, y)


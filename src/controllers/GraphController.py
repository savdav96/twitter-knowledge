from src.models.plotly.PlotlyClient import PlotlyClient


class GraphController:

    def __init__(self):

        self.plotlyClient = PlotlyClient()

    def print_graph(self, graph, data):

        if graph == "Date-time / precision":
            x = []
            y = []
            for sample in data:
                if sample['Amount of analyzed tweets'] >= 10:
                    y.append(sample['Precision'])
                    x.append(sample['Date'])
            self.plotlyClient.print_bar_chart_graph(x, y, "Time", "Precision")

        if graph == "Date-time / recall":
            x = []
            y = []
            for sample in data:
                if sample['Amount of analyzed tweets'] >= 10:
                    y.append(sample['Recall'])
                    x.append(sample['Date'])
            self.plotlyClient.print_bar_chart_graph(x, y, "Time", "Recall")

        if graph == "Precision / recall":
            x = []
            y = []
            for sample in data:
                if sample['Amount of analyzed tweets'] >= 10:
                    x.append(sample['Precision'])
                    y.append(sample['Recall'])
            self.plotlyClient.print_bar_chart_graph(x, y, "Precision", "Recall")

        if graph == "Amount of analyzed tweets / precision":
            x = []
            y = []
            number_of_tweets = 0
            for sample in data:
                if sample['Amount of analyzed tweets'] >= 10:
                    y.append(sample['Precision'])
                    number_of_tweets += sample['Amount of analyzed tweets']
                    x.append(number_of_tweets)
            self.plotlyClient.print_bar_chart_graph(x, y, "Amount of analyzed tweets", "Precision")

        if graph == "Amount of analyzed tweets / precision (confidence limit for FP > 0.3)":
            x = []
            y = []
            number_of_tweets = 0
            k = 0
            for sample in data:
                k += 1
                TP = 0;
                FP = 0;
                for relation in sample['Relations']:
                    # first two elements of dictionary hasn't the field "Test result"
                    if k <= 2:
                        break

                    if relation['Test result'] == 'TP' and relation['Relation'][0]['confidence'] > 0.3:
                        TP += 1
                    if relation['Test result'] == 'FP' and relation['Relation'][0]['confidence'] > 0.3:
                        FP += 1

                if sample['Amount of analyzed tweets'] >= 10:
                    if k > 2:
                        if TP + FP == 0:
                            y.append(1)
                        else:
                            y.append(TP / (TP + FP))

                    number_of_tweets += sample['Amount of analyzed tweets']
                    x.append(number_of_tweets)

            self.plotlyClient.print_bar_chart_graph(x, y, "Amount of analyzed tweets", "Precision")

        if graph == "Date-time / precision (confidence limit for FP > 0.3)":
            x = []
            y = []
            k = 0
            for sample in data:
                k += 1
                TP = 0;
                FP = 0;
                for relation in sample['Relations']:
                    # first two elements of dictionary hasn't the field "Test result"
                    if k <= 2:
                        break

                    if relation['Test result'] == 'TP' and relation['Relation'][0]['confidence'] > 0.3:
                        TP += 1
                    if relation['Test result'] == 'FP' and relation['Relation'][0]['confidence'] > 0.3:
                        FP += 1

                if sample['Amount of analyzed tweets'] >= 10:
                    if k > 2:
                        if TP + FP == 0:
                            y.append(1)
                        else:
                            y.append(TP / (TP + FP))

                    x.append(sample['Date'])

            self.plotlyClient.print_bar_chart_graph(x, y, "Date-time", "Precision")

        if graph == "Date-time / %TN":
            x = []
            y = []
            k = 0
            for sample in data:
                k += 1
                TN = 0;
                for relation in sample['Relations']:
                    # first two elements of dictionary hasn't the field "Test result"
                    if k <= 2:
                        break

                    if relation['Test result'] == 'TN':
                        TN += 1

                if sample['Amount of analyzed tweets'] >= 10:
                    if k > 2:
                        y.append(TN/sample['Amount of analyzed tweets'])

                    x.append(sample['Date'])

            self.plotlyClient.print_bar_chart_graph(x, y, "Date-time", "%TN")

        if graph == "Date-time / %FN":
            x = []
            y = []
            k = 0
            for sample in data:
                k += 1
                FN = 0;
                for relation in sample['Relations']:
                    # first two elements of dictionary hasn't the field "Test result"
                    if k <= 2:
                        break

                    if relation['Test result'] == 'FN':
                        FN += 1

                if sample['Amount of analyzed tweets'] >= 10:
                    if k > 2:
                        y.append(FN/sample['Amount of analyzed tweets'])

                    x.append(sample['Date'])

            self.plotlyClient.print_bar_chart_graph(x, y, "Date-time", "%FN")

        if graph == "Date-time / %TP":
            x = []
            y = []
            k = 0
            for sample in data:
                k += 1
                TP = 0;
                for relation in sample['Relations']:
                    # first two elements of dictionary hasn't the field "Test result"
                    if k <= 2:
                        break

                    if relation['Test result'] == 'TP':
                        TP += 1

                if sample['Amount of analyzed tweets'] >= 10:
                    if k > 2:
                        y.append(TP/sample['Amount of analyzed tweets'])

                    x.append(sample['Date'])

            self.plotlyClient.print_bar_chart_graph(x, y, "Date-time", "%TP")

        if graph == "Date-time / %FP":
            x = []
            y = []
            k = 0
            for sample in data:
                k += 1
                FP = 0
                for relation in sample['Relations']:
                    # first two elements of dictionary hasn't the field "Test result"
                    if k <= 2:
                        break

                    if relation['Test result'] == 'FP':
                        FP += 1

                if sample['Amount of analyzed tweets'] >= 10:
                    if k > 2:
                        y.append(FP/sample['Amount of analyzed tweets'])

                    x.append(sample['Date'])

            self.plotlyClient.print_bar_chart_graph(x, y, "Date-time", "%FP")

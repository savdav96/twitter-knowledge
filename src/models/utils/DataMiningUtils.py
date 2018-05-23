
class DataMiningStatistics:     # Class that calculates precision and recaall

    def __init__(self):
        self.precision = 0
        self.recall = 0
        self.TP = 0     # number of recognized tweets with a known intent (relation)
        self.TN = 0     # number of unrecognized tweets with an unknown intent (relation)
        self.FP = 0     # number of recognized tweets with an unknown intent (relation)
        self.FN = 0     # number of unrecognized tweets with a known intent (relation)

    @property
    def get_precision(self):
        if self.TP + self.FP != 0:
            self.precision = self.TP / (self.TP + self.FP)
        return self.precision

    @property
    def get_recall(self):
        if self.TP + self.FN != 0:
            self.precision = self.TP / (self.TP + self.FN)
        return self.recall

    @property
    def sample_dimension(self):
        return self.TN + self.TP + self.FN + self.FP

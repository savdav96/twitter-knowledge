
class DataMiningStatistics:

    def __init__(self):
        self.precision = 0
        self.recall = 0
        self.TP = 0     #number of recognized tweets with a known intent (relation)
        self.TN = 0     #number of unrecognized tweets with an unknown intent (relation)
        self.FP = 0     #number of recognized tweets with an unknown intent (relation)
        self.FN = 0     #number of unrecognized tweets with a known intent (relation)


    def getPrecision(self):
        if self.TP + self.FP != 0:
            self.precision = self.TP / (self.TP + self.FP)
        return self.precision


    def getRecall(self):
        if self.TP + self.FN != 0:
            self.precision = self.TP / (self.TP + self.FN)
        return self.recall

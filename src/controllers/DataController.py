from models.utils.DataManagementUtils import DataManagementUtils


class DataController:

    def __init__(self):
        self.dataManagement = DataManagementUtils()

    def print_FP_FN(self):
        print()
        k = 0
        for i in self.dataManagement.get_data():
            k += 1
            for j in i['Relations']:
                if k < 2:               # first two elements of dictionary hasn't the field "Test result"
                    break
                if j['Test result'] == "FP" or j['Test result'] == "FN":
                    print(j['Tweet text'])

    def get_data(self):
        return self.dataManagement.get_data()

    def print_data(self):
        self.dataManagement.print_data()

    def save_data(self):
        self.dataManagement.save_data()

    def get_statistics(self):
        return self.dataManagement.get_statistics()

    def get_relations(self):
        return self.dataManagement.get_relations()

    def add_analyzed_tweet(self, id, raw_tweets):
        for tweet in raw_tweets:
            if tweet['id'] == id:
                self.dataManagement.add_analyzed_tweet(tweet)
                break

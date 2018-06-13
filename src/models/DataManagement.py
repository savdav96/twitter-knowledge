import pprint
import datetime
from models.utils.IOUtils import save_obj, load_obj
from models.utils.DataMiningUtils import DataMiningStatistics


class DataManagement:

    def __init__(self):
        self.cleaned_tweets = []
        self.raw_tweets = []
        self.analized_tweets = load_obj("analized tweets")
        self.relations = []
        self.data = load_obj("twitter knowledge data")
        self.statistics = DataMiningStatistics()

    def get_data(self):
        return self.data

    def get_statistics(self):
        return self.statistics

    def get_relations(self):
        return self.relations

    def print_data(self):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.data)

    def save_data(self):
        self.data.append({'Date': str(datetime.datetime.now()),
                          'Precision': float(self.statistics.get_precision()),
                          'Recall': float(self.statistics.get_recall()),
                          'Amount of analyzed tweets': self.statistics.sample_dimension,
                          'Relations': self.relations})
        save_obj(self.data, "twitter knowledge data")
        save_obj(self.analized_tweets, "analized tweets")

    def add_analized_tweet(self, tweet):
        self.analized_tweets.append(tweet)

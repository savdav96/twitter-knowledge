from src.models.twitter.TwitterClient import TwitterClient
import json
from src.models.utils.CleaningUtils import *


class TwitterController:

    def __init__(self):

        self.raw_tweets = []
        self.cleaned_tweets = []
        self.__client = TwitterClient()

    def search(self, q, num):
        """

        :param q: the input query
        :param num: the amount of tweets to search
        """
        self.__client.twitter_search(q, num)
        self.raw_tweets = self.__client.get_tweets()
        self.__clean_raw_tweets()

    def get_raw_tweets(self):
        return self.raw_tweets

    def get_cleaned_tweets(self):
        return self.cleaned_tweets

    def print_raw_tweets(self, pretty):

        for tweet in self.raw_tweets:
            if pretty:
                print("-------------------------------  BEGIN  -------------------------------\n")
                print(json.dumps(tweet._json, indent=4))
                print("\n-------------------------------   END   -------------------------------\n")
            else:
                print(tweet)

    def print_cleaned_tweets(self):
        for tweet in self.cleaned_tweets:
            print(tweet)

    def save_raw_tweets(self):
        # TODO: check function
        with open("tweets.json", "a") as f:
            f.writelines(["%s\n" % tweet for tweet in self.raw_tweets])

    def __clean_raw_tweets(self):
        for tweet in self.raw_tweets:
            self.cleaned_tweets\
                .append(clean(tweet["text"]))


if __name__ == "__main__":

    print("\n")
    tc = TwitterController()
    tc.search("Trump", 10)

    tc.print_cleaned_tweets()
    print("\n")
    tc.print_raw_tweets(False)

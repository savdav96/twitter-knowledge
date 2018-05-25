from tweepy import API
from src.models.twitter.Authenticator import *


class TwitterClient:

    def __init__(self):

        self.auth = authenticate(Davide)
        self.stream = None
        self.tweets = []

    def twitter_search(self, q, num):

        # Searches a finite set of tweets given number and the query

        api = API(self.auth)

        for tweet in api.search(q, lang='en', count=num):
            self.tweets.append(tweet._json)

    def get_tweets(self):
        return self.tweets

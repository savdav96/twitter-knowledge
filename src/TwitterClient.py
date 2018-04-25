from tweepy import Stream, API
from tweepy.streaming import StreamListener
from src.Authenticator import *
import json


class TwitterClient:

    def __init__(self):

        self.auth = authenticate(Davide)
        self.stream = None

    def stop_stream(self):

        # Stop stream attribute

        self.stream.disconnect()

    def start_stream(self, q):

        # Authenticate to twitter API and starts stream, uses query to filter tweets

        self.stream = Stream(self.auth, PrintListener())
        self.stream.filter(track=[str(q)], async=True)

    def search_no_stream(self, q, num, pretty=False):

        # Searches a finite set of tweets given number and the query

        api = API(self.auth)
        tweets = []
        for tweet in api.search(q, lang='en', count=num):
            tweets.append(tweet._json)
            if pretty:

                print("-------------------------------  BEGIN  -------------------------------\n")
                print(json.dumps(tweet._json, indent=4))
                print("\n-------------------------------   END   -------------------------------\n")

            else:
                print(tweet._json["text"])
        return tweets


class PrintListener(StreamListener):

    def on_data(self, data):

        # Saves tweets to JSON file and prints them

        try:
            with open('tweets.json', 'a') as f:
                f.write(data)
                print(data)
            f.close()
            return True

        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):

        # Shows network errors, False terminates stream

        print("Network error: " + status)
        if status == 420:
            return False
        return True

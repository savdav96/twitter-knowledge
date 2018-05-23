from tweepy import Stream, API
from src.models.twitter import PrintListener
import json


class TwitterClient:

    def __init__(self):

        self.auth = authenticate(Davide)
        self.stream = None
        self.print_listener = PrintListener()

    def stop_stream(self):

        # Stop stream attribute

        self.stream.disconnect()

    def start_stream(self, q):

        # Authenticate to twitter API and starts stream, uses query to filter tweets

        self.stream = Stream(self.auth, self.print_listener)
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




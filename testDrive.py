# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json
# Import the necessary methods from "twitter" library
from twitter import *


def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key) + ":")
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = "925076302054461440-J7jS7199LcWFwEIpoETERl5cp48AN7m"
ACCESS_SECRET = "0KHi9gwVNwCEZlhRNUQMXXyGYvfNAbDxeG4HSBfqgCCRl"
CONSUMER_KEY = "ZDyFnglZ5MwBkl2r3aqn8IEHt"
CONSUMER_SECRET = "D4vZIvtEv7sMZ2hj9KYfHvugS8xFXQ2KHJWRtJVmVEfUrWFjbF"

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()

# Print each tweet in the stream to the screen
# Here we set it to stop after getting 1000 tweets.
# You don't have to set it to stop, but can continue running
# the Twitter API to collect data for days or even longer.

'''tweet_count = 10
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print(json.dumps(tweet))

    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)

    if tweet_count <= 0:
        break
'''

tweet_count = 50
t = Twitter(auth=oauth)
query = t.search.tweets(q="china from:realdonaldtrump")  # https://developer.twitter.com/en/docs/tweets/search/guides/standard-operators
#print("a"+str(query))

for tweet in query["statuses"]:                     # scendi nella pagina web fino alla tabella con gli standard search operators
    print(tweet["text"])
    print("\n")
    tweet_count -= 1
    if tweet_count <= 0:
        break
#print("Dati utente:\n")
#print(tweet["user"])
#pretty(tweet["user"], 1) #pretty serve per non stampare tutto su una riga

'''
https://twitter.com/search?l=
en&q=
tutto1%3B%20tutto2%3B%20tutto3%20
%22ciao%2C%20sono%20gino%22
%20almeno1%3B%20OR%20almeno2%3B%20OR%20almeno3%20-nessuna1%3B%20-nessuna2%3B%20-nessuna3%20%23hashtag1%2C%20OR%20%23hashtag2%3B%20OR%20%23hashtah3%20from%3Autente1%3B%20OR%20from%3Autente2%3B%20OR%20from%3Autente3%20to%3Aautente1%3B%20OR%20to%3Aautente2%3B%20OR%20to%3Aautente3%20%40menzionato1%3B%20OR%20%40menzionato2%3B%20OR%20%40menzionato3%20near%3A%22Mantova%2C%20Lombardia%22%20within%3A15mi%20since%3A2018-03-04%20until%3A2018-03-12&src=typd
'''

'''
class OutputStreamListener(StreamListener):

    def __init__(self, filename):
        self.filename=filename

    # Override
    def on_data(self, data):
        try:
            print(data)
            with open(self.filename, 'a') as file:
                file.write(data)
            return True
        except BaseException:
            print("Error in method on_data: %s" % str(BaseException))

    # Override
    def on_error(self, status_code):
        if status_code==420:
            return False
        print("Connection Error: " +status_code)
        return True
''' #Output

'''
class Streamer():

    def getStream(self, hashtags, filename):
        listener = OutputStreamListener(filename)
        stream = Stream(self.auth, listener)
        stream.filter(hashtags)
''' #streamer


from tweepy import API, Cursor, Stream
from tweepy.streaming import StreamListener
from Authenticator import *

class TwitterClient():

    def __init__(self):
        self.auth = authenticate(Davide)
        self.api = API(self.auth)

    def home_timeline(self, num):
        for status in Cursor(self.api.home_timeline).items(num):
            self.__process_or_store__(status._json)

    def friends(self):
        for friend in Cursor(self.api.friends).items():
            self.__process_or_store__(friend._json)

    def user_timeline(self):
        for tweet in Cursor(self.api.user_timeline).items():
            self.__process_or_store__(tweet._json)

    def search(self, q):
        results = self.api.search(q)
        self.__process_or_store__(results)

    def stream_tweets(self, q):
        stream = Stream(self.auth, PrintListener())
        stream.filter(track=[str(q)])

    def __process_or_store__(tweet):
        print(tweet)
        return

class PrintListener(StreamListener):

    def on_data(self, data):
        try:
            #with open('python.json', 'a') as f:
                print(data)
                #f.write(data)
               # return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

t = TwitterClient()

t.stream_tweets("trump")
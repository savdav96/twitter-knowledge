from tweepy import API, Cursor, OAuthHandler, Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from keys import Davide


class MyListener(StreamListener):

    # Override
    def on_data(self, raw_data):
        print(raw_data)
        return True

    # Override
    def on_error(self, status_code):
        print(status_code)
        return True


class Authenticator():

    def authenticate(keys):
        auth = OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
        auth.set_access_token(keys["access_token"], keys["access_token_secret"])
        return auth

class Streamer():

    def

if __name__ == "__main__":
    listener = MyListener()

    stream = Stream(Authenticator.authenticate(Davide.keys), listener)
    stream.filter(track=['donald trump', 'hillary clinton'])

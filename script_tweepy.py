from tweepy import API, Cursor, OAuthHandler, Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from keys import *

class Authenticator():

    def authenticate(keys):
        auth = OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
        auth.set_access_token(keys["access_token"], keys["access_token_secret"])
        return auth

if __name__ == "__main__":

    query = input("Enter query:\n")
    Twitter = API(Authenticator.authenticate(Davide.keys))
    #API.search("from:matteorenzi")




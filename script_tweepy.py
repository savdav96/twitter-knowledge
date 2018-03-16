from tweepy import API
from tweepy import OAuthHandler
from keys import *

class Authenticator():

    def authenticate(keys):
        auth = OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
        auth.set_access_token(keys["access_token"], keys["access_token_secret"])
        return auth

class Searcher():

    def results(q):
        twitter = API(Authenticator.authenticate(Davide.keys))
        result=twitter.search(q)
        print(result)
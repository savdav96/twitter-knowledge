from src.models.twitter.TwitterClient import TwitterClient


class TwitterController:

    def __init__(self):
        self.tweets = []
        self.client = TwitterClient()

    def search(self, q, mode):

        if mode == "normal":
            self.tweets = self.client.search_no_stream(q, 5, True)
        elif mode == "stream":
            self.tweets = self.client.start_stream(q)
        else:
            return

    def get_tweets(self):
        return self.tweets

from tweepy import Stream
from tweepy.streaming import StreamListener
from Authenticator import *


class TwitterClient:

    def stop_stream(self):

        # Stop stream attribute

        self.stream.disconnect()

    def start_stream(self, q):

        # Authenticate to twitter API and starts stream, uses query to filter tweets

        auth = authenticate(Davide)
        self.stream = Stream(auth, PrintListener())
        self.stream.filter(track=[str(q)], async=True)


class PrintListener(StreamListener):

    def on_data(self, data):

        # Saves tweets to JSON file and prints them

        try:
            with open('tweets.json', 'w') as f:
                f.write(data)
                print(data)
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


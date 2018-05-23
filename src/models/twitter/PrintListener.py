from tweepy.streaming import StreamListener


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

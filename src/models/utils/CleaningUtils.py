import re


def clean(tweet):
        cleaned_tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|"
                                        "([^0-9A-Za-z \t])|"
                                        "(\w+:\/\/\S+)|"
                                        "(^RT[\s]+)",
                                        ' ', tweet).split())
        return cleaned_tweet


if __name__ == "__main__":

    tests = [
        "@peter I really love that shirt at #Macy. http://bet.ly//WjdiW4",
        "@shawn Titanic tragedy could have been prevented Economic Times: Telegraph.co.uk  http://bet.ly/tuN2wx",
        "I am at Starbucks http://4sh.com/samqUI (7419 3rd ave, at 75th, Brooklyn)",
    ]

    for string in tests:
        clean(string)
        print(string)


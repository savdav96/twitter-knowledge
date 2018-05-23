import re


emoticons_str = r"""
    (?:
        [:=;] 
        [oO\-]?
        [D\)\]\(\]/\\OpP]
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
    ]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)


def tokenize(s):
    return tokens_re.findall(s)


def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


def get_tokens(tweets):

    tokens = []
    for tweet in tweets:
        token = preprocess(tweet["text"])
        tokens.append(token)

    return tokens


def get_text(raw_tweets):

    tweets = []
    for raw_tweet in raw_tweets:
        tweets.append(raw_tweet["text"])

    return tweets


def cleaner(raw_tweets):

    cleaned_tweets = []
    tweets = get_text(raw_tweets)

    for tweet in tweets:
        cleaned_tweet = tweet.decode("utf8").encode('ascii', 'ignore')
        cleaned_tweets.append(cleaned_tweet)


    return cleaned_tweets

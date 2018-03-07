import tweepy, textblob

consumer_key = 'FcL6EihLddInuDGYHtwzxkJCO'
consumer_secret = '2jJVYrgNeaVoLsUybLaMPMf1JowfRPVq0mDr4ntBGODzOmaSw0'

access_token = '624866981-E2jP1WZB2L6NHv5yp0q7cRBu7qrXsKpavyl5atpb'
access_token_secret = 'ZePuOH4644uTxSdR0ORueszpPERgyGEmDhTFWBeKGLHst'

#script veloce utilizzando tweepy
# TODO vedere documentazione - dove, dio merda?

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print("Connesso a Twitter!\n")
q = input("Digita query di ricerca:\n")
lang = input("Digita la lingua di ricerca in formato ISO 639-1\n")

public_tweets = api.search(q, lang, "default", "100")


for tweet in public_tweets:
    print(tweet.text)
    analysis = textblob.TextBlob(tweet.text)
    print(analysis.sentiment)
    print("\n")
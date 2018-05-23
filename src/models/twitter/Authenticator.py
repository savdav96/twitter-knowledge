from tweepy import OAuthHandler

Davide = \
    {
    'consumer_key': 'FcL6EihLddInuDGYHtwzxkJCO',
    'consumer_secret': '2jJVYrgNeaVoLsUybLaMPMf1JowfRPVq0mDr4ntBGODzOmaSw0',
    'access_token': '624866981-E2jP1WZB2L6NHv5yp0q7cRBu7qrXsKpavyl5atpb',
    'access_token_secret': 'ZePuOH4644uTxSdR0ORueszpPERgyGEmDhTFWBeKGLHst'
    }

Elio = \
    {
    'consumer_key': 'ZDyFnglZ5MwBkl2r3aqn8IEHt',
    'consumer_secret': 'D4vZIvtEv7sMZ2hj9KYfHvugS8xFXQ2KHJWRtJVmVEfUrWFjbF',
    'access_token': '925076302054461440-J7jS7199LcWFwEIpoETERl5cp48AN7m',
    'access_secret': '0KHi9gwVNwCEZlhRNUQMXXyGYvfNAbDxeG4HSBfqgCCRl',
    }  # This dictionary may be outdated


def authenticate(keys):

    # Uses OAuthHandler to access twitter private remote app

    auth = OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
    auth.set_access_token(keys["access_token"], keys["access_token_secret"])
    return auth

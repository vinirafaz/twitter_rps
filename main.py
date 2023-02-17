import tweepy
import os
from dotenv import load_dotenv
from jokenpo import Jokenpo


#TODO: Isolate env variables
load_dotenv()
CONSUMER_KEY_TT = os.getenv('CONSUMER_KEY_TT')
CONSUMER_SECRET_TT = os.getenv('CONSUMER_SECRET_TT')
ACCESS_TOKEN_TT = os.getenv('ACCESS_TOKEN_TT')
ACESS_TOKEN_SECRET_TT = os.getenv('ACESS_TOKEN_SECRET_TT')


# Authenticate to Twitter
def authentication_tt():
    auth = tweepy.OAuthHandler(CONSUMER_KEY_TT, CONSUMER_SECRET_TT)
    auth.set_access_token(ACCESS_TOKEN_TT, ACESS_TOKEN_SECRET_TT)
    return tweepy.API(auth)


if __name__ == '__main__':
    tweet = Jokenpo().result_text

    api = authentication_tt()

    api.update_status(tweet)

    # try:
    #
    # except tweepy.TweepyException as error:
    #     if error == 187:
    #         # Do something special
    #         print('duplicate message')
    #     else:
    #         raise error

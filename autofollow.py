import tweepy
from credentials import *

# twitter auths
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# loop
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print (follower.screen_name)

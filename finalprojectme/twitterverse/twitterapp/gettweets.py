import tweepy
from tweepy import *

consumer_key = 'QLcDOtaD79Vc9zb6zc5vrqpVH'
consumer_secret = 'Sl2GOvNBBegz6YNgIHIf2tQZLY8KXjzfyMVvjhgepsZ0gUaILW'
access_token = '856096822619721728-AvtfUa0VvgnOucRAFzC4pqpva6EJe6B'
access_token_secret = 'l1wbH8ACOFh7AZ8s4AI9cOnPdc2lnK7Gxsps33DFvMFis'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


results = api.search(q="Trump")

for result in results:
    print (result.text)

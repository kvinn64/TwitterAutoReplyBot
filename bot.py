#!/usr/bin/env python
import tweepy
import pickle
import time, random

##########################################################################################
CONSUMER_KEY = "vT79NBViS7AHUoMbGkrnd3LpM"                           #
CONSUMER_SECRET = "qYwhr0gVZR6dDC8D6BVpko2DzgzAFES76s8Bnc72yhUY9jui0u"                   #
ACCESS_TOKEN = "2244472284-cXNvtplvgV0Q2796yn5iJaMZABf9KsMWcVbQ9IG"                      #
ACCESS_TOKEN_SECRET = "rljhOwrT9fYlokBPhwSNdEzNbJwZdGIGn5v38F0beDlKa"                    #
HASHTAG = "malming"                                                                         #
NUMBER_OF_TWEETS_TO_REPLY = 10                                                            #
TWEETS_TYPE = "mixed" #can be set to "mixed" or "popular" as well                       #
##########################################################################################
processed_tweets = []
fetched_tweets = []

try:
   with open('twts.pkl', 'rb') as f:
      processed_tweets=pickle.load(f)
except FileNotFoundError:
   pass

with open('tweets.txt') as tweetsFile:
    fetched_tweets = tweetsFile.readlines()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
 
twt = api.search_tweets(HASHTAG,result_type=TWEETS_TYPE,count=NUMBER_OF_TWEETS_TO_REPLY)
 
for s in twt:
   if s.id not in processed_tweets:
      time.sleep(3)
      sn = s.user.screen_name
      m = "@%s " %sn + random.choice(fetched_tweets).strip("\n") 
      api.update_status(status=m, in_reply_to_status_id = s.id)
      processed_tweets.append(s.id)
      print(s.id)

with open('twts.pkl', 'wb') as f:
   pickle.dump(processed_tweets, f)
print("Done replying!")

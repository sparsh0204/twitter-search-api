import tweepy
import time
import pprint
import json
import datetime

from django.conf import settings
from .models import Tweets

auth = tweepy.OAuthHandler(settings.YOUR_CONSUMER_KEY, settings.YOUR_CONSUMER_SECRET)
auth.set_access_token(settings.YOUR_ACCESS_KEY, settings.YOUR_ACCESS_SECRET)


api = tweepy.API(auth)



class MyStreamListener(tweepy.StreamListener):
    ''' Tweety stream listner for streaming twitter data '''
    var={}

    def __init__(self,start,duration):
        self.start = start
        self.duration = duration


    def on_data(self, data):
        ''' Function call after extracting data from twitter api by tweepy '''
        if(time.time()-self.start>self.duration):
            return (False)
        self.var = json.loads(data)
        tweet_time = self.var['timestamp_ms']
        dt = datetime.datetime.utcfromtimestamp(float(int(tweet_time)/1000))
        tweet_time = dt.isoformat() + 'Z'
        favorite_count = self.var['favorite_count']
        retweet_count = self.var['retweet_count']
        lang = self.var['lang']
        user_followers_count = self.var['user']['followers_count']
        user_screen_name = self.var['user']['screen_name']
        text = self.var['text']
        user_name = self.var['user']['name']
        Tweets.objects.create(text=text,tweet_time=tweet_time,user_name=user_name,
                              favorite_count=favorite_count,retweet_count=retweet_count,
                              lang=lang,user_followers_count=user_followers_count,
                              user_screen_name=user_screen_name).save() # Saving data into Database
        return (True)

    def on_error(self, status_code):
        ''' Function called if it encounters a error '''
        if status_code == 420:
            return False

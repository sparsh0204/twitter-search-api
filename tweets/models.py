from django.db import models

# Create your models here.

class Tweets(models.Model):
    ''' Represents a "Tweet" inside our system '''

    text = models.TextField(max_length=255, blank=True, null=True) # tweet text
    tweet_time = models.DateTimeField(auto_now=False, auto_now_add=False) # tweet time
    user_name = models.CharField(max_length=255, blank=True) # user's name
    favorite_count = models.IntegerField() # number of favorites on the tweet
    retweet_count = models.IntegerField() # number of retweet on the tweet
    lang = models.CharField(max_length=10, blank=True) # language of the tweet
    user_followers_count = models.IntegerField() # number of followers of the user
    user_screen_name = models.CharField(max_length=255, blank=True) # user's screen name

    def __str__(self):
        ''' Django uses this when it needs to convert the object to a string '''
        return self.user_name

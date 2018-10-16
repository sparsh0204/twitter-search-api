# from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField, Serializer
from rest_framework import serializers
from .models import Tweets

class GetDataSerializer(serializers.Serializer):
    ''' Serializer for getting filter and duration of streaming from user '''
    filter = serializers.CharField(max_length=20, required=False)
    duration = serializers.IntegerField(required=False)

class TweetsSerializer(serializers.ModelSerializer):
    ''' Serializer to return tweets data asked by user '''
    tweet_time = serializers.DateTimeField()

    class Meta:
        model = Tweets
        fields = ('text','tweet_time','user_name','favorite_count','retweet_count','lang','user_followers_count','user_screen_name',)

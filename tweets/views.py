from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from . import serializers
from .twitterdata import MyStreamListener
from .models import Tweets
import datetime
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters
from django_filters import rest_framework as dffilters
from rest_framework_csv import renderers as r
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from django.conf import settings

import tweepy
import time
import pprint
import json

# tweepy authantication setup
auth = tweepy.OAuthHandler(settings.YOUR_CONSUMER_KEY, settings.YOUR_CONSUMER_SECRET)
auth.set_access_token(settings.YOUR_ACCESS_KEY, settings.YOUR_ACCESS_SECRET)


api = tweepy.API(auth)


class GetFilterDataView(APIView):
    ''' View to get filter and duration from user '''
    serializer_class = serializers.GetDataSerializer

    def get(self, request, format=None):
        ''' GET mothod of the view called when user request GET '''
        return Response({'filter':'Enter the filter you want to apply',
                         'duration':"Duration in second(s)(min = 5sec) for which you want to stream the data.(default = 5sec)"})

    def post(self, request):
        ''' POST mothod of the view called when user request POST '''
        serializer = serializers.GetDataSerializer(data=request.data)

        if serializer.is_valid():
            keyword = serializer.data.get('filter')
            duration = serializer.data.get('duration')
            if keyword is None:
                keyword = ''
            if duration is None or int(duration)<5:
                duration = 5
            print(settings.YOUR_ACCESS_KEY,settings.YOUR_CONSUMER_KEY)
            myStreamListener = MyStreamListener(start=time.time(),duration=duration)
            myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener(start=time.time(),duration=duration))
            myStream.filter(track=[keyword], async=True)
            return Response({'keyword':keyword,'duration':duration})
        else:
            return Response(serializer.error, status= status.HTTP_400_BAD_REQUEST)


class ListTweetsFilter(dffilters.FilterSet):
    ''' Filtering class for filtering data '''
    tweet_time = dffilters.DateTimeFromToRangeFilter()
    text__exact = dffilters.CharFilter(field_name="text", lookup_expr="iexact")
    user_name__exact = dffilters.CharFilter(field_name="user_name", lookup_expr="iexact")
    user_screen_name__exact = dffilters.CharFilter(field_name="user_screen_name", lookup_expr="iexact")
    favorite_count__exact = dffilters.CharFilter(field_name="favorite_count", lookup_expr="iexact")
    user_followers_count__exact = dffilters.CharFilter(field_name="user_followers_count", lookup_expr="iexact")
    retweet_count__exact = dffilters.CharFilter(field_name="retweet_count", lookup_expr="iexact")

    class Meta:
        model = Tweets
        fields = {
            'text':['startswith', 'endswith', 'contains'],
            'user_name':['startswith', 'endswith', 'contains'],
            'user_screen_name':['startswith', 'endswith', 'contains'],
            'favorite_count':['lt','gt'],
            'user_followers_count':['lt','gt'],
            'retweet_count':['lt','gt'],
            'tweet_time': [],
        }


class StandardResultsSetPagination(PageNumberPagination):
    ''' Pagination class for pagination '''
    page_size = 20
    page_size_query_param = 'page_size'

class ListTweetsView(generics.ListAPIView):
    ''' View to list data to user along with filteration '''
    serializer_class = serializers.TweetsSerializer # serializer class
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter,)
    search_fields = ('user_name', 'text') # filter user for searching
    ordering_fields = ('text', 'tweet_time')
    filter_class = ListTweetsFilter # Filtering class to filter data
    pagination_class = StandardResultsSetPagination # pagination of data

    def get_queryset(self):
        return Tweets.objects.all()


class CsvTweetsView(generics.ListAPIView):
    ''' View to download data as CSV for user along with filteration '''
    serializer_class = serializers.TweetsSerializer # serializer class
    renderer_classes = (r.CSVRenderer, ) # rendering class to render data as csv
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter,)
    search_fields = ('user_name', 'text') # fields used for searching
    ordering_fields = ('text', 'tweet_time') # fileds user for sorting
    filter_class = ListTweetsFilter # Filtering class to filter data

    def get_queryset(self):
        return Tweets.objects.all()

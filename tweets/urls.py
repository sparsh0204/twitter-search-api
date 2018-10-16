from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    GetFilterDataView,
    ListTweetsView,
    CsvTweetsView
)


urlpatterns = [
    url(r'^stream/$', GetFilterDataView.as_view(), name='get_data'), # route for streaming data
    url(r'^list/$', ListTweetsView.as_view(), name='list_tweets'), # route for listing data
    url(r'^list/csv/$', CsvTweetsView.as_view(), name='csv_tweets') # route for downloading csv


]

urlpatterns = format_suffix_patterns(urlpatterns)

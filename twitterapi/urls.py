from django.conf.urls import url, include
from django.contrib import admin
from django.views import generic
from rest_framework.schemas import get_schema_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include("tweets.urls", namespace='tweets')), # route for tweets app
]

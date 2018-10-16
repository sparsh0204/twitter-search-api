from django.contrib import admin
from django.apps import apps

tweets = apps.get_app_config('tweets')

for model_name, model in tweets.models.items():
    admin.site.register(model)

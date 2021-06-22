from django.contrib import admin
from django.urls import path, include, views


urlpatterns = [
    path('', include('website.urls')),
    path('', include('api.urls')),
    path('', include('predictor.urls')),
]

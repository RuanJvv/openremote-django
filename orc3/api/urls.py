from django.urls import path
from . import views


urlpatterns = [
    path('api/postdata', views.get)
]

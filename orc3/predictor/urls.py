from django.urls import path
from . import views


urlpatterns = [
    path('predictor/getdata', views.get),
    path('predictor/response', views.get),
]

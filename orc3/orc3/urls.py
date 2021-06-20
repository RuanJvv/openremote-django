from django.contrib import admin
from django.urls import path, include
from predictor import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('', include('api.urls')),
    path('ml/', views.call_model.as_view())
]

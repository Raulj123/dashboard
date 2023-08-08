from django.contrib import admin
from django.urls import path, include
from . import views
app_name="domain"

urlpatterns = [
    path('', views.dashboard_view)
]

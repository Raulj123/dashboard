from django.contrib import admin
from django.urls import path, include
from . import views
app_name="domain"


urlpatterns = [
    path('', views.dashboard_view, name="home"),
    path('income/', views.income_view, name="income"),
    path('user_create/', views.user_registration, name="user_registration"),
    path('user_sign_in/', views.sign_in, name="sign_in"),
    path('logout/', views.logout_view, name="logout_view"),
]

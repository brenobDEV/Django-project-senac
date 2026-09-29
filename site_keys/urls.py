from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path( '', views.home, name='home'),
    path('login/', views.login, include('django.contrib.auth.urls')),
    path('keys_shop/', views.keys_shop, name='keys_shop'),
]
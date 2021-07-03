from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name='index'),
    path('aboutus', views.about,name='about'),
    path('shop', views.shop,name='shop'),

]

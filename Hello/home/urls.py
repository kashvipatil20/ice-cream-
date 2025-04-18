from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("services2", views.services2, name='services2'),
    path("services3", views.services3, name='services3'),
    path('search', views.search, name='search'),  
    
]


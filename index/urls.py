from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('bar/', views.bar_page, name='bar'),
    path('restaurant/', views.restaurant_page, name='restaurant'),
    path('room/id/<int:pk>/', views.room_page, name='room'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('missionary-work/', views.missionary_work, name='missionary_work'),
    path('latest-mission/', views.latest_mission, name='latest_mission'),
    path('media/', views.media, name='media'),
    path('contact/', views.contact, name='contact'),
]

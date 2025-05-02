from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('missionary-work/', views.missionary_work, name='missionary_work'),
    path('latest-mission/', views.latest_mission, name='latest_mission'),
    path('media/', views.media, name='media'),
    path('contact/', views.contact, name='contact'),

    # Website Guide URLs
    path('website-guide/', views.website_guide, name='website_guide'),
    path('website-guide/part1/', views.website_guide_part1, name='website_guide_part1'),
    path('website-guide/part2/', views.website_guide_part2, name='website_guide_part2'),
    path('website-guide/part3/', views.website_guide_part3, name='website_guide_part3'),
    path('website-guide/part4/', views.website_guide_part4, name='website_guide_part4'),
]

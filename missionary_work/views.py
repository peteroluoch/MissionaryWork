from django.shortcuts import render
import os
from django.conf import settings
from .models import MissionaryPhoto



def home(request):
    featured_photos = MissionaryPhoto.objects.filter(featured=True).order_by('-date_taken')[:5]
    south_sudan_photo = MissionaryPhoto.objects.filter(category__iexact='South Sudan').first()
    kenya_photo = MissionaryPhoto.objects.filter(category__iexact='Kenya').first()
    rwanda_photo = MissionaryPhoto.objects.filter(category__iexact='Rwanda').first()

    non_recent_photos = MissionaryPhoto.objects.filter(featured=False).order_by('-date_taken')[:3]

    global_mission_photos = MissionaryPhoto.objects.filter(category='Global Missionary Work', featured=True).order_by('-date_taken')

    # Assign individual photos for unique cards
    photo1 = non_recent_photos[0] if len(non_recent_photos) > 0 else None
    photo2 = non_recent_photos[1] if len(non_recent_photos) > 1 else None
    photo3 = non_recent_photos[2] if len(non_recent_photos) > 2 else None

    context = {
        'global_mission_photos': global_mission_photos,
        'featured_photos': featured_photos,
        'south_sudan_photo': south_sudan_photo,
        'kenya_photo': kenya_photo,
        'rwanda_photo': rwanda_photo,
        'photo1': photo1,
        'photo2': photo2,
        'photo3': photo3,
    }
    return render(request, 'missionary_work/home.html', context)

def about(request):
    """View for the about page"""
    return render(request, 'missionary_work/about.html')

def missionary_work(request):
    """View for the missionary work page"""
    return render(request, 'missionary_work/missionary_work.html')

def latest_mission(request):
    """View for the latest mission page"""
    return render(request, 'missionary_work/latest_mission.html')

def media(request):
    """View for the media page"""
    # Get South Sudan photos
    south_sudan_photos = []
    photo_dir = os.path.join(settings.MEDIA_ROOT, 'missionary_photos', 'south_sudan_day1')

    if os.path.exists(photo_dir):
        for filename in os.listdir(photo_dir):
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                photo_path = os.path.join('missionary_photos', 'south_sudan_day1', filename)
                title = filename.replace('_', ' ').replace('.jpg', '').replace('.jpeg', '').replace('.png', '').title()

                # Create a dictionary with photo information
                photo = {
                    'path': photo_path,
                    'title': title,
                    'description': 'South Sudan missionary work by Pastor Prince Obasi-Ike',
                }
                south_sudan_photos.append(photo)

    context = {
        'south_sudan_photos': south_sudan_photos,
    }

    return render(request, 'missionary_work/media.html', context)

def contact(request):
    """View for the contact page"""
    return render(request, 'missionary_work/contact.html')

# Website Guide Views
def website_guide(request):
    """View for the main website guide page"""
    return render(request, 'missionary_work/website_guide.html')

def website_guide_part1(request):
    """View for website guide part 1: Introduction and Overview"""
    return render(request, 'missionary_work/website_guide_part1.html')

def website_guide_part2(request):
    """View for website guide part 2: Website Features and Pages"""
    return render(request, 'missionary_work/website_guide_part2.html')

def website_guide_part3(request):
    """View for website guide part 3: Media Resources and Involvement"""
    return render(request, 'missionary_work/website_guide_part3.html')

def website_guide_part4(request):
    """View for website guide part 4: Contact Information"""
    return render(request, 'missionary_work/website_guide_part4.html')

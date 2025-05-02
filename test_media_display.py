import os
import django
from django.conf import settings

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pastor_prince_website.settings')
django.setup()

# Now we can import Django models
from missionary_work.models import MissionaryPhoto

# Check if the media directory exists
media_dir = settings.MEDIA_ROOT
print(f"Media root directory: {media_dir}")
print(f"Media directory exists: {os.path.exists(media_dir)}")

# Check if the South Sudan photos directory exists
south_sudan_dir = os.path.join(media_dir, 'missionary_photos', 'south_sudan_day1')
print(f"South Sudan photos directory: {south_sudan_dir}")
print(f"South Sudan directory exists: {os.path.exists(south_sudan_dir)}")

# List all files in the South Sudan directory
if os.path.exists(south_sudan_dir):
    print("\nFiles in South Sudan directory:")
    for filename in os.listdir(south_sudan_dir):
        print(f"- {filename}")

# Check if we have any MissionaryPhoto objects in the database
print("\nMissionaryPhoto objects in database:")
photos = MissionaryPhoto.objects.all()
print(f"Number of photos: {photos.count()}")

# Create MissionaryPhoto objects for each image in the South Sudan directory
if os.path.exists(south_sudan_dir):
    print("\nCreating MissionaryPhoto objects for South Sudan photos...")
    for filename in os.listdir(south_sudan_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            title = filename.replace('_', ' ').replace('.jpg', '').replace('.jpeg', '').replace('.png', '').title()
            
            # Check if a photo with this title already exists
            if not MissionaryPhoto.objects.filter(title=title).exists():
                photo = MissionaryPhoto(
                    title=title,
                    description='South Sudan missionary work by Pastor Prince Obasi-Ike',
                    location='South Sudan',
                    category='South Sudan Day 1',
                    image=os.path.join('missionary_photos', 'south_sudan_day1', filename)
                )
                photo.save()
                print(f"Created photo: {title}")
            else:
                print(f"Photo already exists: {title}")

# Check if we have any MissionaryPhoto objects in the database after creation
print("\nMissionaryPhoto objects in database after creation:")
photos = MissionaryPhoto.objects.all()
print(f"Number of photos: {photos.count()}")
for photo in photos:
    print(f"- {photo.title}: {photo.image}")

print("\nTest completed successfully!")

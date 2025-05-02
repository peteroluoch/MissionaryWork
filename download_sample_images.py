import os
import requests
from PIL import Image
from io import BytesIO
import random
import datetime

# Create directories if they don't exist
os.makedirs('media/missionary_photos/south_sudan_day1', exist_ok=True)
os.makedirs('static/images/backgrounds', exist_ok=True)
os.makedirs('static/images/icons', exist_ok=True)
os.makedirs('static/images/logos', exist_ok=True)
os.makedirs('static/images/sliders', exist_ok=True)

# Sample image URLs for missionary photos (South Sudan)
missionary_photo_urls = [
    "https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",  # Community gathering
    "https://images.unsplash.com/photo-1504159506876-f8338247a14a?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",  # Village scene
    "https://images.unsplash.com/photo-1532629345422-7515f3d16bb6?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",  # People praying
    "https://images.unsplash.com/photo-1470115636492-6d2b56f9146d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",  # Worship
    "https://images.unsplash.com/photo-1541802645635-11f2286a7482?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",  # Children
]

# Sample image URLs for static images
background_urls = [
    "https://images.unsplash.com/photo-1489657780376-e0d8630c4bd3?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",  # Africa map
    "https://images.unsplash.com/photo-1517299321609-52687d1bc55a?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",  # Texture
]

slider_urls = [
    "https://images.unsplash.com/photo-1504159506876-f8338247a14a?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80",  # Village
    "https://images.unsplash.com/photo-1532629345422-7515f3d16bb6?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80",  # Prayer
    "https://images.unsplash.com/photo-1470115636492-6d2b56f9146d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80",  # Worship
]

logo_urls = [
    "https://via.placeholder.com/200x200.png?text=Pastor+Prince+Logo",
]

icon_urls = [
    "https://via.placeholder.com/64x64.png?text=Icon+1",
    "https://via.placeholder.com/64x64.png?text=Icon+2",
    "https://via.placeholder.com/64x64.png?text=Icon+3",
]

def download_image(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        img = Image.open(BytesIO(response.content))
        img.save(save_path)
        print(f"Downloaded: {save_path}")
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

# Download missionary photos
print("Downloading missionary photos...")
for i, url in enumerate(missionary_photo_urls):
    file_name = f"south_sudan_day1_{i+1}.jpg"
    save_path = os.path.join('media/missionary_photos/south_sudan_day1', file_name)
    download_image(url, save_path)

# Download background images
print("\nDownloading background images...")
for i, url in enumerate(background_urls):
    file_name = f"background_{i+1}.jpg"
    save_path = os.path.join('static/images/backgrounds', file_name)
    download_image(url, save_path)

# Download slider images
print("\nDownloading slider images...")
for i, url in enumerate(slider_urls):
    file_name = f"slider_{i+1}.jpg"
    save_path = os.path.join('static/images/sliders', file_name)
    download_image(url, save_path)

# Download logo images
print("\nDownloading logo images...")
for i, url in enumerate(logo_urls):
    file_name = f"logo_{i+1}.png"
    save_path = os.path.join('static/images/logos', file_name)
    download_image(url, save_path)

# Download icon images
print("\nDownloading icon images...")
for i, url in enumerate(icon_urls):
    file_name = f"icon_{i+1}.png"
    save_path = os.path.join('static/images/icons', file_name)
    download_image(url, save_path)

print("\nAll images downloaded successfully!")

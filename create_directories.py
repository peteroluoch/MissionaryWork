import os

# Define the directories to create
media_dirs = [
    'media/missionary_photos',
    'media/events',
    'media/testimonials',
    'media/sermons',
    'media/projects'
]

# Create each directory
for directory in media_dirs:
    os.makedirs(directory, exist_ok=True)
    print(f"Created directory: {directory}")

print("All directories created successfully!")

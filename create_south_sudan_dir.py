import os

# Create South Sudan Day 1 directory
directory = 'media/missionary_photos/south_sudan_day1'
os.makedirs(directory, exist_ok=True)
print(f"Created directory: {directory}")

# Verify the directory exists
if os.path.exists(directory):
    print(f"Confirmed: Directory {directory} exists!")
else:
    print(f"Error: Directory {directory} was not created!")

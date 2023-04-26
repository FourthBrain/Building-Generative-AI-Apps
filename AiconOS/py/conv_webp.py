
import os
from PIL import Image

# Set directory path
directory = '/Users/ali/Desktop/AiconOS/data/'

# Loop through all files in directory
for filename in os.listdir(directory):
    # Check if file is a PNG image
    if filename.endswith('.png'):
        # Open the image
        img = Image.open(os.path.join(directory, filename))
        # Calculate the new size
        width, height = img.size
        if width > height:
            new_width = 256
            new_height = int(height * (new_width / width))
        else:
            new_height = 256
            new_width = int(width * (new_height / height))
        # Resize the image
        img_resized = img.resize((new_width, new_height))
        # Save the resized image with "_resized" suffix
        new_filename = os.path.splitext(filename)[0] + '_resized' + os.path.splitext(filename)[1]
        img_resized.save(os.path.join(directory, new_filename))
        # Close the images
        img.close()
        img_resized.close()

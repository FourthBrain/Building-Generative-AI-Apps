from PIL import Image

# Open the source image
source_image = Image.open("/Users/ali/Desktop/AiconOS/ios_image_conv/image.png")

# Define the required icon sizes
icon_sizes = [
    (20, 20),
    (29, 29),
    (40, 40),
    (58, 58),
    (60, 60),
    (76, 76),
    (80, 80),
    (87, 87),
    (120, 120),
    (152, 152),
    (167, 167),
    (180, 180),
    (1024, 1024),
]

# Generate each icon size
for size in icon_sizes:
    # Resize the image
    resized_image = source_image.resize(size)

    # Save the image as an iOS icon
    file_name = f"ios_image_conv/generated_icons/icon_{size[0]}x{size[1]}.png"
    resized_image.save(file_name)

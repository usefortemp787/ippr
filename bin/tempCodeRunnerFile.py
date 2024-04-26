
import matplotlib.pyplot as plt
from PIL import Image

# Load the RGB image
rgb_image = Image.open('walchand.jpeg')

# Split the image into color channels
r, g, b = rgb_image.split()

# Define the enhancement factor for a specific channel (e.g., blue channel)
enhancement_factor = 1.5

# Enhance the blue channel
enhanced_b = b.copy()
for y in range(b.size[1]):
    for x in range(b.size[0]):
        enhanced_b.putpixel((x, y), min(int(b.getpixel((x, y)) * enhancement_factor), 255))


# Merge the enhanced blue channel with the original green and red channels
enhanced_image = Image.merge('RGB', (r, g, enhanced_b))

# Display the original and enhanced images
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(rgb_image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(enhanced_image)
plt.title('Enhanced Image')
plt.axis('off')

plt.show()

# Save the enhanced image
enhanced_image.save('enhanced_image.jpg')

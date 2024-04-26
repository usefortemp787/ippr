# import cv2
# import numpy as np

# # Load the RGB image
# rgb_image = cv2.imread('walchand.jpeg')

# # Extract the individual color channels
# b, g, r = cv2.split(rgb_image)

# # Define the enhancement factor for a specific channel (e.g., blue channel)
# enhancement_factor = 1.5

# # Enhance the blue channel by multiplying it with the enhancement factor
# enhanced_b = np.clip(b * enhancement_factor, 0, 255).astype(np.uint8)

# # Merge the enhanced blue channel with the original green and red channels
# enhanced_image = cv2.merge((enhanced_b, g, r))

# # Display the original and enhanced images
# cv2.imshow('Original Image', rgb_image)
# cv2.imshow('Enhanced Image', enhanced_image)

# # Save the enhanced image
# cv2.imwrite('enhanced_image.jpg', enhanced_image)

# # Wait for a key press and then close all windows
# cv2.waitKey(0)
# cv2.destroyAllWindows()





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

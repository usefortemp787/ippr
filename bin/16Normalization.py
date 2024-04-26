# import cv2
# import numpy as np

# # Function to normalize the image
# def normalize_image(image):
#     # Convert image to float32
#     image_float32 = image.astype(np.float32)
#     # Normalize image to range [0, 1]
#     normalized_image = image_float32 / 255.0
#     return normalized_image

# # Load the image
# image = cv2.imread('original_image.jpg')

# # Check if the image is loaded successfully
# if image is None:
#     print("Error: Unable to load image.")
# else:
#     # Convert the image to RGB
#     rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#     # Normalize the RGB image
#     normalized_image = normalize_image(rgb_image)

#     # Display the original and normalized images
#     cv2.imshow('Original Image', rgb_image)
#     cv2.imshow('Normalized Image', normalized_image)

#     cv2.waitKey(0)
#     cv2.destroyAllWindows()




import numpy as np
import matplotlib.pyplot as plt

# Function to normalize the image
def normalize_image(image):
    # Convert image to float32
    image_float32 = image.astype(np.float32)
    # Normalize image to range [0, 1]
    normalized_image = image_float32 / 255.0
    return normalized_image

# Load the image
image = plt.imread('original_image.jpg')

# Check if the image is loaded successfully
if image is None:
    print("Error: Unable to load image.")
else:
    # Normalize the image
    normalized_image = normalize_image(image)

    # Display the original and normalized images
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(normalized_image)
    plt.title('Normalized Image')
    plt.axis('off')

    plt.show()

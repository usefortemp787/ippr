import cv2
import numpy as np

# Function to apply threshold to the image
def apply_threshold(image, threshold_value):
    img = np.array(image)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j] > threshold_value:
                img[i, j] = 255  # White
            else:
                img[i, j] = 0    # Black
                
    return img

# Load the image
image = cv2.imread('original_image.jpg')

# Check if the image is loaded successfully
if image is None:
    print("Error: Unable to load image.")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold value
    threshold_value = 128

    # Apply thresholding
    binary_image = apply_threshold(gray_image, threshold_value)

    # Display the original, grayscale, and binary images
    cv2.imshow('Original Image', image)
    cv2.imshow('Grayscale Image', gray_image)
    cv2.imshow('Binary Image', binary_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

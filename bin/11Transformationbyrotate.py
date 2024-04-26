
# *with opencv

import cv2

# Function to rotate the image clockwise
def rotate_clockwise(image):
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    return rotated_image

# Function to rotate the image anti-clockwise
def rotate_anticlockwise(image):
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    return rotated_image

# Load the original image
original_image = cv2.imread('original_image.jpg')

# Rotate the image clockwise by 90 degrees
rotated_clockwise = rotate_clockwise(original_image)

# Rotate the image anti-clockwise by 90 degrees
rotated_anticlockwise = rotate_anticlockwise(original_image)

#Display the original and rotated images
cv2.imshow('Original Image', original_image)
cv2.imshow('Rotated Clockwise', rotated_clockwise)
cv2.imshow('Rotated Anti-clockwise', rotated_anticlockwise)

cv2.waitKey(0)
cv2.destroyAllWindows()










# * without opencv

from PIL import Image

# Function to rotate the image clockwise
def rotate_clockwise(image_path):
    with Image.open(image_path) as image:
        rotated_image = image.rotate(-90)  # Negative angle for clockwise rotation
    return rotated_image

# Function to rotate the image anti-clockwise
def rotate_anticlockwise(image_path):
    with Image.open(image_path) as image:
        rotated_image = image.rotate(90)  # Positive angle for anti-clockwise rotation
    return rotated_image

# Example usage
original_image_path = 'original_image.jpg'

# Rotate the image clockwise
rotated_clockwise = rotate_clockwise(original_image_path)

# Rotate the image anti-clockwise
rotated_anticlockwise = rotate_anticlockwise(original_image_path)

# Display the original and rotated images
Image.open(original_image_path).show()
rotated_clockwise.show()
rotated_anticlockwise.show()


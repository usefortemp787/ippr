import cv2
import numpy as np

# Function to translate (shift) the image
def translate_image(image, x, y):
    rows, cols = image.shape[:2]
    translation_matrix = np.float32([[1, 0, x], [0, 1, y]])
    translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows))
    return translated_image

# Load the original image
original_image = cv2.imread('original_image.jpg')

# Translate the image to the right by 20 units
translated_right = translate_image(original_image, 20, 0)

# Translate the image downwards by 10 units
translated_down = translate_image(original_image, 0, 10)

# Display the original and translated images
cv2.imshow('Original Image', original_image)
cv2.imshow('Translated Right', translated_right)
cv2.imshow('Translated Down', translated_down)

cv2.waitKey(0)
cv2.destroyAllWindows()

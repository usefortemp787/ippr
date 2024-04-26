# import cv2
# import numpy as np

# def intensity_slicing_preserve_background(image, lower_thresh, upper_thresh):
#     # Create a mask for pixels within the specified intensity range
#     mask = cv2.inRange(image, lower_thresh, upper_thresh)
    
#     # Preserve the background by applying bitwise AND operation between the mask and the original image
#     result_image = cv2.bitwise_and(image, image, mask=mask)
    
#     return result_image

# def intensity_slicing_non_preserve_background(image, lower_thresh, upper_thresh):
#     # Create a mask for pixels within the specified intensity range
#     mask = cv2.inRange(image, lower_thresh, upper_thresh)
    
#     # Invert the mask
#     inverted_mask = cv2.bitwise_not(mask)
    
#     # Set pixels outside the intensity range to a specific value (e.g., 255)
#     result_image = cv2.copyTo(image, inverted_mask)
    
#     return result_image

# # Load the grayscale image
# gray_image = cv2.imread('grayscale1.jpeg', cv2.IMREAD_GRAYSCALE)

# # Define the lower and upper thresholds for intensity slicing
# lower_thresh = 100
# upper_thresh = 200

# # Apply intensity slicing while preserving the background
# result_preserve_background = intensity_slicing_preserve_background(gray_image, lower_thresh, upper_thresh)

# # Apply intensity slicing without preserving the background
# result_non_preserve_background = intensity_slicing_non_preserve_background(gray_image, lower_thresh, upper_thresh)

# # Display the original image and the results
# cv2.imshow('Original Image', gray_image)
# cv2.imshow('Intensity Slicing (Preserve Background)', result_preserve_background)
# cv2.imshow('Intensity Slicing (Non-Preserve Background)', result_non_preserve_background)

# # Save the results
# cv2.imwrite('intensity_slicing_preserve_background.jpg', result_preserve_background)
# cv2.imwrite('intensity_slicing_non_preserve_background.jpg', result_non_preserve_background)

# # Wait for a key press and then close all windows
# cv2.waitKey(0)
# cv2.destroyAllWindows()










import numpy as np
import matplotlib.pyplot as plt

def slice_preserve_bg(img, low, high):
    result = np.zeros_like(img)
    rows, cols = img.shape

    for i in range(rows):
        for j in range(cols):
            if low <= img[i, j] <= high:
                result[i, j] = img[i, j]

    return result

def slice_no_preserve_bg(img, low, high):
    result = np.zeros_like(img)
    rows, cols = img.shape

    for i in range(rows):
        for j in range(cols):
            if not low <= img[i, j] <= high:
                result[i, j] = 255  # Set to white (255) outside the range

    return result

# Load the grayscale image
gray = plt.imread('grayscale1.jpeg')

# Define the lower and upper thresholds for intensity slicing
low_thresh = 100
high_thresh = 200

# Apply intensity slicing while preserving the background
result_preserve_bg = slice_preserve_bg(gray, low_thresh, high_thresh)

# Apply intensity slicing without preserving the background
result_no_preserve_bg = slice_no_preserve_bg(gray, low_thresh, high_thresh)

# Display the original image and the results
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.imshow(gray, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(result_preserve_bg, cmap='gray')
plt.title('Intensity Slicing (Preserve Background)')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(result_no_preserve_bg, cmap='gray')
plt.title('Intensity Slicing (Non-Preserve Background)')
plt.axis('off')

plt.show()

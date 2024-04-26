import cv2
import pywt
import numpy as np

def psnr(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if mse == 0:
        return 100
    max_pixel = 255.0
    psnr_value = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr_value

# Load the RGB image
original_image = cv2.imread('walchand.jpeg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Perform DWT transformation
coeffs = pywt.dwt2(gray_image, 'haar')

# Reconstruct the image using inverse DWT (IDWT)
reconstructed_image = pywt.idwt2(coeffs, 'haar')

# Convert the reconstructed image to uint8
reconstructed_image = np.uint8(reconstructed_image)

# Calculate PSNR between original and reconstructed images
psnr_value = psnr(gray_image, reconstructed_image)

# Display the original and reconstructed images
cv2.imshow('Original Image', gray_image)
cv2.imshow('Reconstructed Image', reconstructed_image)
print("PSNR Value:", psnr_value)

# Save the reconstructed image
cv2.imwrite('reconstructed_image.jpg', reconstructed_image)

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

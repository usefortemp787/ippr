import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to perform DCT transformation
def dct_transform(image):
    # Convert the image to float32 for DCT transformation
    image_float32 = np.float32(image)
    # Apply DCT transformation
    dct_image = cv2.dct(image_float32)
    return dct_image

# Function to perform inverse DCT transformation
def idct_transform(dct_image):
    # Apply inverse DCT transformation
    idct_image = cv2.idct(dct_image)
    # Convert back to uint8
    idct_image_uint8 = np.uint8(idct_image)
    return idct_image_uint8

# Function to calculate PSNR (Peak Signal to Noise Ratio)
def calculate_psnr(original_image, idct_image):
    mse = np.mean((original_image - idct_image) ** 2)
    max_pixel_value = 255.0
    psnr = 20 * np.log10(max_pixel_value / np.sqrt(mse))
    return psnr

# Load the original image
original_image = cv2.imread('original_image.jpg', cv2.IMREAD_GRAYSCALE)

# Perform DCT transformation
dct_image = dct_transform(original_image)

# Perform inverse DCT transformation
idct_image = idct_transform(dct_image)

# Calculate PSNR
psnr_value = calculate_psnr(original_image, idct_image)
print("PSNR value:", psnr_value)

# Display original and IDCT images using Matplotlib
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(idct_image, cmap='gray')
plt.title('IDCT Image')
plt.axis('off')

plt.show()

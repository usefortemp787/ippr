import cv2
import numpy as np

# Function to compress and decompress image using JPEG compression
def compress_decompress(image, compression_factor):
    # Encode image to JPEG format with specified compression factor
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), compression_factor]
    _, encoded_image = cv2.imencode('.jpg', image, encode_param)
    
    # Decode the encoded image back to original format
    decoded_image = cv2.imdecode(encoded_image, 1)
    
    return decoded_image

# Function to calculate PSNR (Peak Signal to Noise Ratio)
def calculate_psnr(original_image, decompressed_image):
    mse = np.mean((original_image - decompressed_image) ** 2)
    max_pixel_value = 255.0
    psnr = 20 * np.log10(max_pixel_value / np.sqrt(mse))
    return psnr

# Load the original image
original_image = cv2.imread('original_image.jpg')

# Compression factor (0 to 100, higher value means less compression)
compression_factor = 90

# Compress and decompress the image
decompressed_image = compress_decompress(original_image, compression_factor)

# Display original and decompressed images
cv2.imshow('Original Image', original_image)
cv2.imshow('Decompressed Image', decompressed_image)

# Calculate PSNR
psnr_value = calculate_psnr(original_image, decompressed_image)
print("PSNR value:", psnr_value)

cv2.waitKey(0)
cv2.destroyAllWindows()

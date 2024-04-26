# import cv2

# # Load the noisy image
# noisy_image = cv2.imread('logo.png')

# # Apply Gaussian blur for smoothing
# smooth_image = cv2.GaussianBlur(noisy_image, (5, 5), 0)

# # Display the original and smoothed images
# cv2.imshow('Noisy Image', noisy_image)
# cv2.imshow('Smoothed Image', smooth_image)

# # Wait for a key press to close the windows
# cv2.waitKey(0)

# # Close all OpenCV windows
# cv2.destroyAllWindows()




from PIL import Image, ImageFilter

# Load the noisy image
noisy_image = Image.open('logo.png').convert('RGB')

# Convert the image to RGB mode (if not already in RGB mode)
rgb_image = noisy_image.convert('RGB')

# Apply Gaussian blur for smoothing
smooth_image = rgb_image.filter(ImageFilter.GaussianBlur(radius=2))

# Display the smoothed image
noisy_image.show()
smooth_image.show()

# Save the smoothed image
smooth_image.save('smoothed_image.png')

# import cv2

# # Load the grayscale images
# image1 = cv2.imread('grayscale1.jpeg', cv2.IMREAD_GRAYSCALE)
# image2 = cv2.imread('grayscale2.jpeg', cv2.IMREAD_GRAYSCALE)

# # Resize images to have the same dimensions
# height = min(image1.shape[0], image2.shape[0])
# width = min(image1.shape[1], image2.shape[1])
# image1 = cv2.resize(image1, (width, height))
# image2 = cv2.resize(image2, (width, height))

# # Perform addition of two images
# addition_result = cv2.add(image1, image2)

# # Perform subtraction of two images
# subtraction_result = cv2.subtract(image1, image2)

# # Display the original images and the results
# cv2.imshow('Image 1', image1)
# cv2.imshow('Image 2', image2)
# cv2.imshow('Addition Result', addition_result)
# cv2.imshow('Subtraction Result', subtraction_result)

# # Save the results
# cv2.imwrite('addition_result.jpg', addition_result)
# cv2.imwrite('subtraction_result.jpg', subtraction_result)

# # Wait for a key press and then close all windows
# cv2.waitKey(0)
# cv2.destroyAllWindows()







from PIL import Image

# Load the grayscale images
image1 = Image.open('grayscale1.jpeg').convert('L')
image2 = Image.open('grayscale2.jpeg').convert('L')

# Resize images to have the same dimensions
width, height = min(image1.size[0], image2.size[0]), min(image1.size[1], image2.size[1])
image1 = image1.resize((width, height))
image2 = image2.resize((width, height))

# Create blank images for addition and subtraction results
addition_result = Image.new('L', (width, height))
subtraction_result = Image.new('L', (width, height))

# Perform addition and subtraction pixel by pixel
for x in range(width):
    for y in range(height):
        # Get pixel values from both images
        pixel1 = image1.getpixel((x, y))
        pixel2 = image2.getpixel((x, y))
        
        # Perform addition and subtraction
        addition_result.putpixel((x, y), min(pixel1 + pixel2, 255))
        subtraction_result.putpixel((x, y), max(pixel1 - pixel2, 0))

# Display the original images and the results
image1.show()
image2.show()
addition_result.show()
subtraction_result.show()

# Save the results
addition_result.save('addition_result.jpg')
subtraction_result.save('subtraction_result.jpg')

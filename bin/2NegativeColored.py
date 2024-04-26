import cv2
import numpy as np

def get_negative(input_image):
    # Calculate the negative image by subtracting each pixel value from 255
    negative_image = 255 - input_image
    return negative_image

def main():
    # Load the input image
    input_image = cv2.imread("image.jpeg")

    if input_image is None:
        print("Error: Could not read the image.")
        return

    # Split the image into its RGB channels
    b, g, r = cv2.split(input_image)

    # Get the negative of each channel
    negative_b = get_negative(b)
    negative_g = get_negative(g)
    negative_r = get_negative(r)

    # Merge the negative channels back into a single image
    negative_image = cv2.merge((negative_b, negative_g, negative_r))

    # Display the input and output images
    cv2.imshow("Input Image", input_image)
    cv2.imshow("Negative Image", negative_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

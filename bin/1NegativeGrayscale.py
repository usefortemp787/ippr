import cv2
import numpy as np

def get_negative(input_image):
    # Calculate the negative image by subtracting the input image from 255
    negative_image = 255 - input_image
    return negative_image

def main():
    # Load the input image in grayscale
    input_image = cv2.imread("image.jpeg", cv2.IMREAD_GRAYSCALE)

    if input_image is None:
        print("Error: Could not read the image.")
        return

    # Get the negative of the input image
    negative_image = get_negative(input_image)

    # Display the input and output images
    cv2.imshow("Input Image", input_image)
    cv2.imshow("Negative Image", negative_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

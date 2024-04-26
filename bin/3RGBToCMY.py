import cv2
import numpy as np

def rgb_to_cmy(rgb_image):
    # Split the image into its RGB channels
    r, g, b = cv2.split(rgb_image)

    # Calculate CMY values
    c = 255 - r
    m = 255 - g
    y = 255 - b

    # Merge CMY channels into a single image
    cmy_image = cv2.merge((c, m, y))

    return cmy_image

def main():
    # Load the input RGB image
    rgb_image = cv2.imread("image.jpeg")

    if rgb_image is None:
        print("Error: Could not read the image.")
        return

    # Convert RGB image to CMY
    cmy_image = rgb_to_cmy(rgb_image)

    # Display the input and CMY images
    cv2.imshow("Input RGB Image", rgb_image)
    cv2.imshow("CMY Image", cmy_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

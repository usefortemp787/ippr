import cv2
import numpy as np

def edge_detection_sobel(rgb_image):
    # Convert RGB image to grayscale
    gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)

    # Apply Sobel operator for edge detection
    sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

    # Combine the gradient images
    gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    gradient_magnitude *= 255.0 / gradient_magnitude.max()

    # Convert the gradient magnitude to uint8
    gradient_magnitude = np.uint8(gradient_magnitude)

    return gradient_magnitude

def main():
    # Load the input RGB image
    rgb_image = cv2.imread("image.jpeg")

    if rgb_image is None:
        print("Error: Could not read the image.")
        return

    # Perform edge detection using Sobel operator
    segmented_image = edge_detection_sobel(rgb_image)

    # Display the input and segmented images
    cv2.imshow("Input RGB Image", rgb_image)
    cv2.imshow("Segmented Image", segmented_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

import cv2
import numpy as np

def edge_detection_prewitt(rgb_image):
    # Convert RGB image to grayscale
    gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)

    # Define Prewitt kernels
    kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

    # Apply Prewitt kernels for horizontal and vertical edges
    prewitt_x = cv2.filter2D(gray_image, -1, kernel_x)
    prewitt_y = cv2.filter2D(gray_image, -1, kernel_y)

    # Combine the gradient images
    gradient_magnitude = np.sqrt(prewitt_x**2 + prewitt_y**2)
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

    # Perform edge detection using Prewitt operator
    segmented_image = edge_detection_prewitt(rgb_image)

    # Display the input and segmented images
    cv2.imshow("Input RGB Image", rgb_image)
    cv2.imshow("Segmented Image", segmented_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

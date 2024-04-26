import cv2

def edge_detection_canny(rgb_image):
    # Convert RGB image to grayscale
    gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray_image, threshold1=100, threshold2=200)

    return edges

def main():
    # Load the input RGB image
    rgb_image = cv2.imread("image.jpeg")

    if rgb_image is None:
        print("Error: Could not read the image.")
        return

    # Perform edge detection using Canny operator
    segmented_image = edge_detection_canny(rgb_image)

    # Display the input and segmented images
    cv2.imshow("Input RGB Image", rgb_image)
    cv2.imshow("Segmented Image", segmented_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_equalization_rgb(image):
    # Convert the RGB image to YUV color space
    yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

    # Equalize the Y channel (luminance)
    yuv_image[:,:,0] = cv2.equalizeHist(yuv_image[:,:,0])

    # Convert the equalized YUV image back to RGB color space
    equalized_image = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2BGR)

    return equalized_image

def plot_histogram(image, title):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Compute histogram
    hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

    # Plot histogram
    plt.figure()
    plt.title(title)
    plt.plot(hist, color='black')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.grid()
    plt.show()

def main():
    # Load the input RGB image
    rgb_image = cv2.imread("image.jpeg")

    if rgb_image is None:
        print("Error: Could not read the image.")
        return

    # Perform histogram equalization on the RGB image
    equalized_image = histogram_equalization_rgb(rgb_image)

    # Plot original and equalized histograms
    plot_histogram(rgb_image, "Original Image Histogram")
    plot_histogram(equalized_image, "Equalized Image Histogram")

    # Display the original and equalized images
    cv2.imshow("Original Image", rgb_image)
    cv2.imshow("Equalized Image", equalized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

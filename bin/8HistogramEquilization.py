import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_equalization(image):
    # Convert RGB image to YUV color space
    yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

    # Apply histogram equalization to Y channel
    yuv_image[:,:,0] = cv2.equalizeHist(yuv_image[:,:,0])

    # Convert back to RGB color space
    equalized_image = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2BGR)

    return equalized_image

def plot_histograms(image, equalized_image):
    # Convert images to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_equalized_image = cv2.cvtColor(equalized_image, cv2.COLOR_BGR2GRAY)

    # Compute histograms
    hist_orig = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    hist_eq = cv2.calcHist([gray_equalized_image], [0], None, [256], [0, 256])

    # Plot histograms
    plt.figure(figsize=(12, 6))

    # Plot original image and histogram
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.plot(hist_orig, color='black')
    plt.title("Original Image Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.grid()

    # Plot equalized image and histogram
    plt.subplot(2, 2, 3)
    plt.imshow(cv2.cvtColor(equalized_image, cv2.COLOR_BGR2RGB))
    plt.title("Equalized Image")
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.plot(hist_eq, color='black')
    plt.title("Equalized Image Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.grid()

    plt.tight_layout()
    plt.show()

def main():
    # Load the input RGB image
    rgb_image = cv2.imread("image.jpeg")

    if rgb_image is None:
        print("Error: Could not read the image.")
        return

    # Perform histogram equalization
    equalized_image = histogram_equalization(rgb_image)

    # Plot histograms
    plot_histograms(rgb_image, equalized_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

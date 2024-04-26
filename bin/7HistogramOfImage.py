import cv2
import numpy as np
import matplotlib.pyplot as plt

def compute_histogram(image):
    # Split the image into its RGB channels
    b, g, r = cv2.split(image)

    # Compute histograms for individual channels
    hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
    hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

    return hist_b, hist_g, hist_r

def plot_histograms(hist_b, hist_g, hist_r):
    plt.figure(figsize=(10, 5))
    plt.title("Histograms for Individual RGB Channels")
    plt.plot(hist_r, color='r', label='Red', alpha=0.7)
    plt.plot(hist_g, color='g', label='Green', alpha=0.7)
    plt.plot(hist_b, color='b', label='Blue', alpha=0.7)
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid()
    plt.show()

def main():
    # Load the input RGB image
    rgb_image = cv2.imread("image.jpeg")

    if rgb_image is None:
        print("Error: Could not read the image.")
        return

    # Compute histograms for individual RGB channels
    hist_b, hist_g, hist_r = compute_histogram(rgb_image)

    # Plot histograms
    plot_histograms(hist_b, hist_g, hist_r)

if __name__ == "__main__":
    main()

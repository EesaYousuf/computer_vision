# 
import cv2
import numpy as np

def lbp_calculate(image, radius=1, points=8):
    lbp_image = np.zeros_like(image, dtype=np.uint8)
    for i in range(radius, image.shape[0] - radius):
        for j in range(radius, image.shape[1] - radius):
            center = image[i, j]
            binary_string = ''
            for point in range(points):
                angle = 2 * np.pi * point / points
                y = i + int(round(radius * np.sin(angle)))
                x = j + int(round(radius * np.cos(angle)))
                neighbor = image[y, x]
                binary_string += '1' if neighbor >= center else '0'
            lbp_image[i, j] = int(binary_string, 2)
    return lbp_image

# Example usage
image = cv2.imread('your_image.jpg', cv2.IMREAD_GRAYSCALE)
if image is None:
    raise ValueError("Image not found. Check the path.")

lbp_image = lbp_calculate(image)
cv2.imshow('LBP', lbp_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

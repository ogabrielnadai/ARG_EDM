import cv2
import numpy as np


image = cv2.imread('code.png', cv2.IMREAD_GRAYSCALE)
height, width = image.shape

for y in range(height):
    for x in range(width):
        if(image[y][x] > 150):
            image[y, :] = 255

# Save or display the modified image
cv2.imwrite('output_image.png', image)
cv2.imshow('Modified Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
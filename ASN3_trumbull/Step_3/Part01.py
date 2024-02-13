import cv2
import numpy as np

# Reading our image in color
img = cv2.imread("ASN3_trumbull/Media/Frame0064.png", 1)

# Extracting the red, green, and blue channels
blue, green, red = cv2.split(img)

zeros = np.zeros(blue.shape, np.uint8)

blueBGR = cv2.merge((blue, zeros, zeros))
greenBGR = cv2.merge((zeros, green, zeros))
redBGR = cv2.merge((zeros, zeros, red))

# Displaying all of our images!
cv2.imshow('Normal', img)
cv2.imshow('blue BGR', blueBGR)
cv2.imshow('green BGR', greenBGR)
cv2.imshow('red BGR', redBGR)

cv2.imwrite("ASN3_trumbull/Outputs/BlueChannel.png", blueBGR)
cv2.imwrite("ASN3_trumbull/Outputs/RedChannel.png", redBGR)
cv2.imwrite("ASN3_trumbull/Outputs/GreenChannel.png", greenBGR)

cv2.waitKey(0)
cv2.destroyAllWindows()

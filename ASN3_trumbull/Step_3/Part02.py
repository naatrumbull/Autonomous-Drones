import cv2

# Reading a color image
rgb = cv2.imread("ASN3_trumbull/Media/Frame0064.png", 1)

# Converting rgb images is hsv
hsv = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)

cv2.imshow("HSV", hsv)
cv2.imshow("RGB", rgb)
cv2.imwrite("ASN3_trumbull/Outputs/HSVImage.png", hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

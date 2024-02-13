import cv2

# Reading an image:
Frame0064 = cv2.imread("ASN3_trumbull/Media/Frame0064.png", 1)
Label0064 = cv2.imread("ASN3_trumbull/Media/Label0064.png", 1)
print("Matrix that represents Frame0064:\n" + str(Frame0064))
print("\nMatrix that represents Label0064:\n" + str(Label0064))

# Displaying an image:
cv2.imshow("Frame0064", Frame0064)
cv2.imshow("Label0064", Label0064)
# Passing 0 into waitKey() will keep window open until closed
cv2.waitKey(0)
cv2.destroyAllWindows()

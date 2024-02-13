import numpy as np
import cv2

# Extracts first frame from video input. Two version are saved
# to the Outputs folder. One is in color, while the other is in
# grayscale.

cap = cv2.VideoCapture('ASN4_trumbull/Data/Vid.mp4')

i = 1
while (i == 1):
    ret, frame = cap.read()

    if ret == False:
        break
    cv2.imwrite('ASN4_trumbull/Outputs/FrameOneUncropped.png', frame)

    i = 2

cv2.imwrite('ASN4_trumbull/Outputs/FrameOneUncroppedGrayScale.png',
            cv2.imread('ASN4_trumbull/Outputs/FrameOneUncropped.png', 0))

cv2.waitKey(0)
cv2.destroyAllWindows()

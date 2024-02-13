import numpy as np
import cv2

Ig = cv2.imread("ASN3_trumbull/Media/Frame0064.png", 0)
Ky = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
Gy = cv2.filter2D(Ig, -1, Ky)

Kx = np.transpose(Ky)
Gx = cv2.filter2D(Ig, -1, Kx)

G = (Gx ** 2 + Gy ** 2) ** 0.5

cv2.imshow("GrayScale", Ig)
cv2.imshow("Gy", Gy)
cv2.imshow("Gx", Gx)
cv2.imshow("G", G)

cv2.imwrite("ASN3_trumbull/Outputs/X-Gradient.png", Gx)
cv2.imwrite("ASN3_trumbull/Outputs/Y-Gradient.png", Gy)
cv2.imwrite("ASN3_trumbull/Outputs/GrayScaleImage.png", Ig)

cv2.waitKey(0)
cv2.destroyAllWindows()

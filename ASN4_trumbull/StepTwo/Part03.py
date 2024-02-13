import cv2 as cv
import numpy as np

# Creating a barrel detector for one single frame. Uses data
# created in Parts in 1 and 2. This is a stepstone for creating 
# the whole video. 

img_rgb = cv.imread("ASN4_trumbull/Outputs/FrameOneUncropped.png", 1)
img_gray = cv.imread("ASN4_trumbull/Outputs/FrameOneUncropped.png", 0)
template = cv.imread("ASN4_trumbull/Outputs/CroppedCone.png", 0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
           'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

img = img_gray.copy()
method = eval(methods[1])
# Apply template Matching
res = cv.matchTemplate(img, template, method)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv.rectangle(img_rgb, top_left, bottom_right, 255, 2)

cv.imwrite("ASN4_trumbull/Outputs/InitialFrame.png", img_rgb)

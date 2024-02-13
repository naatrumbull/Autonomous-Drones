import cv2 as cv
import numpy as np

# Takes an input video and a mask and outputs a video
# with a rectangle outlining the detected image in the video.

cap_rgb = cv.VideoCapture('ASN4_trumbull/Data/Vid.mp4')

template = cv.imread("ASN4_trumbull/Outputs/CroppedCone.png", 0)
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
           'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
w, h = template.shape[::-1]

width = int(cap_rgb.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap_rgb.get(cv.CAP_PROP_FRAME_HEIGHT))

result = cv.VideoWriter("ASN4_trumbull/Outputs/Output.mp4",
                        cv.VideoWriter_fourcc(*"MPG4"),
                        30.0, (width, height))

while (cap_rgb.isOpened()):
    ret, frame = cap_rgb.read()

    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    method = eval(methods[5])

    res = cv.matchTemplate(frame_gray, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(frame, top_left, bottom_right, 255, 2)

    if ret == True:
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

    result.write(frame)

cap_rgb.release()
result.release()
cv.destroyAllWindows()

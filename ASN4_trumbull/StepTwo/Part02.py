import numpy as np
import cv2

# Building off of part 1, this code converts a whole
# video to GrayScale instead of just one frame.

cap = cv2.VideoCapture('ASN4_trumbull/Data/Vid.mp4')

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

result = cv2.VideoWriter("ASN4_trumbull/Outputs/VidGrayScale.mp4",
                         cv2.VideoWriter_fourcc(*"MPG4"),
                         30.0, (width, height))

while (cap.isOpened()):
    ret, frame = cap.read()

    grayScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result.write(grayScale)

    if ret == True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
result.release()
cv2.destroyAllWindows()

import numpy as np
import cv2


cap = cv2.VideoCapture('ASN3_trumbull/Media/Vid.mp4')
lower = np.array((0, 80, 120))
upper = np.array((100, 200, 250))

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

result = cv2.VideoWriter("ASN3_trumbull/Outputs/test.mp4",
                         cv2.VideoWriter_fourcc(*"MPG4"),
                         25.0, (width, height))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:

        retval, th3 = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY, 11, 2)
        newFrame = np.array(th3)
        result.write(th3)
        cv2.imshow('newFrame', newFrame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
result.release()
cv2.destroyAllWindows()

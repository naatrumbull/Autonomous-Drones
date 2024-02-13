
import numpy as np
import cv2

cap = cv2.VideoCapture('ASN3_trumbull/Media/Vid.mp4')

orangeMean = np.array([255, 145, 0])
orangeMeanWithZeros = np.array([[255], [145], [0]])
print(orangeMean)

covarianceMatrix = np.array([[6025, 36975, 5], [36975, 21025, 4], [3, 2, 1]])

print(np.linalg.inv(covarianceMatrix))


def normal(pixel, mean, covariance):
    difference = pixel - mean
    transposeMatrix = np.transpose(difference)
    inverse = np.linalg.inv(covariance)
    productOne = np.multiply(transposeMatrix, inverse)
    productTwo = np.multiply(productOne, difference)
    productThree = productTwo * 0.5
    euler = np.exp(productThree)
    determine = np.linalg.det(covariance)
    productFour = np.pi * 2 * determine
    absoluteValue = np.abs(productFour)
    root = np.sqrt(absoluteValue)
    return np.sum(euler / root)


print(normal([255, 145, 1], orangeMeanWithZeros, covarianceMatrix))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:

        retval, threshold = cv2.threshold(frame, 0, 255, cv2.THRESH_BINARY)
        newFrame = np.array(frame)

        cv2.imshow('newFrame', newFrame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()

import numpy as np
import sys
import cv2 as cv

cap = cv.VideoCapture(0)
print("pegou")
while(True):
	ret, frame = cap.read()
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	cv.imshow('frame',gray)
	if cv.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv.destroyAllWindows()

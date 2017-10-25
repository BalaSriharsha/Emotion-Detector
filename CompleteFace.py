import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('haarcascade_mouth.xml')

if mouth_cascade.empty():
  raise IOError('Unable to load the mouth cascade classifier xml file')

cap = cv2.VideoCapture(0)
ds_factor = 0.5

while True:
	ret, img = cap.read()
    	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    	faces = face_cascade.detectMultiScale(gray, 1.3, 5)


	for (x,y,w,h) in faces:
        	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        	roi_gray = gray[y:y+h, x:x+w]
        	roi_color = img[y:y+h, x:x+w]

		eyes = eye_cascade.detectMultiScale(roi_gray)
        	for (ex,ey,ew,eh) in eyes:
            		cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	mouth_rects = mouth_cascade.detectMultiScale(gray, 1.7, 11)
    	for (x,y,w,h) in mouth_rects:
        	y = int(y - 0.15*h)
        	cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)
        	break

	cv2.imshow('img',img)
	cv2.imwrite('image.jpeg',img)
    	k = cv2.waitKey(30) & 0xff
    	if k == 27:
        	break

cap.release()
cv2.destroyAllWindows()	

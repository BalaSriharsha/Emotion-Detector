import cv2
import PIL from Image
import cv

def mouth(mouth_image):
	mouth = cv.Load('haarcascade_mouth.xml')
	face = cv.Load('haarascade_frontalface_default.xml')
	store_image = cv.CreateMemStorage()
	after_mouth_detection = cv.HaarDetectObjects(mouth_image,mouth,store_image)
	after_face_detection = cv.HaarDetectObjects(mouth_image,face,store_image)

	size_of_maximum_face = 0
	maximum_face = 0

	if after_face_detection:
		for face in after_face_detection:
			if face[0][3]*face[0][2] > size_of_maximmum_face:
				size_of_maximum_face = face[0][2] * face[0][2]
				maximum_face = face
	if maximum_face ==0:
		return 2

	def bottom_face(mouth,face):
		if ( mouth[0][1] > face[0][1] + face[0][3] * 3 / float(5) and mouth[0][1] + mouth[0][3] < face[0][1] + face[0][3]
      and abs((mouth[0][0] + mouth[0][2] / float(2))) < face[0][2] / float(10)):
			return True
		else:
			return False

	mouth_after_filtering = 0
	for mouth in filteredMouth:
		if mouth[0][3]* mouth[0][2] > size_of_maximum_mouth:
			size_of_maximum_mouth

cap.release()
cv2.destroyAllWindows()

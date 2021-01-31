# We import the necessary packages
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2

# We construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required = True,
	help ="path to facial landmark predictor")
ap.add_argument("-i", "--image", required = True,
	help ="path to input image")
args = vars(ap.parse_args())

# We are initializing the dlib's face detector (HOG-based) and then
# creation of the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

# We then load the input image, resize it, and convert it to grayscale
images = cv2.imread(args["image"])
images = imutils.resize(images, width = 500)
gray = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)

# We then detect faces in the grayscale image
rects = detector(gray, 1)

# Now, job is to loop over the face detections
for (i, rect) in enumerate(rects):
	# We will determine the facial landmarks for the face region, then
	# can convert the facial landmark (x, y)-coordinates to a NumPy array
	shape = predictor(gray, rect)
	shape = face_utils.shape_to_np(shape)

	# We then convert dlib's rectangle to a OpenCV-style bounding box
	# [i.e., (x, y, w, h)], then can draw the face bounding box
	(x, y, w, h) = face_utils.rect_to_bb(rect)
	cv2.rectangle(images, (x, y), (x + w, y + h), (255, 255, 0), 2)

	# We then show the face number
	cv2.putText(images, 'Face % {}'.format(i + 1), (x - 10, y - 10),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

	# We then loop over the (x, y)-coordinates for the facial landmarks
	# and draw them on the image
	for (x, y) in shape:
		cv2.circle(images, (x, y), 1, (0, 0, 255), -1)

# Now show the output image with the face detections as well as
# facial landmarks
cv2.imshow("Output", images)
cv2.waitKey(0)

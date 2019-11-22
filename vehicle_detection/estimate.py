from imutils import paths
import numpy as np
import imutils
import cv2

# initialize the known distance from the camera to the object, which
# in this case is 24 inches
KNOWN_DISTANCE = 180

# initialize the known object width, which in this case, the piece of
# paper is 12 inches wide
KNOWN_WIDTH = 50

# load the first image that contains an object that is KNOWN TO BE 2 feet
# from our camera, then find the paper marker in the image, and initialize
# the focal length
image = cv2.imread("test_images/test_3.jpg")
focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH


def distance_to_camera(knownWidth, focalLength, perWidth):
	# compute and return the distance from the maker to the camera
	return (knownWidth * focalLength) / perWidth
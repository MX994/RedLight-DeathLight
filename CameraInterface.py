import cv2
import numpy as np

class CameraInterface:
	def __init__(self):
		self.capture = cv2.VideoCapture(0)
		self.filter = cv2.createBackgroundSubtractorMOG2(100, 100, True)
		self.foundMovement = False

	def trackingMovement(self):
		ret, frame = self.capture.read()
		if not ret:
			return
		resizedFrame = cv2.resize(frame, (0, 0), fx=1, fy=1)
		fgmask = self.filter.apply(resizedFrame)
		if np.count_nonzero(fgmask) > 5000:
			self.foundMovement = True
		else:
			self.foundMovement = False

	def getFoundMovement(self):
		return self.foundMovement

	def resetFoundMovement(self):
		foundMovement = False

	def disableCamera(self):
		self.capture.release()
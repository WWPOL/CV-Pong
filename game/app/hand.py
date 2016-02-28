import cv2
import numpy as np

class HandJob:
	def __init__(self):
		self.cap = cv2.VideoCapture(0)
		self.samples = []

		self.oldPosition = [0,0]

		self.frame_hsv = 0 # just declare for now

		cv2.namedWindow("Frame")
		cv2.setMouseCallback("Frame", self.getSample)
	
	def getSample(self, event, x, y, flags, param):
		if event == cv2.EVENT_LBUTTONDOWN:
			print "%d %d" % (x,y)
			#print self.frame_hsv[y,x]
			print "click"
			self.samples.append(self.frame_hsv[y,x])

	def createMultipleThresholds(self, img):
		#img = cv2.GaussianBlur(img, (7,7), 3)
		combined_mask = np.zeros((img.shape[0], img.shape[1]), np.uint8) # start off with 2D array of zeros
		# range for HSV threshold:
		range_hsv = np.array([1,50,50]) # give little flexibility in hue but more in sat & val (b/c lighting) -Philip

		for sample in self.samples:
			# iterate over each HSV numpy array
			mask = cv2.inRange(img, sample - range_hsv, sample + range_hsv)
			combined_mask = combined_mask + mask

		# combined_mask = cv2.erode(combined_mask, kernel, iterations=2)
		# combined_mask = cv2.dilate(combined_mask, kernel, iterations=4)
		combined_mask = cv2.medianBlur(combined_mask, 11)
		return combined_mask

	def getLargestContour(self, img):
		contours, hierarchy = cv2.findContours(img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		# contourSizes = []
		# for i, contour in enumerate(contours):
		# 	size = cv2.contourArea(contour)
		# 	contourSizes.append((i, size))
		if len(contours) != 0:
			largestContour = (contours[0], 0) # loop thru and find the largest contour & size
			for contour in contours: 
				size = cv2.contourArea(contour)
				if size > largestContour[1]:
					largestContour = (contour, size) 

			#print largestContour
			return largestContour[0]
		else:
			return 0

	def getContourMoment(self, contour):
		m = cv2.moments(contour)
		cx = int(m['m10']/(m['m00']+0.01)) # add 0.01 to prevent division by 0 errors
		cy = int(m['m01']/(m['m00']+0.01))
		return [cx, cy]

	def captureImage(self):
		position = [0, 0]
		velocity = [0, 0]

		frame = self.cap.read()[1]

		if frame != None:
			frame = cv2.flip(frame, 1)

			self.frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

			threshold_mask = self.createMultipleThresholds(self.frame_hsv)


			contour = self.getLargestContour(threshold_mask)
			if type(contour) != int:
				cv2.drawContours(frame, contour, -1, (0, 255, 255), 2)
				position = self.getContourMoment(contour)
				cv2.circle(frame, (position[0], position[1]), 5, (0,0,255), -1)

			# calculate velocity
			velocity = [position[0] - self.oldPosition[0], position[1] - self.oldPosition[1]]
			# print velocity

			cv2.imshow("Frame", frame)
			cv2.waitKey(10)

		self.oldPosition = position
		return [position, velocity]



# cam = HandJob()

# while True:
# 	cam.captureImage()
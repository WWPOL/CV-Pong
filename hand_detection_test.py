import cv2
import numpy as np

def createMultipleThresholds(img):
	#img = cv2.GaussianBlur(img, (7,7), 3)
	combined_mask = np.zeros((img.shape[0], img.shape[1]), np.uint8) # start off with 2D array of zeros
	# range for HSV threshold:
	range_hsv = np.array([1,50,50]) # give little flexibility in hue but more in sat & val (b/c lighting) -Philip

	for sample in samples:
		# iterate over each HSV numpy array
		mask = cv2.inRange(img, sample - range_hsv, sample + range_hsv)
		combined_mask = combined_mask + mask

	# combined_mask = cv2.erode(combined_mask, kernel, iterations=2)
	# combined_mask = cv2.dilate(combined_mask, kernel, iterations=4)
	combined_mask = cv2.medianBlur(combined_mask, 11)
	return combined_mask

def getLargestContour(img):
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

def getContourMoment(contour):
	m = cv2.moments(contour)
	cx = int(m['m10']/m['m00'])
	cy = int(m['m01']/m['m00'])
	return [cx, cy]



def getSample(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		# print "%d %d" % (x,y)
		print frame_hsv[y,x]
		samples.append(frame_hsv[y,x])

def captureImage(old):
	frame = cap.read()[1]
	frame = cv2.flip(frame, 1)
	
	global frame_hsv
	frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	# frame = cv2.GaussianBlur(frame, (7,7), 3)

	threshold_mask = createMultipleThresholds(frame_hsv)


	position = [0, 0]
	velocity = [0, 0]

	contour = getLargestContour(threshold_mask)
	if type(contour) != int:
		cv2.drawContours(frame, contour, -1, (0, 255, 255), 2)
		position = getContourMoment(contour)
		cv2.circle(frame, (position[0], position[1]), 5, (0,0,255), -1)
	
	# calculate velocity
	oldPosition = old[0]
	velocity = [position[0] - oldPosition[0], position[1] - oldPosition[1]]
	print velocity
	# draw frames (remove if necessary)

	cv2.imshow("Frame", frame) 
	cv2.imshow("Combined Mask", threshold_mask)
	cv2.waitKey(20) # ADJUST THIS DEPENDING ON FRAME DRAW RATE

	# # scale position, velocity from 640 x 480 to 1280 x 720
	# position[0] *= 2
	# velocity[0] *= 2

	# position[1] = int(position[1] * 1.5)
	# velocity[1] = int(velocity[1] * 1.5)

	# print [position, velocity]

	return [position, velocity]


cap = cv2.VideoCapture(0)
# frame size: 640 x 480

samples = []

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", getSample)

previousValues = [[0,0],[0,0]]

while True: 
	# print previousValues[0]
	previousValues = captureImage(previousValues)	
	# print previousValues[0]

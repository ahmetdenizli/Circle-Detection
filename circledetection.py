# import the necessary packages
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

cap.set(3,1280)
# default Resolution 640x480.
while(True):
	ret, frame = cap.read()
			
	output = frame.copy()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# GuassianBlur to reduce noise
	gray_blurred  = cv2.GaussianBlur(gray, (5,5), 0);
	gray_blurred  = cv2.medianBlur(gray_blurred ,5)
	
	gray = cv2.adaptiveThreshold(gray_blurred ,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,3.5)
	
	kernel = np.ones((5,5), np.uint8)
	gray = cv2.erode(gray, kernel, iterations = 1)
	
	gray = cv2.dilate(gray, kernel, iterations = 1)
	
	# HoughCircles
	detected_circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 200, param1=30, param2=45, minRadius=0, maxRadius=150)

	if detected_circles is not None:
		# Convert the circle parameters a, b and r to integers.
		detected_circles = np.uint16(np.around(detected_circles[0, :]))

		for (x, y, r) in detected_circles:
			# Draw the circumference of the circle.
			cv2.circle(output, (x, y), r, (0, 255, 0), 4)
			# Draw a small circle to show the center.
			cv2.circle(output, (x, y), 1, (0, 0, 255), 3)
			print ("Col: ", x, ", Row: ", y, ", Radius: ", r)

			if x <360:
				print("--------------------------\n\n\n\n")
				print("sol\n\n\n\n")
				print("--------------------------\n\n\n\n")
			elif x>720:
				print("--------------------------\n\n\n\n")
				print("sağ\n\n\n\n")
				print("--------------------------\n\n\n\n")
			else:
				print("--------------------------\n\n\n\n")
				print("düz\n\n\n\n")
				print("--------------------------\n\n\n\n")

	# Display the resulting frame
	#cv2.imshow('gray',gray)
	cv2.imshow('frame',output)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# release the capture
cap.release()
cv2.destroyAllWindows()

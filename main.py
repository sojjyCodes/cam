# import the opencv library 
import cv2


vid = cv2.VideoCapture(0) 

while(True): 
	
	# Capture the video frame 
	ret, frame = vid.read() 

	# Display the resulting frame 
	cv2.imshow('frame', frame) 
	
	# the 'q' button is to quit
	if cv2.waitKey(1) & 0xFF == ord('q'): 
		break

# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 

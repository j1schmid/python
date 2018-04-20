import numpy as np
import cv2

rows = 640
cols = 480
cap = cv2.VideoCapture(0) #use external cam
ret = cap.set(3,rows)
ret = cap.set(4,cols)

background = cv2.imread('background_640x480.jpg')

thresh = 230
blur = 3
final = ""
display=1
kernel = np.ones((5,5),np.uint8)

# create window
cv2.namedWindow("chroma", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("chroma", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	frame = cv2.flip(frame,1,frame)

	lab_image = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
	l_channel,chan_a,chan_b = cv2.split(lab_image)

	b_channel = cv2.bitwise_not(chan_b)
	a_channel = cv2.add(chan_a,b_channel)
	a_channel = cv2.bitwise_not(a_channel)
	a_channel_inv = cv2.bitwise_not(a_channel)


	# create mask

	im_bw = cv2.threshold(a_channel_inv, thresh, 255, cv2.THRESH_BINARY)[1]
	im_bw = cv2.GaussianBlur(im_bw,(blur,blur),0)


	im_bw = cv2.morphologyEx(im_bw, cv2.MORPH_OPEN, kernel)
	ret ,im_bw = cv2.threshold(im_bw,thresh,255,cv2.THRESH_BINARY)

	im_bw_inv = cv2.bitwise_not(im_bw)
	im_bw_inv = cv2.GaussianBlur(im_bw_inv,(1,1),0)
	im_bw_inv = cv2.morphologyEx(im_bw_inv, cv2.MORPH_CLOSE, kernel)

	roi = cv2.bitwise_and(background,background,mask = im_bw_inv)
	im = cv2.bitwise_and(frame,frame,mask = im_bw)

	# add mask
	dst = cv2.add(roi,im)

	# Display the resulting frame

	k = cv2.waitKey(33)
	if k == 27: #ESC
		break
	if k == ord("+"):
		thresh+=1
	if k == ord("-"):
		thresh-=1

	if k == ord("."):
		blur*=3
	if k == ord(","):
		if blur > 1:
			blur/=3

	if k == ord("1"):
		display = 1
	if k == ord("2"):
		display = 2
	if k == ord("3"):
		display = 3
	if k == ord("4"):
		display = 4
	if k == ord("5"):
		display = 5
	if k == ord("6"):
		display = 6
	if k == ord("7"):
		display = 7
	if k == ord("8"):
		display = 8
	
	if (display == 1):
		final = dst
		text = 'final image'
	if (display == 2):
		final = im
		text = 'masked foreground'
	if (display == 3):
		final = roi
		text = 'masked background'
	if (display == 4):
		final = im_bw
		text = 'foreground mask'
	if (display == 5):
		final = im_bw_inv
		text = 'background mask'
	if (display == 6):
		final = chan_a
		text = 'channel a'
	if (display == 7):
		final = chan_b
		text = 'channel b'
	if (display == 8):
		final = l_channel
		text = 'l channel'

	#display image
	
	a3 = np.array( [[[10,10],[200,10],[200,100],[10,100]]], dtype=np.int32)
	#np.array([[0,0], [0,100], [100,100], [100,0]])
	cv2.fillPoly(final, a3, (255,255,255))
	#cv2.rectangle(final ,(0,0), (100,100), (255,255,255))
	cv2.putText(final, "Thresh (+/-): " + str(thresh), (20,40), cv2.FONT_HERSHEY_SIMPLEX,0.5, 0)
	cv2.putText(final, "Blur (./,): " + str(blur), (20,60), cv2.FONT_HERSHEY_SIMPLEX,0.5, 0)
	cv2.putText(final, text, (20,80), cv2.FONT_HERSHEY_SIMPLEX,0.5, 0)
	cv2.imshow('chroma', final)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows() 

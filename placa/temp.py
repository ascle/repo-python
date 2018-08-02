import cv2
import numpy as np

def draw_lines(hough, image, nlines):
	n_x, n_y=image.shape
   	#convert to color image so that you can see the lines
	draw_im = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

	for (rho, theta) in hough[0][:nlines]:
		try:
			x0 = np.cos(theta)*rho
			y0 = np.sin(theta)*rho
			pt1 = ( int(x0 + (n_x+n_y)*(-np.sin(theta))), int(y0 + (n_x+n_y)*np.cos(theta)) )
			pt2 = ( int(x0 - (n_x+n_y)*(-np.sin(theta))),  int(y0 - (n_x+n_y)*np.cos(theta)) )
			alph = np.arctan( (pt2[1]-pt1[1])/( pt2[0]-pt1[0]) )
			alphdeg = alph*180/np.pi
         	#OpenCv uses weird angle system, see: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html
			if abs( np.cos( alph - 180 )) > 0.8: #0.995:
				cv2.line(draw_im, pt1, pt2, (255,0,0), 2)
			if rho>0 and abs( np.cos( alphdeg - 90)) > 0.7:
				cv2.line(draw_im, pt1, pt2, (0,0,255), 2)    
		except:
			pass

	cv2.imwrite("3HoughLines.png", draw_im, [cv2.IMWRITE_PNG_COMPRESSION, 12])   

img = cv2.imread('exCars/image_0040.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

flag,b = cv2.threshold(gray,160,255,cv2.THRESH_BINARY)
cv2.imwrite("1tresh.jpg", b)

element = np.ones((3,3))
b = cv2.erode(b,element)
cv2.imwrite("2erodedtresh.jpg", b)

edges = cv2.Canny(b,10,100,apertureSize = 3)
cv2.imwrite("3Canny.jpg", edges)

hough = cv2.HoughLines(edges, 1, np.pi/180, 200)   
draw_lines(hough, b, 100)
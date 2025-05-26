'''

Welcome to SmartUmpires!!!!
You are currently viewing the HEART of smartumps, this is the strikezone, ball tracking, and camera feed.
A few things to know, contour means the outline or border of the shape in an image and ret means return

Some code provided Copilot, and some info from OpenCv python docs






'''

import cv2  # lets us use the camera
import numpy as np  # helps with math stuff

cap = cv2.VideoCapture(0)  # start the webcam

# get the camera's width and height
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# make a rectangle for the strike zone in the middle
zone_w, zone_h = 400, 200
zone_x1 = (frame_width - zone_w) // 2
zone_y1 = (frame_height - zone_h) // 2
zone_x2 = zone_x1 + zone_w
zone_y2 = zone_y1 + zone_h

while True:
    ret, frame = cap.read()
    if not ret: # Ret means return BTW
        break  # if no camera image, stop

    # draw the green strike zone
    cv2.rectangle(frame, (zone_x1, zone_y1), (zone_x2, zone_y2), (0, 255, 0), 3)

    # turn picture into HSV so color is easy to find
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # set what counts as "white"
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 40, 255])
    mask = cv2.inRange(hsv, lower_white, upper_white)
    # find shapes in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #RETER_EXTERNAL will only give you the border of a shape if their is a shape inside of a shape, and CHAIN_APPPROX_SIMPLE will remove all external points that don't help you see the shape

    # if we see something white, draw a circle on it
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_contour)
        if area > 300:
            (x, y), radius = cv2.minEnclosingCircle(largest_contour)
            center = (int(x), int(y))
            radius = int(radius)
            cv2.circle(frame, center, radius, (0, 255, 0), 2)

    # show the video window
    cv2.imshow("Strike Zone Baseball Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): # keycode for q  to exit program (& OXFF) make sure we only look at the key part
        break  # press q to quit

cap.release()
cv2.destroyAllWindows()

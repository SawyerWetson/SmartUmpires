'''
Welcome to SmartUmpires!!!!
You are currently viewing the HEART of smartumps, this is the strikezone, ball tracking, and camera feed.
A few things to know, contour means the outline or border of the shape in an image and ret means return

Some code provided Copilot, and some info from OpenCv python docs
'''

import cv2  # lets us use the camera
import numpy as np  # helps with math stuff
import os # helps with the voice detection 

cap = cv2.VideoCapture(0)  # start the webcam

# get the camera's width and height
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# make a rectangle for the strike zone in the middle
zone_w, zone_h = 300,200
zone_x1 = (frame_width - zone_w) // 2
zone_y1 = (frame_height - zone_h) // 2
zone_x2 = zone_x1 + zone_w
zone_y2 = zone_y1 + zone_h

# get the center of the strike zone
zone_center = ((zone_x1 + zone_x2) // 2, (zone_y1 + zone_y2) // 2)

# Make the OpenCV window take up the full screen
cv2.namedWindow("Strike Zone Baseball Tracking", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Strike Zone Baseball Tracking", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# ---- Baseball area detection settings ----
MIN_BASEBALL_AREA = 1000
MAX_BASEBALL_AREA = 3000

while True:
    ret, frame = cap.read()
    if not ret: # Ret means return BTW
        break  # if no camera image, stop

    # check if strikezone should be shown (voice controlled)
    # For debugging, always show the strikezone if the file doesn't exist
    if os.path.exists("strikezone_state.txt"):
        with open("strikezone_state.txt") as f:
            strikezone_on = f.read().strip().lower() == "on"
    else:
        strikezone_on = True  # Default to True for debugging

    if strikezone_on:
        # Draw the strike zone rectangle
        cv2.rectangle(frame, (zone_x1, zone_y1), (zone_x2, zone_y2), (0, 255, 0), 3)
        # Show the center of the strikezone as a blue dot (for reference)
        cv2.circle(frame, zone_center, 3, (255, 0, 0), -1)

    # turn picture into HSV so color is easy to find
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # set what counts as "white" (tighter range to avoid tracking large objects like hands)
    lower_white = np.array([0, 0, 220])
    upper_white = np.array([180, 30, 255])
    mask = cv2.inRange(hsv, lower_white, upper_white)
    # find shapes in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # ---- Area-based detection for green circle and "no baseball detected" ----
    baseball_found = False
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # Uncomment the next line to see the area for calibration:
        # print("Contour area:", area)
        if MIN_BASEBALL_AREA < area < MAX_BASEBALL_AREA:
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            center = (int(x), int(y))
            radius = int(radius)
            cv2.circle(frame, center, radius, (0, 255, 0), 2)  # Green outline for the ball
            cv2.circle(frame, center, 3, (0, 0, 255), -1)      # Red dot at the ball's center
            # say if the ball is in the strikezone
            if zone_x1 < center[0] < zone_x2 and zone_y1 < center[1] < zone_y2:
                cv2.putText(frame, "IN STRIKE ZONE", (zone_x1, zone_y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
            baseball_found = True

    if not baseball_found:
        cv2.putText(frame, "No baseball detected", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # show the video window
    cv2.imshow("Strike Zone Baseball Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): # keycode for q  to exit program (& 0xFF) make sure we only look at the key part
        break  # press q to quit

cap.release()
cv2.destroyAllWindows()

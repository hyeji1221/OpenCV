# -----------------------------
#   USAGE
# -----------------------------
# python detect_low_contrast_video.py --input example_video.mp4

# -----------------------------
#   IMPORTS
# -----------------------------
# Import the necessary packages
from skimage.exposure import is_low_contrast
import numpy as np
import argparse
import imutils
import cv2

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, default="", help="Optional path to video file")
ap.add_argument("-t", "--thresh", type=float, default=0.35, help="threshold for low contrast")
args = vars(ap.parse_args())

# Grab a pointer to the input video stream
print("[INFO] Accessing video stream...")
vs = cv2.VideoCapture(args["input"] if args["input"] else 0)

# Loop over the frames from the video stream
while True:
    # Read a frame from the video stream
    (grabbed, frame) = vs.read()
    # If no frame has been grabbed, then the end of the video stream has been reached and so the end of the script
    if not grabbed:
        print("[INFO] No frame read from stream! Exiting...")
        break
    # Resize the frame, convert it to grayscale, blur it and then perform edge detection
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 30, 150)
    # Initialize the text and color to indicate that the current frame is *not* low contrast
    text = "Low contrast: No"
    color = (0, 255, 0)
    # Check to see if the frame is low contrast, and if so, update the text and color
    if is_low_contrast(gray, fraction_threshold=args["thresh"]):
        # Update the text and color
        text = "Low contrast: Yes"
        color = (0, 0, 255)
    # Otherwise, the image is *not* low contrast, so in order to continue to processing it
    else:
        # Find contours in the edge map and find the largest one, which will be assumed to be the outline
        # of the color correction card
        cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        c = max(cnts, key=cv2.contourArea)
        # Draw the largest contour on the image
        cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
    # Draw the text on the output frame
    cv2.putText(frame, text, (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    # Stack the output frame and edge map next to each other
    output = np.dstack([edged] * 3)
    output = np.hstack([frame, output])
    # Show the output to the screen
    cv2.imshow("Output", output)
    key = cv2.waitKey(1) & 0xFF
    # If the 'q' key was pressed, then break from the loop
    if key == ord("q"):
        break

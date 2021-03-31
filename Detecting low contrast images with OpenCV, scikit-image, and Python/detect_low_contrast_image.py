# -----------------------------
#   USAGE
# -----------------------------
# python detect_low_contrast_image.py --input examples

# -----------------------------
#   IMPORTS
# -----------------------------
# Import the necessary packages
from skimage.exposure import is_low_contrast
from imutils.paths import list_images
import argparse
import imutils
import cv2

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="Path to input directory of images")
ap.add_argument("-t", "--thresh", type=float, default=0.35, help="Threshold for low contrast")
# The threshold for low contrast -> 밝기 범위의 35 % 미만이 데이터 유형의 전체 범위를 차지하면 이미지가 낮은 대비로 간주
args = vars(ap.parse_args())

# Grab the paths to the input images
imagePaths = sorted(list(list_images(args["input"])))

# Loop over the image paths
for (i, imagePath) in enumerate(imagePaths):
    # Load the input image from disk, resize it and convert it to grayscale
    print("[INFO] Processing image {}/{}".format(i + 1, len(imagePaths)))
    image = cv2.imread(imagePath)
    image = imutils.resize(image, width=450)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Blur the image slightly and perform edge detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 30, 150)
    # Initialize the text and color to indicate that the input image is *not* low contrast
    text = "Low contrast: No"
    color = (0, 255, 0)
    # Check to see if the image is low contrast
    if is_low_contrast(gray, fraction_threshold=args["thresh"]):
        # Update the text and color
        text = "Low contrast: Yes"
        color = (0, 0, 255)
    # Otherwise, the image is *not* low contrast, so in order to continue to processing it
    else:
        # Find contours in the edge map and find the largest one, which will be assumed to be the outline
        # of the color correction card
        cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.RETR_EXTERNAL : 가장 바깥쪽 외곽선만 검출
        # cv2.CHAIN_APPROX_SIMPLE : 수직선, 수평선, 대각선에 대해 끝점만 사용하여 압축
        cnts = imutils.grab_contours(cnts) # contour 총 개수
        c = max(cnts, key=cv2.contourArea) # key는 외곽선으로 구성된 면적
        # Draw the largest contour on the image
        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    # Draw the test on the output image
    cv2.putText(image, text, (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    # Show the output image and edge map
    cv2.imshow("Image", image)
    cv2.imshow("Edge", edged)
    cv2.waitKey(0)

import cv2
import mediapipe as mp
import math
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
mp_holistic = mp.solutions.holistic
# mp.drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2) # color, line 두께, 원 반경

def distance(x1, y1, x2, y2):
  result = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
  return result

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.

    image.flags.writeable = False
    results = pose.process(image)
    (h, w) = image.shape[:2]


    left_ear_x = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EAR].x * w
    left_ear_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EAR].y * h
    right_ear_x = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EAR].x * w
    right_ear_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EAR].y * h

    # 길이 구하기
    ear_length = distance(left_ear_x, left_ear_y, right_ear_x,right_ear_y)
    print("양쪽 귀 길이 : " , ear_length)
    # Draw the pose annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
      image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    cv2.imshow('MediaPipe Pose', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()

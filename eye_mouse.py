import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize camera and FaceMesh
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

# Smoothing factor
prev_x, prev_y = 0, 0
smooth_factor = 0.2  # Between 0 and 1

while True:
    ret, frame = cam.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks

    frame_h, frame_w, _ = frame.shape

    if landmark_points:
        landmarks = landmark_points[0].landmark

        # Use landmark 475 (or 468) for iris center
        eye_landmark = landmarks[475]  # You can try 468 for iris center

        x = int(eye_landmark.x * frame_w)
        y = int(eye_landmark.y * frame_h)
        cv2.circle(frame, (x, y), 4, (0, 255, 0), -1)

        # Map to screen coordinates
        target_x = eye_landmark.x * screen_w
        target_y = eye_landmark.y * screen_h

        # Smooth movement
        curr_x = prev_x + (target_x - prev_x) * smooth_factor
        curr_y = prev_y + (target_y - prev_y) * smooth_factor

        pyautogui.moveTo(curr_x, curr_y)
        prev_x, prev_y = curr_x, curr_y

        # Blink detection (optional - left eye)
        left_eye_top = landmarks[145]
        left_eye_bottom = landmarks[159]
        top_y = int(left_eye_top.y * frame_h)
        bottom_y = int(left_eye_bottom.y * frame_h)

        cv2.circle(frame, (int(left_eye_top.x * frame_w), top_y), 3, (255, 0, 255), -1)
        cv2.circle(frame, (int(left_eye_bottom.x * frame_w), bottom_y), 3, (255, 0, 255), -1)

        if abs(top_y - bottom_y) < 5:  # Threshold might need tuning
            pyautogui.click()
            time.sleep(1)

    cv2.imshow('Eye Controlled Mouse', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()
cv2.destroyAllWindows()
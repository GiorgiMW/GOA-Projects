import pyautogui
import cv2
import numpy as np

res = (1920, 1080)

codec = cv2.VideoWriter_fourcc(*"XVID")

file_name = "Video.avi"

fps = 30.0

out = cv2.VideoWriter(file_name, codec, fps, res)
cv2.namedWindow("Recorder", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Recorder", 480, 270)

while True:
    img = pyautogui.screenshot()
    frames = np.array(img)
    frames = cv2.cvtColor(frames, cv2.COLOR_BGR2RGB)
    out.write(frames)
    cv2.imshow('Recorder', frames)

    if cv2.waitKey(1) == ord("|"):
        break
out.release()

cv2.destroyAllWindows()
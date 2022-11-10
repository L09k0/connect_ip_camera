from os import scandir
import numpy as np
import cv2

#example link rtsp://Name user:Password@ip:port/stream1 or stream2
#example link rtsp://Logko:123@192.168.2.5:8543/stream1 or stream2
stream = cv2.VideoCapture('link ip camera')
try:
    while True:
        ret, frame = stream.read()
        height, width, layers = frame.shape
        frame = cv2.resize(frame, (width // 2, height // 2))
        cv2.imshow("CLOSE MEGA DOOR!", frame)
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break
except Exception as e:
    print("ERROR:", e)
if __name__ == "__main__":
    stream.release()
    cv2.destroyAllWindows()

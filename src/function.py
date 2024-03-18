import cv2
import os

def save_all_frames(input_path, output_path='../data/output', basename='frame', extension='jpg'):
    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        return

    os.makedirs(output_path, exist_ok=True)
    base_path = os.path.join(output_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), extension), frame)
            n += 1
        else:
            break

def other_mode():
    print("This is a test")
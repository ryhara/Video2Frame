import cv2
import os
import datetime

def video_to_image_all(input_path, output_path='../data/output', basename='frame', extension='jpg'):
    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        return

    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    output_path = os.path.join(output_path, timestamp)
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

def video_info(input_path):
    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        return

    print ('File:', input_path)
    print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
    print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print('Frame count:', int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
    print('Frame rate:', cap.get(cv2.CAP_PROP_FPS))
    print('Duration (s):', int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) / cap.get(cv2.CAP_PROP_FPS))

    cap.release()

# TODO : split完成させる
def video_cut(input_path, output_path='../data/output', basename='frame', extension='mp4', start_sec=0, end_sec=10):
    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        return

    os.makedirs(output_path, exist_ok=True)
    base_path = os.path.join(output_path, basename)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('{}_{}_to_{}.{}'.format(base_path, start_sec, end_sec, extension), fourcc, 20.0, (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

    start_frame = int(start_sec * cap.get(cv2.CAP_PROP_FPS))
    end_frame = int(end_sec * cap.get(cv2.CAP_PROP_FPS))

    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            if cap.get(cv2.CAP_PROP_POS_FRAMES) >= end_frame:
                break
        else:
            break

    cap.release()
    out.release()

def other_mode():
    print("This is a test")
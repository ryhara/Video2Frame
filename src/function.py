import cv2
import os
import datetime
from moviepy.editor import VideoFileClip
import os
import time

def video_to_image_all(input_path, output_path='../data/output', basename='frame', extension='jpg'):
    """Save all frames of a video to images.

    Args:
        input_path (str): input_path of the video.
        output_path (str, optional): output_path of the images. Defaults to '../data/output'.
        basename (str, optional): basename for the saved images. Defaults to 'frame'.
        extension (str, optional): extension for the saved images. Defaults to 'jpg'.
    """
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
    """Print information of a video.

    Args:
        input_path (str): input_path of the video.
    """
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

def video_cut(input_path, output_path='../data/output', basename='video', extension='mp4', start=0, end=10, swap_dimensions=False):
    """Cut a video.

    Args:
        input_path (str): input_path of the video.
        output_path (str, optional): output_path of the video. Defaults to '../data/output'.
        basename (str, optional): basename for the saved video. Defaults to 'video_'.
        extension (str, optional): extension for the saved video. Defaults to 'mp4'.
        start (int, optional): start time to cut the video. Defaults to 0.
        end (int, optional): end time to cut the video. Defaults to 10.
        swap_dimensions (bool, optional): swap dimensions of the video. Defaults to False.
    """
    output_filename = f"{basename}_{start}s_{end}s.{extension}"
    output_file_path = os.path.join(output_path, output_filename)

    os.makedirs(output_path, exist_ok=True)

    clip = VideoFileClip(input_path)

    width, height = clip.size

    if swap_dimensions:
        cut_clip = clip.subclip(start, end).resize((height, width))
    else:
        cut_clip = clip.subclip(start, end)

    cut_clip.write_videofile(output_file_path, codec='libx264', audio_codec='aac')

    clip.close()
    cut_clip.close()

def video_split(input_path, output_path='../data/output', basename='video', extension='mp4', split_num=2, swap_dimensions=False):
    """Split a video into multiple videos.

    Args:
        input_path (str): input_path of the video.
        output_path (str, optional): output_path of the video. Defaults to '../data/output'.
        basename (str, optional): basename for the saved video. Defaults to 'video_'.
        extension (str, optional): extension for the saved video. Defaults to 'mp4'.
        split_num (int, optional): number of split videos. Defaults to 2.
        swap_dimensions (bool, optional): swap dimensions of the video. Defaults to False.
    """
    os.makedirs(output_path, exist_ok=True)

    clip = VideoFileClip(input_path)
    total_duration = clip.duration
    width, height = clip.size

    clip_duration = total_duration / split_num
    clip.close()

    for i in range(split_num):
        clip = VideoFileClip(input_path)
        start_time = i * clip_duration
        end_time = min((i + 1) * clip_duration, total_duration)

        output_filename = f"{basename}_{i+1}.{extension}"
        output_file_path = os.path.join(output_path, output_filename)

        if swap_dimensions:
            cut_clip = clip.subclip(start_time, end_time).resize((height, width))
        else:
            cut_clip = clip.subclip(start_time, end_time)

        cut_clip.write_videofile(output_file_path, codec='libx264', audio_codec='aac')

        clip.close()
        cut_clip.close()
        time.sleep(2)



def print_info(mode):
    """Print information of a video.

    Args:
        mode (str): mode to run the program.
    """
    print('Mode "{}" is not implemented yet.'.format(mode))
    print('Please choose one of the following modes:')
    print('  all:    Save all frames of a video to images.')
    print('  info:   Print information of a video.')
    print('  cut:    Cut a video.')
    print('  split:  Split a video into multiple videos.')
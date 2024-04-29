import cv2
import os
import datetime
import time
from moviepy.editor import VideoFileClip, ImageSequenceClip

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

    info_file_path = os.path.join(output_path, "info.txt")
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    digit = len(str(frame_count))

    with open(info_file_path, 'w') as f:
        n = 0
        while True:
            ret, frame = cap.read()
            if ret:
                file_name = '{}_{}.{}'.format(basename, str(n).zfill(digit), extension)
                full_path = os.path.join(output_path, file_name)
                cv2.imwrite(full_path, frame)
                microseconds = int((n / fps) * 1e6)
                f.write(f"{output_path}/{file_name} {microseconds}\n")
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

def video_cut(input_path, output_path='../data/output', basename='video', extension='mp4', start=0, end=10, swap_aspect=False):
    """Cut a video.

    Args:
        input_path (str): input_path of the video.
        output_path (str, optional): output_path of the video. Defaults to '../data/output'.
        basename (str, optional): basename for the saved video. Defaults to 'video_'.
        extension (str, optional): extension for the saved video. Defaults to 'mp4'.
        start (int, optional): start time to cut the video. Defaults to 0.
        end (int, optional): end time to cut the video. Defaults to 10.
        swap_aspect (bool, optional): swap aspect ratio of the video. Defaults to False.
    """
    output_filename = f"{basename}_{start}s_{end}s.{extension}"
    output_file_path = os.path.join(output_path, output_filename)

    os.makedirs(output_path, exist_ok=True)

    clip = VideoFileClip(input_path)

    width, height = clip.size

    if swap_aspect:
        cut_clip = clip.subclip(start, end).resize((height, width))
    else:
        cut_clip = clip.subclip(start, end)

    cut_clip.write_videofile(output_file_path, codec='libx264', audio_codec='aac')

    clip.close()
    cut_clip.close()

def video_split(input_path, output_path='../data/output', basename='video', extension='mp4', split_num=2, swap_aspect=False):
    """Split a video into multiple videos.

    Args:
        input_path (str): input_path of the video.
        output_path (str, optional): output_path of the video. Defaults to '../data/output'.
        basename (str, optional): basename for the saved video. Defaults to 'video_'.
        extension (str, optional): extension for the saved video. Defaults to 'mp4'.
        split_num (int, optional): number of split videos. Defaults to 2.
        swap_aspect (bool, optional): swap aspect ratio of the video. Defaults to False.
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

        if swap_aspect:
            cut_clip = clip.subclip(start_time, end_time).resize((height, width))
        else:
            cut_clip = clip.subclip(start_time, end_time)

        cut_clip.write_videofile(output_file_path, codec='libx264', audio_codec='aac')

        clip.close()
        cut_clip.close()
        time.sleep(2)

def frames_to_video(input_path, output_path='../data/output', basename='video', extension='mp4', fps=30):
    """Convert frames to a video.

    Args:
        input_path (str): input_path of the frames.
        output_path (str, optional): output_path of the video. Defaults to '../data/output'.
        fps (int, optional): frame rate of the video. Defaults to 30.
    """
    os.makedirs(output_path, exist_ok=True)
    output_path = os.path.join(output_path, '{}.{}'.format(basename, extension))
    if os.path.isdir(input_path):
        frames_dir = input_path
        frame_paths = sorted([os.path.join(frames_dir, f) for f in os.listdir(frames_dir) if f.endswith(('.png', '.jpg'))])
        clip = ImageSequenceClip(frame_paths, fps=fps)
        clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
    else:
        raise ValueError("input_path must be a directory. images in the directory will be used to create the video.")

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
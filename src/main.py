import argparse
from function import video_to_image_all, print_info, video_info, video_cut, video_split, frames_to_video

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Save all frames of a video to images.')
    parser.add_argument('input_path', type=str, help='Path to the input video.')
    parser.add_argument('-o', '--output_path', type=str, default='../data/output', help='Directory to save the images. Default is "../data/output".')
    parser.add_argument('-m', '--mode', type=str, default='video2frame', help='Mode to run the program. Default is "video2frame".')
    parser.add_argument('-b', '--basename', type=str, default='frame', help='Basename for the saved images. Default is "frame".')
    parser.add_argument('-ie', '--img_extension', type=str, default='jpg', help='img_extension for the saved images. Default is "jpg".')
    parser.add_argument('-v', '--video_extension', type=str, default='mp4', help='video_extension for the saved video. Default is "mp4".')
    parser.add_argument('-s', '--start_s', type=int, default=0, help='Start time to cut the video. Default is 0.')
    parser.add_argument('-e', '--end_s', type=int, default=10, help='End time to cut the video. Default is 10.')
    parser.add_argument('-n', '--split_num', type=int, default=2, help='Number of split videos. Default is 2.')
    parser.add_argument('-sw', '--swap_aspect', type=bool, default=False, help='Swap the aspect ratio of the video.')
    parser.add_argument('-f', '--fps', type=int, default=24, help='Frame rate of the video. Default is 30.')

    args = parser.parse_args()

    if args.mode == 'video2frame':
        video_to_image_all(args.input_path, args.output_path, args.basename, args.img_extension)
    elif args.mode == 'frame2video':
        frames_to_video(args.input_path, args.output_path, args.basename, args.video_extension, args.fps)
    elif args.mode == 'info':
        video_info(args.input_path)
    elif args.mode == 'cut':
        video_cut(args.input_path, args.output_path, args.basename, args.video_extension, args.start_s, args.end_s, args.swap_aspect)
    elif args.mode == 'split':
        video_split(args.input_path, args.output_path, args.basename, args.video_extension, args.split_num, args.swap_aspect)
    else:
        print_info(args.mode)

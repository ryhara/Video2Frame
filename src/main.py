import argparse
from function import video_to_image_all, other_mode, video_info, video_split

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Save all frames of a video to images.')
    parser.add_argument('input_path', type=str, help='Path to the input video.')
    parser.add_argument('--mode', type=str, default='all', help='Mode to run the program. Default is "all".')
    parser.add_argument('--output_path', type=str, default='../data/output', help='Directory to save the images. Default is "../data/output".')
    parser.add_argument('--basename', type=str, default='frame', help='Basename for the saved images. Default is "frame".')
    parser.add_argument('--extension', type=str, default='jpg', help='Extension for the saved images. Default is "jpg".')

    args = parser.parse_args()

    if args.mode == 'all':
        video_to_image_all(args.input_path, args.output_path, args.basename, args.extension)
    elif args.mode == 'info':
        video_info(args.input_path)
    elif args.mode == 'split':
        video_split(args.input_path, args.output_path, args.basename, args.extension)
    else:
        other_mode()

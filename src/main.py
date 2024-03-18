import argparse
from function import save_all_frames, other_mode

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Save all frames of a video to images.')
    parser.add_argument('input_path', type=str, help='Path to the input video.')
    parser.add_argument('--mode', type=str, default='all', help='Mode to run the program. Default is "all".')
    parser.add_argument('--output_path', type=str, default='../data/output', help='Directory to save the images. Default is "../data/output".')
    parser.add_argument('--basename', type=str, default='frame', help='Basename for the saved images. Default is "frame".')
    parser.add_argument('--extension', type=str, default='jpg', help='Extension for the saved images. Default is "jpg".')

    args = parser.parse_args()

    if args.mode == 'all':
        save_all_frames(args.input_path, args.output_path, args.basename, args.extension)
    else:
        other_mode()

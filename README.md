# Video2Frame

## Function
### video2frame
> 動画をフレームごとに切り出して、画像に変換します。全てのフレームを画像として保存します

### frame2video
> １つのディレクトリ内にある画像から、動画を作成します。画像は名前順で用いられます。

### cut
> 秒数を指定して、動画の特定の区間を切り出します。

### split
> 動画を指定した数に分割します。

### info
> 動画の情報を出力します。


## Environment

実行環境は以下の通りとなっています。

> - M1 MacBook Air / macOS Sonoma 14.2.1
> - conda 23.7.2

**手動でconda環境を作成する方法**

```
conda create -n Video2Frame python=3.8
```

```
conda activate Video2Frame
```

```
conda install ffmpeg
```

```
pip install -r requirements.txt
```

**conda env createでconda環境を作成する方法**

※こちらは動作確認は行っていません
```
conda env create -f environment.yml
```

Python3, numpy, opencv-python, moviepy, ffmpegが入っていれば基本的に動くと思いますが、他の環境では動作確認を行っていないので保証できません。

動かない場合は仮想環境を作成して実行してみてください。

## Dataset

### input

> 入力となる動画は`data/input/`以下に配置してください。
>
> 実行時に入力動画のpathを引数に取るため、別の場所に配置することも可能です。


### output

> 出力結果は指定しない限り、`data/output/`以下に保存されます。
>
> 引数で指定することも可能です。指定方法は Usage を確認してください。

## Usage

```
cd src
```

```
python main.py <input_path> [--output_path=, --mode=, --basename=, --img_extension=, --video_extension=, --start_s, --end_s, --split_num, --swap_aspect, --fps]
```
> input_path は必ず指定してください。その他のパラメータはオプションです

**オプションの確認方法**

```
python main.py -h
```

```
usage: main.py [-h] [-o OUTPUT_PATH] [-m MODE] [-b BASENAME]
               [-ie IMG_EXTENSION] [-v VIDEO_EXTENSION] [-s START_S]
               [-e END_S] [-n SPLIT_NUM] [-sw SWAP_ASPECT] [-f FPS]
               input_path

Save all frames of a video to images.

positional arguments:
  input_path            Path to the input video.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_PATH, --output_path OUTPUT_PATH
                        Directory to save the images. Default is
                        "../data/output".
  -m MODE, --mode MODE  Mode to run the program. Default is "video2frame".
  -b BASENAME, --basename BASENAME
                        Basename for the saved images. Default is "frame".
  -ie IMG_EXTENSION, --img_extension IMG_EXTENSION
                        img_extension for the saved images. Default is "jpg".
  -v VIDEO_EXTENSION, --video_extension VIDEO_EXTENSION
                        video_extension for the saved video. Default is "mp4".
  -s START_S, --start_s START_S
                        Start time to cut the video. Default is 0.
  -e END_S, --end_s END_S
                        End time to cut the video. Default is 10.
  -n SPLIT_NUM, --split_num SPLIT_NUM
                        Number of split videos. Default is 2.
  -sw SWAP_ASPECT, --swap_aspect SWAP_ASPECT
                        Swap the aspect ratio of the video.
  -f FPS, --fps FPS     Frame rate of the video. Default is 30.
```

### Makefile
効率化のためMakefileでの実行方法も用意しています。Makefile 内に解説を書いているのでご活用ください

Makefileで実行する場合と、src/内で実行する場合の相対パスの指定の仕方に注意してください

```
make 〇〇
```

## License

MIT LICENSE

## Reference

- [Python, OpenCV で動画ファイルからフレームを切り出して保存 | note.nkmk.me](https://note.nkmk.me/python-opencv-video-to-still-image/)

# video2Frame

## Environment

実行環境は以下の通りとなっています。

- M1 MacBook Air / macOS Sonoma 14.2.1
- conda 23.7.2

```
conda create -n video2Frame python=3.8
```

```
pip install -r requirements.txt
```

Python3, numpy, opencv-python が入っていれば基本的に動くと思いますが、他の環境では動作確認を行っていないので保証できません。

動かない場合は仮想環境を作成して実行して見てください。

## Dataset

### input

入力となる動画は`data/input/`以下に配置してください。

### output

出力結果は指定しない限り、`data/output/`以下に保存されます。

引数で指定することも可能です。指定方法は Usage を確認してください。

## Usage

```
cd src
```

input_path は必ず指定してください。その他のパラメータはオプションです

```
python main.py <input_path> [--mode=, --output_path=, --basename=, --extension= ]
```

オプションの確認方法

```
python main.py -h
```

Makefile での実行方法も用意しています。Makefile 内に解説を書いているのでご活用ください

```
make 〇〇
```

## License

MIT LICENSE

## Reference

- [Python, OpenCV で動画ファイルからフレームを切り出して保存 | note.nkmk.me](https://note.nkmk.me/python-opencv-video-to-still-image/)

usage:
	echo "make [clean_input, clean_output, clean_cache, clean, info, run, cut]"

# remove all files in input folder
clean_input:
	find ./data/input ! -name '.gitignore' -delete

# remove all files in output folder
clean_output:
	find ./data/output ! -name '.gitignore' -delete

# remove all cache files
clean_cache:
	rm -rf ./src/__pycache__

# remove all files in output folder, and cache files
clean: clean_output clean_cache

# main.pyの引数を指定して実行してください

# run the video to frame
run :
	python ./src/main.py ./data/input/test.mp4 --output_path=./data/output/

# cut the video
cut:
	python ./src/main.py ./data/input/test.mp4 --mode=cut --output_path=./data/output/ --start_s=0 --end_s=5 --basename=video

# split the video
split:
	python ./src/main.py ./data/input/test.mp4 --mode=split --output_path=./data/output/ --split_num=10 --basename=video

# print the video info
info:
	python ./src/main.py ./data/input/test.mp4 --mode=info --output_path=./data/output/

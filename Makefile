usage:
	echo "make [clean_input, clean_output, clean_cache, clean, info, run, split]"


clean_input:
	find ./data/input ! -name '.gitignore' -delete

clean_output:
	find ./data/output ! -name '.gitignore' -delete

clean_cache:
	rm -rf ./src/__pycache__

clean: clean_output clean_cache

run :
	python ./src/main.py ./data/input/test.mp4

split:
	python ./src/main.py ./data/input/test.mp4 --mode=split

info:
	python ./src/main.py ./data/input/test.mp4 --mode=info

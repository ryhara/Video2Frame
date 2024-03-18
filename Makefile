usage:
	echo "make [clean_input, clean_output, clean_cache, clean, run]"


clean_input:
	find ./data/input ! -name '.gitignore' -delete

clean_output:
	find ./data/output ! -name '.gitignore' -delete

clean_cache:
	rm -rf ./src/__pycache__

clean: clean_output clean_cache

run :
	python ./src/main.py input_path=. --mode=a

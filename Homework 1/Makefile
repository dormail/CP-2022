all: build/main.pdf

build/Ex1.pdf: Exercise1.py | build
	python Exercise1.py

build/Ex2.pdf: Exercise2.py | build
	python Exercise2.py
	
build/Ex3.pdf: Exercise3.py | build
	python Exercise3.py

Exercise4.py: Exercise4.ipynb
	jupyter nbconvert --to script "Exercise4.ipynb"

build/many_walks.pdf: Exercise4.py | build
	python Exercise4.py

build/main.pdf: build/Ex1.pdf
build/main.pdf: build/Ex2.pdf
build/main.pdf: build/Ex3.pdf
build/main.pdf: build/many_walks.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build Exercise4.py

FORCE:

.PHONY: all clean

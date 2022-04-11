all: build/main.pdf

build:
	mkdir -p build

build/Ex1.pdf: Exercise1.py build
	python Exercise1.py

build/Ex2.pdf: Exercise2.py build
	python Exercise2.py

build/many_walks.pdf: Exercise4.py build
	python Exercise4.py


build/main.pdf: build main.tex build/Ex1.pdf build/Ex2.pdf build/many_walks.pdf
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex


clean:
	rm -rf build

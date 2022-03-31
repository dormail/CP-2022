all: build/main.pdf

build:
	mkdir -p build

build/main.pdf: build main.tex build/Ex1.pdf
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build/Ex1.pdf: Exercise1.py build
	python Exercise1.py

clean:
	rm -rf build

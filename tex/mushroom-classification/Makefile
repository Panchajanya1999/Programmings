# makefile for cleaning files automatically

# target files to build
PYTHON := $(wildcard *.py)
TEXFILES := $(wildcard *.tex)

all: python pdf

python: $(PYTHON)
	@echo "Building python files"
	python3 $^
	@echo "Python files built successfully"

pdf: $(TEXFILES)
	@echo "Preparing to build the project"
	pdflatex -interaction=nonstopmode -halt-on-error -file-line-error $^
	@echo "Build complete"

clean:
	@echo "Cleaning up generated files..."
	rm -rf *log *.out *.gz *.fls *.fdb_latexmk *.aux *.toc *.bbl *.blg *.dvi *.ps *.synctex.gz
	@echo "Cleaning Done Successfully!"

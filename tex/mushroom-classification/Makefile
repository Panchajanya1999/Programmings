# makefile for cleaning files automatically

# target files to build
PYTHON := $(wildcard *.py)
TEXFILES := $(wildcard *.tex)

# Color options
ERED := \033[0;31m
EGREEN := \033[0;32m
EWHT := \033[0m
EYELLOW := \033[0;33m

help:
	@echo -e "$(EGREEN)This is a makefile for building and cleaning project automatically.$(EWHT)"
	@echo -e "Usage: $(EYELLOW)make [target]$(EGREEN)"
	@echo -e "Targets:"
	@echo -e "  $(EYELLOW)help$(EGREEN): show this help message"
	@echo -e "  $(EYELLOW)python$(EGREEN): build python files"
	@echo -e "  $(EYELLOW)tex$(EGREEN): build tex files into a pdf file"
	@echo -e "  $(EYELLOW)all$(EGREEN): build all files"
	@echo -e "  $(EYELLOW)clean$(EGREEN): clean all files"

all: python tex

python: $(PYTHON)
	@echo -e "$(EYELLOW)Building python files$(EWHT)"
	@echo ""
	python3 $^
	@echo ""
	@echo -e "$(EGREEN)Python files built successfully"

tex: $(TEXFILES)
	@echo -e "$(EYELLOW)Preparing to build the project"
	pdflatex -interaction=nonstopmode -halt-on-error -file-line-error $^
	@echo -e "$(EGREEN)Build complete"

clean:
	@echo -e "$(EYELLOW)Cleaning up generated files..."
	rm -rf *log *.out *.gz *.fls *.fdb_latexmk *.aux *.toc *.bbl *.blg *.dvi *.ps *.synctex.gz
	@echo -e "$(EGREEN)Cleaning Done Successfully!"

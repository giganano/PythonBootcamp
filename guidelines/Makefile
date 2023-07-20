
TEXCOMPILER := pdflatex

all: guidelines.pdf

%.pdf: *.tex %.sty
	@ $(TEXCOMPILER) $(basename $@)
	@ $(TEXCOMPILER) $(basename $@)

.PHONY: clean
clean:
	@ rm -f *.aux
	@ rm -f *.log
	@ rm -f guidelines.pdf

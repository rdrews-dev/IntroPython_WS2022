all: CollectionExam.pdf

clean:
	rm -f *.aux *.dvi *.log *.out *.pdf *.fdb_latexmk *.fls *.synctex.gz
	rm -f Includes/*.aux

dependencies = $(wildcard Figures/*.jpg Figures/*.png) \
	$(wildcard Includes/*.tex) \
	$(wildcard Src/*.py) \

CollectionExam.pdf: CollectionExam.tex Header.tex ${dependencies}
	pdflatex CollectionExam.tex

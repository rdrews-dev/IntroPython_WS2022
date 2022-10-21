all: CollectionExercises.pdf

clean:
	rm -f *.aux *.dvi *.log *.out *.pdf
	rm Includes/*.aux

dependencies = $(wildcard Figures/*.jpg Figures/*.png) \
	$(wildcard Includes/*.tex) \
	$(wildcard Src/Ex0/*.py) \
	$(wildcard Src/Ex1/*.py) \
	$(wildcard Src/Ex2/*.py) \
	$(wildcard Src/Ex3/*.py) \
	$(wildcard Src/Ex4/*.py)

CollectionExercises.pdf: CollectionExercises.tex Header.tex ${dependencies}
	pdflatex CollectionExercises.tex

all: CollectionExercises.pdf

clean:
	rm -f *.aux *.dvi *.log *.out *.pdf
	rm Includes/*.aux

dependencies = Figures/20181031_140359.jpg \
    Figures/virtual_box1.png \
    Figures/virtual_box2.png \
    Figures/vs_code1.png \
		Includes/Ex0.tex \
		Includes/Ex1.tex \
		Includes/Ex2.tex \
		Includes/Ex3.tex \
		Includes/ExAdvanced.tex \
		Src/Ex0/PlotExample.py \
		Src/Ex1/HelloWorld.py \
		Src/Ex1/KeelingRawData.py\
		Src/Ex1/KeelingFilter.py\
		Src/Ex3/UserInput.py

CollectionExercises.pdf: CollectionExercises.tex Header.tex ${dependencies}
	pdflatex CollectionExercises.tex

report.pdf: report.tex myplot1.png myplot2.png 
	latexmk -pdf

myplot1.png: cox_etal_2013.txt project.py
	python3 cylinders_3D.py

myplot2.png: cox_etal_2013.txt project.py
	python3 project.py

.PHONY: clean almost_clean

clean: almost_clean
	rm report.pdf
	rm myplot1.png
	rm myplot2.png

almost_clean:
	latexmk -c

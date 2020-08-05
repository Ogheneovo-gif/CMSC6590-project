processed_data.pkl: cox_etal_2013.txt process_data.py
	     python3 process_data.py

plot1.png: processed_data.pkl make_myplot1.py
	     python3 make_myplot1.py

plot2.png: processed_data.pkl make_myplot1.py
	     python make_myplot2.py

.PHONY: clean almost_clean

clean: almost_clean
	rm report.pdf
	rm myplot1.png
	rm myplot2.png

almost_clean:
	latexmk -c

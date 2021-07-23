##
# Doc gen crypto
#
# @file
# @version 0.1

make:
	pdflatex  -shell-escape -interaction nonstopmode  main && \
	biber main && \
	pdflatex  -shell-escape -interaction nonstopmode  main

clean:
	rm *.el *.aux *.out *.log .auctex-auto/ *.synctex.gz *.toc \
	   *.pdf _minted-main/ *.bbl *.bcf *.blg *.run.xml -rf

# end

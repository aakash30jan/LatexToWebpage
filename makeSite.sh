#sudo apt-get install texstudio texlive-latex-extra
#sudo apt-get install texlive-fonts-recommended

cd ./CV/LaTeX/
pdflatex -interaction=nonstopmode main.tex 
cp main.pdf ../myCV.pdf
cd ../../
echo "CV has been generated."

python putTex.py
echo "Website data has been generated."


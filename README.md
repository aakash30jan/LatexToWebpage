# LatexToWebpage
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1464274.svg)](https://doi.org/10.5281/zenodo.1464274)  
[![HitCount](http://hits.dwyl.io/aakash30jan/LatexToWebpage.svg)](http://hits.dwyl.io/aakash30jan/LatexToWebpage)

A pythonic way of putting LaTeX CV data to your webpage.  
This code makes use of Moderncv documentclass by Xavier Danaux (https://github.com/xdanaux/moderncv) and webpage style-sheet by Jon Barron's code (https://github.com/jonbarron/jonbarron_website).  


## Directory Structure:
```sh
.
├── CV
│   ├── LaTeX
│   │   ├── main.tex
│   │   ├── main.pdf
│   │   ├── logo.png
│   │   └── [ALL moderncv documnetclass files]
│   └── myCV.pdf
├── index.html
├── LICENSE
├── makeSite.sh
├── putTex.py
├── README.md
└── website
    ├── images
    │   ├── favicon.ico
    │   ├── project1.png
    │   └── <PUT ALL PROJECT IMAGES HERE>
    └── js
        └── scramble.js
```

## Requirements:  
1. Python 2.7  
2. Latex essentials: texstudio, texlive-latex-extra, texlive-fonts-recommended  

## Download  
Clone the repository with:  
`$ git clone https://github.com/aakash30jan/LatexToWebpage.git`  

## Using the code:
After you are done with editing the `./CV/LaTeX/main.tex` (the main latex file where you write your CV)  and the marked entries in `./index.html` (the main webpage file where you write your profile) proceed as follows:  
1. Execute with `bash makeSite.sh`.  
2. Your generated CV can be checked with `evince ./CV/myCV.pdf`.  
3. Your updated webpage can be checked with `firefox index.html`.  
4. You may now upload the webpage to your favourite hosting service !  

## Issues:
Problems? Please raise an issue at "https://github.com/aakash30jan/LatexToWebpage/issues" and I will get back to you soon.  
Please use `https://doi.org/10.5281/zenodo.1464274` if you wish to cite this code.  
## License
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

2025-11-20
To get the Sandia SAND report working with minted

python3 -m venv .venv
source .venv/bin/activate

pip install Pygments

pygmentize -V

should output Pygments version 2.x.x

compile LaTeX with 


pdflatex -shell-escape main.tex



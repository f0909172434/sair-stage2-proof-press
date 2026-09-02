# Paper

`main.tex` and `references.bib` are the source for the project paper. The manuscript reports released-input results, governed research outcomes, cost, and limitations. It does not claim a private score or rank.

Build from the repository root:

```sh
mkdir -p output/pdf tmp/pdfs/paper-build
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=tmp/pdfs/paper-build paper/main.tex
bibtex tmp/pdfs/paper-build/main
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=tmp/pdfs/paper-build paper/main.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=tmp/pdfs/paper-build paper/main.tex
cp tmp/pdfs/paper-build/main.pdf output/pdf/sair_stage2_solver_research.pdf
```

The final PDF is written to [`../output/pdf/sair_stage2_solver_research.pdf`](../output/pdf/sair_stage2_solver_research.pdf).

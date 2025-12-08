### Data Provenance and Reproducibility

This repository contains analysis code reproducing the statistical results
reported in the accompanying Physical Review D submission.

For numerical stability and long-term reproducibility, the differential cross-
section data used in the fits are **hard-coded directly into the analysis scripts**.
All values are taken verbatim from publicly available ATLAS and CMS HEPData records.

A detailed, line-by-line mapping between code variables and experimental data
tables is provided in `DATA_SOURCES.md`, including direct links to the original
HEPData entries so that results can be independently verified or modified.

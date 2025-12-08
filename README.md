# Discrete Scale Invariance in the Higgs Sector (PRD Submission)

This repository accompanies the Physical Review D submission:

**“Discrete Scale Invariance in the Higgs Sector: A Multi-Channel Analysis of Phase-Coherent Modulation”**

Author: Ryan D. Russell  
Affiliation: Horizon Code Initiative / Quesmart Research Group

---

## Purpose of This Repository

This repository provides:
- Exact analysis scripts used in the paper
- Hard-coded numerical values extracted from public ATLAS and CMS HEPData tables
- Figures reproduced directly from the analysis
- Complete manuscript source (LaTeX) and appendices

The repository is intended for **reproducibility, transparency, and referee audit**, not as a software library.

---

## Data Policy

No proprietary or restricted data are included.

All numerical values are:
- **Manually extracted** from public HEPData tables
- **Hard-coded intentionally** to eliminate API or backend dependence
- Fully referenced with direct URLs in `data_sources/`

Readers are encouraged to retrieve the original datasets independently and verify correspondence.

---

## How to Reproduce Figures

```bash
pip install -r analysis/requirements.txt
python analysis/fit_global.py
python analysis/plot_residuals.py

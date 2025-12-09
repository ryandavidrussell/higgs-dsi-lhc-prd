# Discrete Scale Invariance in the Higgs Sector (PRD Companion Repository)

This repository accompanies the Physical Review D submission:

**“Discrete Scale Invariance in the Higgs Sector: A Multi-Channel Analysis of Phase-Coherent Modulation”**

Author: Ryan D. Russell  
Affiliation: Horizon Code Initiative / Quesmart Research Group  

---

## Purpose of This Repository

This repository provides full transparency for the analysis reported in the PRD submission.

Specifically, it contains:
- The exact analysis scripts used to generate figures
- Hard-coded numerical inputs extracted from public ATLAS and CMS HEPData tables
- All generated figures appearing in the manuscript
- Full LaTeX source of the manuscript, appendices, and cover letter

The repository is intended for **reproducibility and referee inspection**, not as a software package.

---

## Data Policy

No proprietary or collaboration-internal data are used.

All numerical inputs were:
- Extracted manually from **public HEPData records**
- Hard-coded deliberately to avoid API dependence
- Fully cited with direct URLs

Readers are encouraged to independently retrieve the original datasets.

---

## Scope of Analysis

Included Higgs Run-2 channels:
- ATLAS ggF H → WW*
- CMS VBF H → γγ
- ATLAS ggF H → γγ
- ATLAS ggF H → ZZ*

This analysis does **not** claim discovery-level significance and is explicitly falsifiable with Run-3 data.
## How to Cite

If you use this code or analysis, please cite:

@misc{russell_higgs_dsi_lhc_prd_software,
  author       = {Ryan D. Russell},
  title        = {higgs-dsi-lhc-prd: Analysis and manuscript package},
  year         = {2025},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.17861311},
  url          = {https://doi.org/10.5281/zenodo.17861311}
}

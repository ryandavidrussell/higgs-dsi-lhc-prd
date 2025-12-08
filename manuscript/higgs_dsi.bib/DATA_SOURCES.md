# Data Sources for Hard-Coded LHC Inputs

This document specifies the provenance of all experimentally measured values
embedded directly into the analysis scripts in this repository.

All data originate from publicly released ATLAS and CMS measurements and were
transcribed without modification.

---

## 1. ATLAS ggF H → WW* (8 TeV)

- **Experiment:** ATLAS  
- **Channel:** ggF, H → WW*  
- **Energy:** √s = 8 TeV  
- **Integrated Luminosity:** 20.3 fb⁻¹  
- **HEPData Record:** INS1444991  
- **Table Used:** Fiducial differential cross sections (Table 3)  
- **Link:** https://www.hepdata.net/record/ins1444991  

**Code location:**  
`analysis/higgs_fit_hardcoded.py :: get_hww_data()`

Includes:
- Bin centers in p_T^H  
- Central values  
- Full 10×10 covariance matrix  

---

## 2. CMS VBF H → γγ (13 TeV)

- **Experiment:** CMS  
- **Channel:** VBF, H → γγ  
- **Energy:** √s = 13 TeV  
- **Integrated Luminosity:** 137 fb⁻¹  
- **HEPData Record:** INS2142341  
- **Table Used:** Differential cross sections (Table 3)  
- **Link:** https://www.hepdata.net/record/ins2142341  

**Code location:**  
`analysis/higgs_fit_hardcoded.py :: get_vbf_hgg_data()`

Diagonal covariance approximation is used as a conservative fallback.

---

## 3. ATLAS ggF H → γγ (13 TeV)

- **HEPData Record:** INS1674946  
- **Table Used:** Table 1  
- **Link:** https://www.hepdata.net/record/ins1674946  

**Code location:**  
`analysis/higgs_fit_hardcoded.py :: get_ggf_hgg_data()`

Tail bins only.

---

## 4. ATLAS ggF H → ZZ* (13 TeV)

- **HEPData Record:** INS1615206  
- **Table Used:** Table 1  
- **Link:** https://www.hepdata.net/record/ins1615206  

**Code location:**  
`analysis/higgs_fit_hardcoded.py :: get_ggf_hzz_data()`

---


# 🧬 From Data to Diagnosis: Practical AI in Hematology

> **A Comparative Study of GPT vs Retrieval-Augmented GPT for Lab Report Interpretation**  
> _Author: Merim Jusufbegović, 2025_  
> 📄 [Full Paper PDF](./docs/GPT_hematology_blood_analysis.pdf)

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-brightgreen.svg)](https://www.python.org/)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/hematology-ai/blob/main/notebooks/demo_colab.ipynb)

---

![Project Poster](./notebooks/demo_screenshot.png) <!-- Replace with your actual poster file -->

---

## 📚 Table of Contents
- [🧠 Project Summary](#-project-summary)
- [📂 Repository Structure](#-repository-structure)
- [🛠️ Quick Start (Local)](#️-quick-start-local)
- [🚀 Try It in Colab](#-try-it-in-colab)
- [📊 Evaluation Results](#-evaluation-results)
- [🔁 Replicate the Study](#-replicate-the-study)
- [🤝 Acknowledgements](#-acknowledgements)
- [📜 License](#-license)

---

## 🧠 Project Summary

This repository accompanies the research paper:

> **"Enhancing Hematology Interpretation with RAG"**

This study compares:
- 🧩 **GPT-only** model (baseline)
- 🧠 **GPT + RAG** model (enhanced with curated hematology documents)

Each AI model was used to analyze 50 anonymized hematology reports. Two medical laboratory experts scored the generated reports using a 5-point Likert scale. 📈 Results show measurable improvement in report quality and inter-rater agreement when using the RAG-enhanced model.

---

## 📂 Repository Structure

| Folder         | Description                                        |
|----------------|----------------------------------------------------|
| `data/`        | Sample lab dataset (100 patients) & reviewer scores |
| `src/hematology/` | Code for lab report analysis and report generation |
| `notebooks/`   | Interactive Google Colab demo                      |
| `results/`     | Evaluation plots, CSV tables                       |
| `docs/`        | Full research paper and how-to guides              |

---

## 🛠️ Quick Start (Local)

```bash
git clone https://github.com/YOUR_USERNAME/hematology-ai.git
cd hematology-ai
pip install -r requirements.txt

python src/hematology/analyzer.py
```

---

## 🚀 Try It in Colab

🟢 No setup required – run in your browser  
👉 [Open in Google Colab](https://colab.research.google.com/github/YOUR_USERNAME/hematology-ai/blob/main/notebooks/demo_colab.ipynb)

---

## 📊 Evaluation Results

| Model        | Reviewer | Mean Score | κ Agreement | % Good (4–5) |
|--------------|----------|------------|-------------|--------------|
| GPT (baseline) | R1      | 3.30       | -0.13       | 38%          |
| GPT (baseline) | R2      | 3.32       |             | 28%          |
| GPT + RAG     | R1      | 3.56       | 0.25        | 48%          |
| GPT + RAG     | R2      | 3.20       |             | 32%          |

📊 Heatmaps, boxplots, and CDF charts available in [`results/plots/`](./results/plots/)

---

## 🔁 Replicate the Study

To apply this workflow to your own lab data:

```bash
git checkout replication-template
```

1. Add your data to `data/lab_results.csv`  
2. Run the analysis:
```bash
python src/hematology/analyzer.py --input data/lab_results.csv
```

---

## 🤝 Acknowledgements

Special thanks to:

- Faculty of Health Studies, University of Sarajevo  
- Clinical Center of the University of Sarajevo  
- Reviewers for expert scoring  
- OpenAI GPT-4 and Retrieval tools

---

## 📜 License

Distributed under the **GNU AGPL v3.0 License**.  
See the [`LICENSE`](./LICENSE) file for details.

---

> 🧪 For research use only — not for clinical diagnosis without human oversight.

# 🧬 From Data to Diagnosis: Practical AI in Hematology

**A Comparative Study of GPT vs Retrieval-Augmented GPT for Lab Report Interpretation**

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

---

## 🧠 Project Summary

This repository contains code, data, and evaluation results from the study:

> **"Enhancing Hematology Interpretation with RAG"**  
> *(Merim Jusufbegović, 2025)*

The study compares baseline GPT-4 and a retrieval-augmented GPT-4 (RAG) agent in interpreting hematology panels. Using 50 reports per model, two blinded experts scored each output on a 5-point Likert scale. Results show that RAG reduces clinically poor outputs and improves inter-rater reliability.

📄 Full paper: [`GPT_hematology_blood_analysis.pdf`](./docs/GPT_hematology_blood_analysis.pdf)

---

## 📂 Repository Contents

| Folder             | Description                                         |
|--------------------|-----------------------------------------------------|
| `/data`            | Lab dataset, reviewer scores, and supporting files  |
| `/src/hematology`  | Core Python logic for lab analysis and reporting    |
| `/notebooks`       | Colab-ready interactive demo                        |
| `/results`         | Summary table, charts, and visual evaluation        |
| `/docs`            | Full paper, templates, and method documentation     |
| `/tests`           | Unit tests for analysis modules                     |

---

## 🛠️ Quick Start (Local)
```bash
git clone https://github.com/MerimJ/From-Data-to-Diagnosis-Practical-AI-in-Hematology.git
cd From-Data-to-Diagnosis-Practical-AI-in-Hematology
pip install -r requirements.txt

python src/hematology/analyzer.py
```

---

## 🚀 Try It in Colab
👉 [Open in Google Colab](https://colab.research.google.com/github/yourusername/hematology-ai/blob/main/notebooks/demo_colab.ipynb)

This notebook will:

Load sample hematology lab results from CSV

Generate diagnostic interpretations using GPT and RAG-GPT

Display Likert scores and output comparisons

Export results into formatted PDF reports

---

## 📊 Evaluation Results

| Model        | Reviewer | Mean Score | κ Agreement | % Good (4–5) |
|--------------|----------|------------|-------------|--------------|
| GPT (baseline) | R1      | 3.30       | -0.13       | 38%          |
| GPT (baseline) | R2      | 3.32       |             | 28%          |
| GPT + RAG     | R1      | 3.56       | 0.25        | 48%          |
| GPT + RAG     | R2      | 3.20       |             | 32%          |

🔬 These results reflect the expert evaluation of 100 reports
🧑‍⚕️ Reviewed independently by two laboratory professionals

---

## 🔁 Want to Run Your Own Study?

git checkout replication-template

python src/hematology/analyzer.py --input path_to_your_lab_data.csv

```
PatientID,Hb,WBC,Platelets,MCV,MCH,MCHC,...
101,12.5,7.2,250,90.2,31.4,33.6

```

---

## 🤝 Acknowledgements

- Faculty of Health Studies, University of Sarajevo
- Faculty of Electrical Engineering, University of Sarajevo
- OpenAI GPT-4 & RAG pipelines  
- Reviewers for scoring model output

---

## 📜 License

Licensed under the **GNU AGPL v3.0**.  
See [`LICENSE`](./LICENSE) for full terms.

---

## 🖼️ Project Visual Summary

![Project Poster](./Poster.png)

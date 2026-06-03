# Credit Risk Analytics & MLOps Pipeline 🚀

This project is a complete **end-to-end Machine Learning pipeline** for predicting **credit risk (loan default probability)** using structured financial data.

It includes data preprocessing, feature engineering, model training using XGBoost, and deployment using Streamlit.

---

## 📊 Project Overview

Financial institutions need to assess whether a loan applicant is likely to default.  
This project builds a **machine learning-based credit risk prediction system** that classifies applicants as:

- ✅ Low Risk
- ⚠️ High Risk

---

## 🧠 Machine Learning Approach

- Algorithm: **XGBoost Classifier**
- Data Preprocessing:
  - Missing value handling (median imputation)
  - Feature engineering (missing indicators)
- Encoding:
  - Label Encoding for categorical variables
- Evaluation Metrics:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - ROC-AUC

---

## 📂 Project Structure
Credit_risk_pipeline/
│
├── app.py
├── credit_risk_model.pkl
├── requirements.txt
├── README.md
│
├── data/
│ 
│
├── config/
│ └── config.yaml
│
└── notebooks/
└── Credit_Risk_Analytics_MLOps.ipynb

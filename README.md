# 💰 Credit Risk Analytics

A user-friendly Streamlit web application that predicts the likelihood of loan default using Machine Learning (XGBoost model).

---

## 🚀 Features

- Easy-to-use interface with helpful tooltips
- Real-time credit risk prediction
- Color-coded risk results (🟢 Low | 🟠 Medium | 🔴 High)
- Clear explanations for all input fields
- Professional and clean design

---

## 🎯 How to Use

1. Go to the sidebar and fill in the applicant details
2. Enter loan information
3. Click **"Predict Risk"** button
4. Get instant prediction with probability

---

## 📋 Input Fields Explanation

### Personal Information
- **Age**: Applicant's current age
- **Annual Income**: Yearly income in USD
- **Employment Length**: Years in current job
- **Home Ownership**: RENT, OWN, MORTGAGE, or OTHER

### Loan Details
- **Loan Amount**: Amount requested
- **Interest Rate**: Rate charged on the loan
- **Loan % of Income**: Loan amount relative to income
- **Loan Purpose**: Purpose of the loan
- **Loan Grade** (A-G): 
  - **A** = Lowest risk
  - **G** = Highest risk

### Credit History
- **Credit History Length**: Years of credit history
- **Previous Default on File**: Has the person defaulted before? (**Yes** = High Risk)

---

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Model**: XGBoost Classifier
- **Data Processing**: Pandas
- **Deployment**: Streamlit Community Cloud

---

## 📁 Project Structure
├── app.py                 
├── credit_risk_model.pkl  
├── requirements.txt        
└── README.md


---

## 🖥️ Live App

[Open App](https://credit-risk-analytics-dqxf6drasg3invduurf6js.streamlit.app/)

---

## ⚠️ Important Note

This application is for **educational and demonstration purposes**.  
The prediction should be used as a supporting tool only. Always perform proper due diligence before making lending decisions.

---

## 👨‍💻 Author

Created by [Your Name]

---

**Made with ❤️ using Streamlit**

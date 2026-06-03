import streamlit as st
import numpy as np
import joblib

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Credit Risk Dashboard",
    page_icon="💳",
    layout="wide"
)

# ---------------------------
# Load Model
# ---------------------------
model = joblib.load("model.pkl")

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Predict Risk", "About"])

# ---------------------------
# Dashboard Page
# ---------------------------
if page == "Dashboard":
    st.title("💳 Credit Risk Analytics Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Applications", "10,240", "1.2%")
    col2.metric("Approved Loans", "7,890", "2.5%")
    col3.metric("Default Rate", "3.8%", "-0.4%")

    st.markdown("---")

    st.info("This dashboard helps predict whether a loan applicant is High Risk or Low Risk using ML model.")

# ---------------------------
# Prediction Page
# ---------------------------
elif page == "Predict Risk":
    st.title("🔍 Loan Risk Prediction")

    st.markdown("### Enter Applicant Details")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 18, 100, 30)
        income = st.number_input("Annual Income", 10000, 10000000, 500000)
        loan_amount = st.number_input("Loan Amount", 1000, 1000000, 200000)

    with col2:
        credit_score = st.number_input("Credit Score", 300, 900, 650)
        employment_years = st.number_input("Employment Years", 0, 40, 5)

    if st.button("Predict Risk 🚀"):
        input_data = np.array([[age, income, loan_amount, credit_score, employment_years]])

        prediction = model.predict(input_data)

        st.markdown("---")

        if prediction[0] == 1:
            st.error("❌ High Risk Applicant")
            st.warning("Loan should NOT be approved")
        else:
            st.success("✅ Low Risk Applicant")
            st.info("Loan can be approved")

# ---------------------------
# About Page
# ---------------------------
elif page == "About":
    st.title("ℹ️ About Project")

    st.write("""
    This is a Machine Learning-based Credit Risk Analysis System.

    🔹 Model: XGBoost / ML Classifier  
    🔹 Input: Applicant financial details  
    🔹 Output: Risk classification (High / Low)

    Built using Streamlit for interactive deployment.
    """)

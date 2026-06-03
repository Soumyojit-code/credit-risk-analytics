import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("credit_risk_model.pkl")

st.title("Credit Risk Analytics")

st.write("Predict whether a loan applicant is high risk.")

person_age = st.number_input("Age", min_value=18, value=25)
person_income = st.number_input("Annual Income", value=50000)
person_emp_length = st.number_input("Employment Length", value=5)

loan_amnt = st.number_input("Loan Amount", value=10000)
loan_int_rate = st.number_input("Interest Rate", value=10.5)
loan_percent_income = st.number_input("Loan Percent Income", value=0.2)

cb_person_cred_hist_length = st.number_input(
    "Credit History Length",
    value=5
)

person_home_ownership = st.selectbox(
    "Home Ownership",
    [0, 1, 2, 3]
)

loan_intent = st.selectbox(
    "Loan Intent",
    [0, 1, 2, 3, 4, 5]
)

loan_grade = st.selectbox(
    "Loan Grade",
    [0, 1, 2, 3, 4, 5, 6]
)

cb_person_default_on_file = st.selectbox(
    "Previous Default",
    [0, 1]
)

if st.button("Predict Risk"):

    input_df = pd.DataFrame({
        'person_age':[person_age],
        'person_income':[person_income],
        'person_home_ownership':[person_home_ownership],
        'person_emp_length':[person_emp_length],
        'loan_intent':[loan_intent],
        'loan_grade':[loan_grade],
        'loan_amnt':[loan_amnt],
        'loan_int_rate':[loan_int_rate],
        'loan_percent_income':[loan_percent_income],
        'cb_person_default_on_file':[cb_person_default_on_file],
        'cb_person_cred_hist_length':[cb_person_cred_hist_length],
        'emp_length_missing':[0],
        'interest_rate_missing':[0]
    })

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("High Credit Risk")
    else:
        st.success("Low Credit Risk")
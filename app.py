import streamlit as st
import pandas as pd
import joblib

model = joblib.load("credit_risk_model.pkl")

st.set_page_config(page_title="Credit Risk Analytics", page_icon="💰", layout="centered")

st.title("💰 Credit Risk Analytics")
st.markdown("### Predict whether a loan applicant is likely to default")

st.info("""
**How to use this app:**
1. Fill in the applicant and loan details in the sidebar
2. Click Predict Risk button
3. Check the result below
""")

with st.sidebar:
    st.header("Applicant & Loan Details")
    
    st.subheader("Personal Information")
    person_age = st.number_input("Age (years)", min_value=18, max_value=100, value=30, help="Applicant's age")
    
    person_income = st.number_input("Annual Income ($)", min_value=0, value=60000, 
                                   help="Yearly income in USD")
    
    person_emp_length = st.number_input("Employment Length (years)", min_value=0, max_value=50, value=5,
                                       help="How many years in current job?")
    
    person_home_ownership = st.selectbox(
        "Home Ownership",
        ["RENT", "OWN", "MORTGAGE", "OTHER"],
        help="Current housing situation"
    )

    st.subheader("Loan Details")
    loan_amnt = st.number_input("Loan Amount ($)", min_value=0, value=10000, 
                               help="Amount of loan requested")
    
    loan_int_rate = st.number_input("Interest Rate (%)", min_value=0.0, max_value=30.0, value=11.0, 
                                   help="Interest rate on the loan")
    
    loan_percent_income = st.number_input("Loan Percent of Income", min_value=0.0, max_value=1.0, value=0.2,
                                         help="Loan amount as % of annual income (Lower is better)")
    
    loan_intent = st.selectbox(
        "Loan Intent (Purpose)",
        ["EDUCATION", "MEDICAL", "VENTURE", "PERSONAL", "HOMEIMPROVEMENT", "DEBTCONSOLIDATION"],
        help="""
        **Risk Guide:**
        - DEBTCONSOLIDATION & MEDICAL → Higher Risk
        - HOMEIMPROVEMENT → Lower Risk
        """
    )
    
    loan_grade = st.selectbox(
        "Loan Grade",
        ["A", "B", "C", "D", "E", "F", "G"],
        help="A = Lowest Risk | G = Highest Risk"
    )

    st.subheader("Credit History")
    cb_person_cred_hist_length = st.number_input("Credit History Length (years)", min_value=0, value=5,
                                                help="How long credit history exists")
    
    cb_person_default_on_file = st.selectbox(
        "Previous Default on File",
        ["No", "Yes"],
        help="Has the person defaulted before?"
    )

if st.button("🚀 Predict Risk", type="primary", use_container_width=True):
    
    home_ownership_map = {"RENT": 0, "OWN": 1, "MORTGAGE": 2, "OTHER": 3}
    loan_intent_map = {
        "EDUCATION": 0, "MEDICAL": 1, "VENTURE": 2, "PERSONAL": 3,
        "HOMEIMPROVEMENT": 4, "DEBTCONSOLIDATION": 5
    }
    loan_grade_map = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
    default_map = {"No": 0, "Yes": 1}

    input_df = pd.DataFrame({
        'person_age': [person_age],
        'person_income': [person_income],
        'person_home_ownership': [home_ownership_map[person_home_ownership]],
        'person_emp_length': [person_emp_length],
        'loan_intent': [loan_intent_map[loan_intent]],
        'loan_grade': [loan_grade_map[loan_grade]],
        'loan_amnt': [loan_amnt],
        'loan_int_rate': [loan_int_rate],
        'loan_percent_income': [loan_percent_income],
        'cb_person_default_on_file': [default_map[cb_person_default_on_file]],
        'cb_person_cred_hist_length': [cb_person_cred_hist_length],
        'emp_length_missing': [0],
        'interest_rate_missing': [0]
    })

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.subheader("Prediction Result")
    
    if probability >= 0.7:
        st.error(f"🔴 **HIGH RISK** (Default Probability: {probability:.1%})")
        st.warning("This applicant has a high chance of defaulting.")
    elif probability >= 0.4:
        st.warning(f"🟠 **MEDIUM RISK** (Default Probability: {probability:.1%})")
        st.info("This applicant has moderate risk. Review carefully.")
    else:
        st.success(f"🟢 **LOW RISK** (Default Probability: {probability:.1%})")
        st.success("This applicant appears to be a good candidate for the loan.")

    st.caption("Note: This is a prediction based on historical data. Always use human judgment for final decisions.")

else:
    st.info("👈 Fill the sidebar and click Predict Risk to get the result.")

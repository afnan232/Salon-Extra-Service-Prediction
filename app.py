"""
Simple Streamlit App
Salon Extra Service Prediction
"""

import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("best_model.joblib")

st.set_page_config(page_title="Salon Extra Service Prediction", page_icon="💇")

st.title("💇 Salon Extra Service Prediction")
st.write("Predict the probability that a customer will buy an extra service.")

st.markdown("---")

# Input form
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", min_value=18, max_value=70, value=30)
    visits = st.slider("Number of Previous Visits", min_value=1, max_value=25, value=5)
    bill_amount = st.number_input("Current Bill Amount ($)", min_value=20.0, max_value=500.0, value=120.0, step=5.0)

with col2:
    is_new = st.selectbox("Is New Customer?", options=["No", "Yes"])
    service_type = st.selectbox("Main Service Type", options=["Haircut", "Coloring", "Treatment"])
    time_of_day = st.selectbox("Time of Day", options=["Morning", "Evening"])

# Convert inputs
is_new_customer = 1 if is_new == "Yes" else 0

input_df = pd.DataFrame([{
    "Age": age,
    "Visits": visits,
    "Bill_Amount": bill_amount,
    "Is_New_Customer": is_new_customer,
    "Service_Type": service_type,
    "Time_of_Day": time_of_day
}])

st.markdown("---")

if st.button("Predict", type="primary"):
    probability = model.predict_proba(input_df)[0][1]
    prediction = "Yes" if probability >= 0.5 else "No"

    st.subheader("Result")
    st.metric(label="Probability of Buying Extra Service", value=f"{probability*100:.1f}%")
    
    if prediction == "Yes":
        st.success(f"Prediction: **{prediction}** — Customer is likely to buy an extra service.")
    else:
        st.info(f"Prediction: **{prediction}** — Customer is less likely to buy an extra service.")

    st.caption("Threshold used: 0.50")

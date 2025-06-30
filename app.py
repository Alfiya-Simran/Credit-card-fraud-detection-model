import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model (make sure it's in the same directory)
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("💳 Credit Card Fraud Detection App")

st.markdown("Enter transaction details or upload a CSV file to predict fraud.")

# Option 1: Upload a CSV
uploaded_file = st.file_uploader("Upload transaction data (.csv)", type="csv")

if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
    prediction = model.predict(input_df)
    st.write("### 🔍 Prediction Results:")
    st.write(pd.DataFrame({"Fraud (1=yes)": prediction}))
else:
    st.write("Or, manually input transaction data below:")

    # Option 2: Manual input
    features = [f"V{i}" for i in range(1, 29)] + ["Amount"]
    user_input = []

    for feature in features:
        val = st.number_input(f"{feature}", value=0.0)
        user_input.append(val)

    if st.button("Detect Fraud"):
        input_array = np.array(user_input).reshape(1, -1)
        result = model.predict(input_array)[0]
        prob = model.predict_proba(input_array)[0][1]
        st.success(f"Prediction: {'Fraud' if result == 1 else 'Legit'} (Confidence: {prob:.2f})")
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

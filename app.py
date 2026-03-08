import streamlit as st
import pandas as pd
import pickle
import os
import requests

# URLs of your files in GitHub
MODEL_URL = "https://raw.githubusercontent.com/bais05/Crop-Yield-Prediction/main/dt.pkl"
PREPROCESSOR_URL = "https://raw.githubusercontent.com/bais05/Crop-Yield-Prediction/main/preprocessor.pkl"

# download if missing
if not os.path.exists("dt.pkl"):
    with open("dt.pkl", "wb") as f:
        f.write(requests.get(MODEL_URL).content)

if not os.path.exists("preprocessor.pkl"):
    with open("preprocessor.pkl", "wb") as f:
        f.write(requests.get(PREPROCESSOR_URL).content)

# load files
with open("dt.pkl", "rb") as f:
    model = pickle.load(f)
with open("preprocessor.pkl", "rb") as f:
    preprocessor = pickle.load(f)

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="Crop Yield Prediction")

st.title("🌾 Crop Yield Prediction System")
st.write("Enter the following agricultural parameters to predict crop yield")
st.markdown("---")

# User Inputs
year = st.number_input("Year", 1990, 2030)
rainfall = st.number_input("Average Rainfall (mm per year)")
pesticides = st.number_input("Pesticides Tonnes")
temperature = st.number_input("Average Temperature")
area = st.text_input("Area (Country)").title()
item = st.text_input("Crop Item").title()

st.markdown("---")

# Prediction button
if st.button("Predict Yield"):
    input_df = pd.DataFrame(
        [[year, rainfall, pesticides, temperature, area, item]],
        columns=[
            "Year",
            "average_rain_fall_mm_per_year",
            "pesticides_tonnes",
            "avg_temp",
            "Area",
            "Item",
        ],
    )

    transformed = preprocessor.transform(input_df)
    prediction = model.predict(transformed)

    st.success(f"Predicted Crop Yield: {prediction[0]}")
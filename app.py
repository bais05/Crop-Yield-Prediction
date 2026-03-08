import streamlit as st
import pandas as pd
import pickle
import os

# ----------------------------
# Deployment-safe paths
# ----------------------------
BASE_DIR = os.path.dirname(__file__)  # directory of app.py
model_path = os.path.join(BASE_DIR, "dt.pkl")
preprocessor_path = os.path.join(BASE_DIR, "preprocessor.pkl")

# ----------------------------
# Load files safely
# ----------------------------
with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(preprocessor_path, "rb") as f:
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
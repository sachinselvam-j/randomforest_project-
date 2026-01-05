import streamlit as st
import numpy as np
import pickle
import os

st.set_page_config(page_title="River Nutrient Prediction")

st.title("🌊 Dissolved Inorganic Nitrogen Prediction")

# ================= MODEL LOADING =================
MODEL_PATH = "random_forest_model.pkl"

if not os.path.exists(MODEL_PATH):
    st.error("❌ Model file not found!")
    st.stop()

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    st.success("✅ Model loaded successfully")
except Exception as e:
    st.error("❌ Error loading model")
    st.exception(e)
    st.stop()

st.divider()

# ================= INPUTS =================
region = st.number_input("Region Code", min_value=0, step=1)
conductivity = st.number_input("Water Electrical Conductivity", min_value=0.0)
ph = st.number_input("Water pH", min_value=0.0, max_value=14.0)
phosphorus = st.number_input("Dissolved Inorganic Phosphorus", min_value=0.0)

# ================= PREDICTION =================
if st.button("🔍 Predict"):
    try:
        input_data = np.array([[region, conductivity, ph, phosphorus]])
        prediction = model.predict(input_data)
        st.success(f"✅ Predicted Value: {prediction[0]:.2f}")
    except Exception as e:
        st.error("❌ Prediction failed")
        st.exception(e)

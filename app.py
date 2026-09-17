import streamlit as st
import requests
import joblib

scaler = joblib.load("rscaler_v1.pkl")
feature_names = list(scaler.feature_names_in_)

# Default values — pulled from a real malignant sample
default_values = {
    "radius_mean": 17.99, "texture_mean": 10.38, "perimeter_mean": 122.8, "area_mean": 1001.0,
    "smoothness_mean": 0.1184, "compactness_mean": 0.2776, "concavity_mean": 0.3001,
    "concave points_mean": 0.1471, "symmetry_mean": 0.2419, "fractal_dimension_mean": 0.07871,
    "radius_se": 1.095, "texture_se": 0.9053, "perimeter_se": 8.589, "area_se": 153.4,
    "smoothness_se": 0.006399, "compactness_se": 0.04904, "concavity_se": 0.05373,
    "concave points_se": 0.01587, "symmetry_se": 0.03003, "fractal_dimension_se": 0.006193,
    "radius_worst": 25.38, "texture_worst": 17.33, "perimeter_worst": 184.6, "area_worst": 2019.0,
    "smoothness_worst": 0.1622, "compactness_worst": 0.6656, "concavity_worst": 0.7119,
    "concave points_worst": 0.2654, "symmetry_worst": 0.4601, "fractal_dimension_worst": 0.1189,
    "perimeter_area_ratio": 15.06, "concavity_score": 0.0442, "size_deviation": 1018.0
}

st.title("Cancer Cell Prediction")
st.write("Enter the tumor cell measurements:")

API_URL = "http://65.1.248.79:8000/predict"

input_data = {}
for feature in feature_names:
    input_data[feature] = st.number_input(
        feature,
        value=default_values.get(feature, 0.0),
        format="%.5f"
    )

if st.button("Predict"):
    response = requests.post(API_URL, json={"features": input_data})
    if response.status_code == 200:
        result = response.json()
        if "error" in result:
            st.error(result["error"])
        else:
            label_map = {"M": "Malignant (Cancerous)", "B": "Benign (Non-cancerous)"}
            readable_result = label_map.get(result["prediction"], result["prediction"])

            st.subheader(f"Prediction: {readable_result}")
            st.write(f"Confidence: {result['confidence']*100:.2f}%")
    else:
        st.error("Something went wrong contacting the API.")
        
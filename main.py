from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Cancer Prediction API")

model = joblib.load("model_v1.pkl")
scaler = joblib.load("rscaler_v1.pkl")
le = joblib.load("label_encoder_v1.pkl")

class TumorInput(BaseModel):
    features: dict[str, float]

@app.get("/")
def home():
    return {"message": "Cancer Prediction API is running"}

@app.post("/predict")
def predict(data: TumorInput):
    try:
        input_df = pd.DataFrame([data.features])
        input_df = input_df[scaler.feature_names_in_]
        scaled_input = scaler.transform(input_df)

        prediction = model.predict(scaled_input)[0]
        probability = model.predict_proba(scaled_input)[0][prediction]
        result = le.inverse_transform([prediction])[0]

        return {
            "prediction": str(result),
            "confidence": round(float(probability), 4)
        }
    except Exception as e:
        return {"error": str(e)}
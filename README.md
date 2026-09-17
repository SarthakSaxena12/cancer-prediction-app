# Cancer Cell Prediction — ML Pipeline + Deployment

Predicts whether a tumor is malignant or benign using cell nuclei measurements, 
built as part of CCC's ML Task 3.

## Live Links
- **API (FastAPI)**: http://65.1.248.79:8000/docs
- **Frontend (Streamlit)**: Coming Soon

## Project Structure
- `Cancer.ipynb` — full pipeline: EDA, feature engineering, model training, evaluation
- `main.py` — FastAPI backend serving the trained model
- `app.py` — Streamlit frontend
- `model_v1.pkl`, `rscaler_v1.pkl`, `label_encoder_v1.pkl` — saved model artifacts
- `Dockerfile` — containerizes the FastAPI backend

## Dataset
Breast Cancer Wisconsin (Diagnostic) Dataset — 569 samples, 30 features (radius, 
texture, perimeter, area, concavity, etc.) plus 3 engineered features.

## Models Compared
Logistic Regression, Random Forest, SVM, Decision Tree — tuned via GridSearchCV. 
Final model: **Logistic Regression** (98.2% accuracy, 100% recall after tuning).

## Run Locally
\`\`\`bash
pip install -r requirements.txt
uvicorn main:app --reload        # backend
streamlit run app.py             # frontend, separate terminal
\`\`\`

## Deployment
Model containerized with Docker, pushed to DockerHub, deployed on AWS EC2.

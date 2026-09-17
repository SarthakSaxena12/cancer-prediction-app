# Cancer Prediction App

A machine learning-powered web app that predicts whether a breast tumor is malignant or benign based on cell nucleus measurements. This project was built as part of CCC's ML Task 3 and includes a trained model, a FastAPI backend, and a Streamlit frontend.

## Live Applications
- API (FastAPI Swagger UI): http://65.1.248.79:8000/docs
- Frontend (Streamlit): https://cancer-prediction-app-25vi8makvzmxzbgaswugi4.streamlit.app/

## Overview
The project uses the Breast Cancer Wisconsin (Diagnostic) dataset to train a classification model that predicts tumor status from 30 diagnostic features, including:
- radius
- texture
- perimeter
- area
- concavity
- smoothness
- and other cell nucleus measurements

The app is designed to demonstrate a complete ML workflow:
- data exploration and preprocessing
- feature engineering
- model comparison and tuning
- model selection and evaluation
- deployment via Docker and cloud hosting

## Project Structure
- `Cancer.ipynb` — end-to-end ML pipeline, including EDA, preprocessing, feature engineering, model training, and evaluation
- `main.py` — FastAPI backend that loads the trained model and provides prediction endpoints
- `app.py` — Streamlit user interface for interacting with the model
- `model_v1.pkl` — trained Logistic Regression model
- `rscaler_v1.pkl` — saved scaler used during preprocessing
- `label_encoder_v1.pkl` — saved label encoder for class mapping
- `requirements.txt` — Python dependencies
- `Dockerfile` — containerizes the backend service

## Dataset
Dataset used: Breast Cancer Wisconsin (Diagnostic) Dataset
- 569 samples
- 30 original feature columns
- 3 engineered features added during preprocessing
- target classes: malignant vs benign

## Modeling Approach
Several models were compared and tuned using GridSearchCV:
- Logistic Regression
- Random Forest
- SVM
- Decision Tree

The final selected model is: Logistic Regression
- Accuracy: 98.2%
- Recall: 100% after tuning

This model was chosen because it delivered the best balance between accuracy and reliability for the classification task.

## Local Setup
### 1) Clone the repository
```bash
git clone https://github.com/SarthakSaxena12/cancer-prediction-app.git
cd cancer-prediction-app
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Run the backend
```bash
uvicorn main:app --reload
```
The API will be available at:
- http://127.0.0.1:8000
- Swagger docs: http://127.0.0.1:8000/docs

### 4) Run the frontend
Open a second terminal and execute:
```bash
streamlit run app.py
```
The app should open in your browser on the local Streamlit port.

## Deployment
The trained model and backend were containerized with Docker and deployed using AWS EC2. The API is also exposed through a public endpoint for quick testing and demonstration.

## Example Usage
Once the backend is running, the FastAPI docs provide a simple interactive interface for sending sample tumor measurements and receiving predictions.

## Notes
This project demonstrates a full machine learning deployment workflow—from notebook experimentation to a functional web application deployed in a real environment.

## Future Improvements
- add automated CI/CD for model and deployment validation
- improve model monitoring and retraining pipeline
- add more robust input validation and error handling
- enhance the frontend with charts and confidence scores

---

Built with Python, Scikit-learn, FastAPI, Streamlit, Docker, and AWS.

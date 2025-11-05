"""
AI-Driven Customer Churn Prediction - FastAPI REST API
Author: Akshat
Project: AI + DevOps Integration for Telecom Industry (IA-2)
Description: REST API endpoint for real-time churn prediction using trained CatBoost model
"""

import uvicorn
import pandas as pd
from fastapi import FastAPI
from catboost import CatBoostClassifier

# Path to the model
MODEL_PATH = "../model/cat_model.cbm" 

# Function to load the trained model
def load_model():
    model = CatBoostClassifier()
    model.load_model(MODEL_PATH)
    return model

# Function to predict churn probability from data in DataFrame format
def get_churn_probability(data, model):
    # Convert incoming data into a DataFrame
    dataframe = pd.DataFrame.from_dict(data, orient='index').T
    # Make the prediction
    churn_probability = model.predict_proba(dataframe)[0][1]
    return churn_probability

# Load the model
model = load_model()

# Create the FastAPI application
app = FastAPI(title="Churn Prediction API", version="1.0")

@app.get('/')
def index():
    return {'message': 'CHURN Prediction API'}

# Define the API endpoint
@app.post('/predict/')
def predict_churn(data: dict):
    # Get the prediction
    churn_probability = get_churn_probability(data, model)
    # Return the prediction
    return {'Churn Probability': churn_probability}

# Run the application
if __name__ == '__main__':
    uvicorn.run("fast_api:app", host='0.0.0.0', port=8000)

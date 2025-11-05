"""
AI-Driven Customer Churn Prediction - Streamlit Web Interface
Author: Akshat
Project: AI + DevOps Integration for Telecom Industry (IA-2)
Description: Interactive web app for churn prediction in Indian Rupees
"""

import os
import pandas as pd
import numpy as np
import streamlit as st
from catboost import CatBoostClassifier

# Get the directory of the current script and construct model path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
MODEL_PATH = os.path.join(PROJECT_ROOT, "model", "cat_model.cbm")

st.set_page_config(
    page_title="AI Churn Prediction",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_resource
def load_model():
    """Load the pre-trained CatBoost model"""
    model = CatBoostClassifier()
    model.load_model(MODEL_PATH)
    return model

st.title("🎯 AI-Driven Customer Churn Prediction")
st.markdown("**Developed by Akshat** | Indian Telecom Industry | AI + DevOps Project (IA-2)")
st.markdown("---")

model = load_model()

tab1, tab2 = st.tabs(["📈 Predict Churn", "📋 About"])

with tab1:
    st.header("Customer Churn Prediction")
    st.write("Enter customer information to predict churn probability (All prices in ₹ - Indian Rupees)")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Demographics")
        gender = st.selectbox("Gender", ["Male", "Female"], key="gender")
        senior_citizen = st.selectbox("Senior Citizen", ["No", "Yes"], key="senior")
        partner = st.selectbox("Partner", ["Yes", "No"], key="partner")
        dependents = st.selectbox("Dependents", ["Yes", "No"], key="dependents")
    
    with col2:
        st.subheader("Account Information")
        tenure = st.slider("Tenure (months)", 0, 72, 12)
        contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"], key="contract")
        paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"], key="paperless")
        payment_method = st.selectbox(
            "Payment Method",
            ["Electronic check", "Mailed check", "Bank transfer", "Credit card"],
            key="payment"
        )
    
    with col3:
        st.subheader("Charges (in ₹)")
        monthly_charges = st.number_input("Monthly Charges (₹)", min_value=0.0, max_value=15000.0, value=5200.0, step=1.0)
        total_charges = st.number_input("Total Charges (₹)", min_value=0.0, max_value=800000.0, value=80000.0, step=100.0)
    
    st.markdown("---")
    
    col4, col5 = st.columns(2)
    
    with col4:
        st.subheader("Phone & Internet Services")
        phone_service = st.selectbox("Phone Service", ["Yes", "No"], key="phone")
        multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"], key="lines")
        internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"], key="internet")
    
    with col5:
        st.subheader("Online Services")
        online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"], key="security")
        online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"], key="backup")
        device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"], key="device")
        tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"], key="tech")
        streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"], key="tv")
        streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"], key="movies")
    
    st.markdown("---")
    
    if st.button("🔮 Predict Churn Probability", use_container_width=True, type="primary"):
        customer_data = pd.DataFrame({
            "customerID": ["PREDICTION-001"],
            "gender": [gender],
            "SeniorCitizen": [1 if senior_citizen == "Yes" else 0],
            "Partner": [partner],
            "Dependents": [dependents],
            "tenure": [tenure],
            "PhoneService": [phone_service],
            "MultipleLines": [multiple_lines],
            "InternetService": [internet_service],
            "OnlineSecurity": [online_security],
            "OnlineBackup": [online_backup],
            "DeviceProtection": [device_protection],
            "TechSupport": [tech_support],
            "StreamingTV": [streaming_tv],
            "StreamingMovies": [streaming_movies],
            "Contract": [contract],
            "PaperlessBilling": [paperless_billing],
            "PaymentMethod": [payment_method],
            "MonthlyCharges": [monthly_charges],
            "TotalCharges": [total_charges]
        })
        
        try:
            churn_probability = model.predict_proba(customer_data)[:, 1][0]
            
            st.markdown("---")
            st.markdown("## 📊 Prediction Results")
            
            col_result1, col_result2 = st.columns(2)
            
            with col_result1:
                if churn_probability > 0.7:
                    color = "🔴"
                    status = "HIGH RISK"
                elif churn_probability > 0.4:
                    color = "🟡"
                    status = "MEDIUM RISK"
                else:
                    color = "🟢"
                    status = "LOW RISK"
                
                st.metric(
                    label="Churn Probability",
                    value=f"{churn_probability:.1%}",
                    delta=status
                )
            
            with col_result2:
                st.info(f"{color} **Status**: {status}")
            
            st.progress(churn_probability)
            
            st.markdown("### 📌 Insights")
            
            if churn_probability > 0.7:
                st.warning(
                    "⚠️ This customer has a **HIGH RISK** of churning. "
                    "Consider offering retention strategies such as discounts, "
                    "loyalty programs, or premium support."
                )
            elif churn_probability > 0.4:
                st.info(
                    "📊 This customer has a **MEDIUM RISK** of churning. "
                    "Monitor their account and consider proactive engagement."
                )
            else:
                st.success(
                    "✅ This customer has a **LOW RISK** of churning. "
                    "They appear to be a loyal customer."
                )
            
            st.markdown("### 👤 Customer Profile")
            profile_col1, profile_col2, profile_col3 = st.columns(3)
            
            with profile_col1:
                st.write(f"**Gender**: {gender}")
                st.write(f"**Senior Citizen**: {senior_citizen}")
                st.write(f"**Partner**: {partner}")
            
            with profile_col2:
                st.write(f"**Tenure**: {tenure} months")
                st.write(f"**Contract**: {contract}")
                st.write(f"**Monthly Charges**: ₹{monthly_charges:.2f}")
            
            with profile_col3:
                st.write(f"**Total Charges**: ₹{total_charges:.2f}")
                st.write(f"**Internet Service**: {internet_service}")
                st.write(f"**Phone Service**: {phone_service}")
        
        except Exception as e:
            st.error(f"❌ Error making prediction: {str(e)}")

with tab2:
    st.header("About This Project")
    
    st.markdown("""
    ### 🎯 Project Overview
    This AI-Driven Customer Churn Prediction system uses machine learning to identify customers 
    at risk of leaving a telecommunications company. The model helps businesses implement 
    targeted retention strategies.
    
    ### 🧠 Machine Learning Model
    - **Algorithm**: CatBoost Classifier
    - **Training Data**: 7,043 customers
    - **Features**: 19 customer attributes
    - **Performance**: ~80% Accuracy with high recall
    
    ### 📊 Key Features
    - **Real-time Predictions**: Get instant churn probability scores
    - **Customer Profiles**: Analyze demographics and service usage
    - **Risk Assessment**: Automatic risk classification (High/Medium/Low)
    - **Indian Currency**: All prices displayed in Indian Rupees (₹)
    - **Production-Ready**: Deployed via FastAPI, Docker, and CI/CD
    
    ### 🚀 Technology Stack
    - **ML Framework**: CatBoost, Scikit-learn
    - **Web Interface**: Streamlit
    - **API**: FastAPI
    - **Containerization**: Docker
    - **CI/CD**: GitHub Actions
    - **Currency**: Indian Rupees (₹)
    
    ### 👤 Author
    **Akshat**  
    *AI + DevOps Integration Project (IA-2)*  
    *Telecom Industry Customer Churn Prediction*
    
    ### 📚 How to Use
    1. Navigate to the **"Predict Churn"** tab
    2. Enter customer information
    3. Click **"Predict Churn Probability"**
    4. View the prediction results and recommendations
    
    ### 🔗 API Endpoint
    The same model is available via REST API at:
    ```
    POST http://localhost:8000/predict/
    ```
    
    Access API documentation: [Swagger UI](http://localhost:8000/docs)
    
    ### 💱 Currency Information
    All charges are displayed in **Indian Rupees (₹)**.
    """)
    
    st.markdown("---")
    st.info("🎓 Developed for academic purposes as part of IA-2 coursework | Indian Telecom Industry")

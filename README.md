# AI-Driven Customer Churn Prediction using DevOps Automation

# Telco Customer Churn Project

**Developed by Akshat — AI + DevOps Project for Telecom Industry (IA-2)**

This project is a machine learning project focusing on customer churn prediction. The project consists of 4 main steps: 

## 📋 Project Overview- Data Preprocessing and Model Development (CatBoost)

- Interface (Streamlit)

This project demonstrates an end-to-end AI-powered customer churn prediction system for the telecommunications industry, integrated with modern DevOps practices. The system predicts whether a customer will churn (leave the service) based on their demographics, account information, and service usage patterns.- API (FastAPI)

- Automation (Docker)

### 🎯 Key Features

- **Machine Learning**: CatBoost classifier for accurate churn prediction(You can also take a look at the [Medium](https://medium.com/@ramazanolmeez/end-to-end-machine-learning-project-churn-prediction-e9c4d0322ac9) article that hosts all the processes of the project)

- **REST API**: FastAPI endpoint for real-time predictions

- **Interactive UI**: Streamlit web application with model explainability (SHAP)## Project Folder Structure

- **Containerization**: Docker for consistent deployment```bash

- **CI/CD Pipeline**: GitHub Actions for automated build, test, and deploymentTelco Customer Churn Project/

│

---├── data/

│   ├── churn_data_regulated.parquet

## 🏗️ Architecture│   ├── WA_Fn-UseC_-Telco-Customer-Churn.csv

│   ├── ...

```│

Data Pipeline → Model Training → Prediction Services → Containerization → CI/CD → Deployment├── model/

```│   └── cat_model.cbm

│

### Pipeline Flow:├── notebooks/

1. **Data Ingestion**: Load Telco customer data (CSV)│   ├── telco-customer-churn-eda.ipynb

2. **Model Training**: Train CatBoost classifier with preprocessed data│   ├── telco-catboost-xgboost-shap-lime.ipynb

3. **API Service**: FastAPI serves predictions via REST endpoint│

4. **Web Interface**: Streamlit app for interactive predictions and SHAP analysis├── src/

5. **Dockerization**: Containerize the application│   ├── fast-api.py

6. **Automation**: GitHub Actions CI/CD pipeline│   ├── predict.py

7. **Deployment**: Deploy to cloud platforms (Render, Railway, AWS, etc.)│   ├── streamlit-app.py

│   └── train_model.py

---│

└── Dockerfile

## 📂 Project Structure└── requirements.txt

```

```

AI-Driven-Telco-Churn/## Project Files

│

├── data/- **data/**: Contains the data files used for the project.

│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv  # Customer dataset- **model/**: Contains the trained model file.

│- **notebooks/**: Includes Jupyter Notebooks used for data analysis and model development.

├── src/- **src/**: Contains the source code of the project. Model training, prediction and service/application development are located in this folder.

│   ├── train_model.py         # Model training script

│   ├── fast-api.py            # FastAPI REST API## Steps

│   ├── streamlit-app.py       # Streamlit web interface1. **Data Preprocessing and Model Development**: Using the script `train_model.py`, Telco Customer data is preprocessed and a machine learning model is created using the CatBoost model.

│   └── predict.py             # CLI prediction tool2. **Interface**: Using the model, the `streamlit-app.py` script allows the user to enter new customer information and based on this information the churn probability is estimated. Furthermore, the overall SHAP graph of the model and the specific SHAP graph of the selected customer are shown.

│3. **API**: The `fast-api.py` script creates an API using the model created with train_model.py. This API takes customer data and returns the churn probability.

├── model/4. **Automation**: Using Docker, the project is containerized and made executable through the `predict.py` script. This script takes customer data and calculates the churn probability.

│   └── cat_model.cbm          # Trained CatBoost model

│

├── .github/## Usage

│   └── workflows/

│       └── devops.yml         # CI/CD pipeline configuration### 

│1. Clone the project

├── Dockerfile                 # Container configuration```bash

├── requirements.txt           # Python dependenciesgit clone https://github.com/rolmez/Customer-Churn-Project.git

└── README.md                  # Project documentation```

```2. Go to the project directory

```bash

---cd Customer-Churn-Project

```

## 🚀 Getting Started3. Install dependencies

```bash

### Prerequisitespip install requirements.txt

- Python 3.9+```

- Docker (optional, for containerization)4. Go to the src directory

- Git```bash

cd src

### Installation```

- For train model

1. **Clone the repository**```bash

   ```bashpython train_model.py

   git clone https://github.com/yourusername/AI-Driven-Telco-Churn.git```

   cd AI-Driven-Telco-Churn- For Streamlit app

   ``````bash

streamlit run streamlit-app.py

2. **Install dependencies**```

   ```bash- For API

   pip install -r requirements.txt```bash

   ```python fast-api.py

```

3. **Train the model**- For predict

   ```bash```bash

   cd srcpython predict.py

   python train_model.py```

   ```### or Docker

   This generates `model/cat_model.cbm`1. Run the following command to create the Docker container in the project's home folder:

```bash

---  docker build -t telco-churn .

```

## 💻 Usage2. Run the following command to start the Docker container:

```bash

### Option 1: FastAPI (REST API)  docker run -it telco-churn

```

Start the API server:

```bash## Some images from the project

cd src### Streamlit

uvicorn fast-api:app --host 0.0.0.0 --port 8000 --reload![Streamlit Overview](photos/streamlit%201.png)

```![Actual-Prediction](photos/streamlit%202.png)

![SHAP](photos/streamlit%203.png)

Access the API:![SHAP 2](photos/streamlit%204.png)

- **Interactive Docs**: http://localhost:8000/docs### API

- **API Endpoint**: POST to http://localhost:8000/predict/![FastAPI](photos/fast-api%202.png)

![FastAPI](photos/fast-api%203.png)

Example request:![FastAPI](photos/fast-api%204.png)

```bash### Docker

curl -X POST "http://localhost:8000/predict/" \![Docker Run](photos/docker%20run.png)
  -H "Content-Type: application/json" \
  -d '{
    "customerID": "1234-ABCD",
    "gender": "Male",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 12,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "Yes",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 85.50,
    "TotalCharges": 1025.00
  }'
```

### Option 2: Streamlit Web App

Launch the interactive interface:
```bash
cd src
streamlit run streamlit-app.py
```

Access at: http://localhost:8501

**Features**:
- Calculate churn probability for new customers
- View feature importance (SHAP values)
- Analyze individual customer predictions with waterfall plots

### Option 3: Command Line Interface

Run predictions via CLI:
```bash
cd src
python predict.py
```
Follow the prompts to enter customer information.

---

## 🐳 Docker Deployment

### Build the Docker image
```bash
docker build -t telco-churn-api .
```

### Run the container
```bash
docker run -d -p 8000:8000 telco-churn-api
```

The API will be available at: http://localhost:8000

---

## 🔄 CI/CD Pipeline

The project includes a GitHub Actions workflow (`.github/workflows/devops.yml`) that automates:

1. **Build**: Install dependencies and validate code
2. **Test**: Run model training and verify predictions
3. **Dockerize**: Build and tag Docker image
4. **Push**: Upload image to Docker Hub / Container Registry
5. **Deploy**: Trigger deployment to cloud platform

### Setup Instructions:

1. Add secrets to your GitHub repository:
   - `DOCKER_USERNAME`: Your Docker Hub username
   - `DOCKER_PASSWORD`: Your Docker Hub password

2. Push code to trigger the pipeline:
   ```bash
   git add .
   git commit -m "Deploy AI churn prediction system"
   git push origin main
   ```

---

## 📊 Dataset Information

**Source**: Telco Customer Churn Dataset  
**Records**: 7,043 customers  
**Features**: 19 attributes + 1 target (Churn)

### Key Features:
- **Demographics**: Gender, Senior Citizen, Partner, Dependents
- **Account**: Tenure, Contract Type, Payment Method, Billing
- **Services**: Phone, Internet, Security, Backup, Streaming
- **Charges**: Monthly Charges, Total Charges
- **Target**: Churn (Yes/No)

---

## 🧠 Model Details

- **Algorithm**: CatBoost Classifier
- **Why CatBoost?**
  - Handles categorical features natively
  - High accuracy with minimal tuning
  - Built-in support for class imbalance
- **Training Split**: 80/20 stratified split
- **Evaluation Metrics**: Accuracy, Recall, Precision, ROC-AUC

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| **ML Framework** | CatBoost, Scikit-learn |
| **API Framework** | FastAPI |
| **Web Interface** | Streamlit |
| **Explainability** | SHAP |
| **Containerization** | Docker |
| **CI/CD** | GitHub Actions |
| **Deployment** | Render / Railway / AWS |
| **Language** | Python 3.9+ |

---

## 📈 Performance Metrics

The CatBoost model achieves:
- **Accuracy**: ~80%
- **Recall**: High (focus on identifying churners)
- **Precision**: Balanced for business use case
- **ROC-AUC**: >0.85

*(Metrics may vary based on training data split)*

---

## 🚢 Deployment Options

### Cloud Platforms:
1. **Render**: Connect GitHub repo, auto-deploy from `main` branch
2. **Railway**: One-click Docker deployment
3. **AWS ECS/Fargate**: Production-grade container orchestration
4. **Heroku**: Simple push-to-deploy workflow
5. **Azure App Service**: Enterprise deployment

---

## 🔮 Future Enhancements

- [ ] Add real-time data streaming pipeline
- [ ] Implement A/B testing framework
- [ ] Create customer segmentation module
- [ ] Add monitoring and alerting (Prometheus/Grafana)
- [ ] Integrate with CRM systems
- [ ] Deploy on Kubernetes for scalability

---

## 📄 License

This project is developed for academic purposes as part of IA-2 coursework.

---

## 👤 Author

**Akshat**  
*AI + DevOps Integration Project*  
*Telecom Industry Customer Churn Prediction*

---

## 🤝 Acknowledgments

- Dataset source: IBM Sample Data Sets
- Inspired by real-world telecom churn analysis
- Built with modern MLOps best practices

---

**⭐ If you found this project helpful, please star the repository!**

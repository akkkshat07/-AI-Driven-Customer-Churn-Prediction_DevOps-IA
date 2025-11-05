#!/bin/bash

# AI-Driven Customer Churn Prediction - Quick Start Script
# Author: Akshat | AI + DevOps Project (IA-2)

echo "========================================"
echo "AI-Driven Customer Churn Prediction"
echo "Quick Start Script"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.9+ first."
    exit 1
fi

echo "✓ Python found: $(python3 --version)"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

echo ""
echo "========================================"
echo "What would you like to do?"
echo "========================================"
echo "1) Train the model"
echo "2) Run FastAPI server"
echo "3) Run Streamlit app"
echo "4) Run CLI prediction tool"
echo "5) Build Docker image"
echo "========================================"
read -p "Enter your choice (1-5): " choice

case $choice in
    1)
        echo "🤖 Training model..."
        cd src && python3 train_model.py
        ;;
    2)
        echo "🚀 Starting FastAPI server..."
        echo "API will be available at: http://localhost:8000"
        echo "Docs available at: http://localhost:8000/docs"
        cd src && uvicorn fast-api:app --host 0.0.0.0 --port 8000 --reload
        ;;
    3)
        echo "🌐 Starting Streamlit app..."
        echo "App will open in your browser at: http://localhost:8501"
        cd src && streamlit run streamlit-app.py
        ;;
    4)
        echo "💻 Running CLI prediction tool..."
        cd src && python3 predict.py
        ;;
    5)
        echo "🐳 Building Docker image..."
        docker build -t telco-churn-api .
        echo "✓ Docker image built successfully!"
        echo "Run with: docker run -d -p 8000:8000 telco-churn-api"
        ;;
    *)
        echo "❌ Invalid choice. Please run the script again."
        exit 1
        ;;
esac

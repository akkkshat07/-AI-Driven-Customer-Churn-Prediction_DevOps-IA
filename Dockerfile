# AI-Driven Customer Churn Prediction - Docker Configuration
# Author: Akshat | AI + DevOps Project (IA-2)

# Use a Python-based image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port for FastAPI
EXPOSE 8000

# Run FastAPI application with uvicorn
CMD ["uvicorn", "src.fast-api:app", "--host", "0.0.0.0", "--port", "8000"]

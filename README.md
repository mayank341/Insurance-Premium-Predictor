# Insurance-Premium-Predictor


A Machine Learning-powered Insurance Premium Prediction API built using FastAPI, Scikit-Learn, and XGBoost.

## Overview

This project predicts the insurance premium of a customer based on personal and health-related information such as:

* Age
* Gender
* BMI
* Number of Children
* Smoking Status
* Region

The model is trained on an insurance dataset and exposed through a FastAPI REST API.

---

## Features

* Insurance premium prediction using Machine Learning
* Feature engineering for BMI categories
* Risk assessment based on smoking and BMI
* FastAPI backend with interactive Swagger documentation
* Model persistence using Pickle
* JSON-based API requests and responses

---

## Tech Stack

* Python 3.12+
* FastAPI
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Uvicorn

---

## Project Structure

```text
Insurance-Premium-Predictor/
│
├── insurance.py
├── insurance_premium.pkl
├── insurance_dataset.csv
├── model_training.ipynb
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Insurance-Premium-Predictor.git
cd Insurance-Premium-Predictor
```

### Create Virtual Environment

```bash
python -m venv myenv
```

### Activate Environment

Windows:

```bash
myenv\Scripts\activate
```

Linux / macOS:

```bash
source myenv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the API

Start the FastAPI server:

```bash
uvicorn insurance:app --reload
```

Server will run on:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### POST /predict

Predicts the insurance premium.

#### Request Body

```json
{
  "age": 50,
  "sex": "male",
  "bmi": 30,
  "children": 1,
  "smoker": "yes",
  "region": "northwest"
}
```

#### Response

```json
{
  "predicted_premium": 8775.63,
  "risk_score": 4.87,
  "health_risk": "Low"
}
```

---

## Feature Engineering

### BMI Category

| BMI Range   | Category    |
| ----------- | ----------- |
| < 18.5      | Underweight |
| 18.5 - 24.9 | Normal      |
| 25 - 29.9   | Overweight  |
| >= 30       | Obese       |

### Smoking Risk

* High
* Medium
* Low

Derived using BMI and smoking status.

---

## Model Information

Algorithm Used:

* XGBoost Regressor

Evaluation Metrics:

* Mean Absolute Percentage Error (MAPE)
* Root Mean Squared Error (RMSE)

The trained model is stored as:

```text
insurance_premium.pkl
```

---

## Future Improvements

* Multi-model architecture
* Health risk classification
* Risk score prediction model
* Docker deployment
* Cloud deployment (AWS/Azure/GCP)
* Frontend dashboard integration

---

## Author

Mayank Kumar

Built using FastAPI, Machine Learning, and XGBoost.

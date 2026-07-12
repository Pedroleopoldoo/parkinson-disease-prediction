# Project Roadmap

This document outlines the planned development stages for the Parkinson Disease Prediction project.

---

# 1. Exploratory Data Analysis (EDA)

## Objectives

- Understand the dataset
- Inspect data types and distributions
- Identify missing values
- Detect outliers
- Build histograms
- Analyze feature correlations
- Document key insights

## Status

✅ Completed

---

# 2. Feature Engineering

## Objectives

- Data cleaning
- Data type conversion
- Feature scaling
- Feature selection
- Handle multicollinearity
- Prepare the dataset for machine learning

## Status

⬜ Not Started

---

# 3. Machine Learning (Scikit-Learn)

## Objectives

Train and compare multiple regression models:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor
- Support Vector Regressor (SVR)
- XGBoost (optional)

Evaluate using:

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

## Status

⬜ Not Started

---

# 4. Machine Learning (PyTorch)

## Objectives

Build a neural network for regression.

### Planned Steps

- Custom Dataset
- DataLoader
- Neural Network Architecture
- Model Training
- Model Evaluation

Compare the results against Scikit-Learn models.

## Status

⬜ Not Started

---

# 5. Database

## Objectives

Store and manage the dataset using a relational database.

### Technologies

- SQLite
- PostgreSQL (optional)

### Tasks

- Database modeling
- Data insertion
- SQL queries
- Data retrieval

## Status

⬜ Not Started

---

# 6. REST API

## Objectives

Expose the trained model through a REST API.

### Technology

- FastAPI

### Planned Endpoints

- GET /patients
- GET /statistics
- POST /predict

## Status

⬜ Not Started

---

# 7. Dashboard / Frontend

## Objectives

Develop an interactive interface for data exploration and predictions.

### Technologies

- Streamlit
- Dash (optional)
- React (optional)

### Features

- Dataset visualization
- Interactive charts
- Statistical analysis
- Parkinson score prediction

## Status

⬜ Not Started

---

# 8. Deployment

## Objectives

Deploy the application for public access.

### Possible Platforms

- Docker
- Render
- Railway

## Status

⬜ Not Started

---

# 9. Documentation

## Objectives

Complete the project documentation.

### Deliverables

- README
- Architecture overview
- Data pipeline
- Installation guide
- Usage instructions
- Results and discussion
- Final conclusions

## Status

⬜ Not Started
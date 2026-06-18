# 🔥 Forest Fire Risk Prediction System (End-to-End ML + Deployment)

## 🚀 Project Overview

This project is an end-to-end machine learning system that predicts **forest fire risk levels** based on environmental and meteorological conditions. The system is designed for real-world disaster monitoring use cases, aligned with applications in environmental surveillance and satellite-based analytics.

It integrates data preprocessing, feature engineering, model training, evaluation, and deployment using an interactive web application.

---

## 🎯 Objective

To build a predictive system that classifies forest fire risk as:

- 🌿 Low Risk  
- 🔶 Moderate Risk  
- 🔥 High Risk  

based on atmospheric and fire weather indices.

---

## 📊 Dataset

- Algerian Forest Fire Dataset
- Features include:
  - Temperature
  - Relative Humidity (RH)
  - Wind Speed (Ws)
  - Rainfall
  - FFMC, DMC, DC, ISI, BUI, FWI (fire weather indices)

---

## 🧠 Machine Learning Models Used

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Gradient Boosting Classifier

### 🏆 Best Model
- Gradient Boosting Classifier
- Achieved ~97–98% accuracy

---

## ⚙️ Workflow

1. Data Cleaning & Preprocessing
2. Feature Engineering
3. Model Training & Comparison
4. Performance Evaluation
5. Model Persistence using Joblib
6. Deployment using Streamlit

---

## 📈 Key Insights

- Fire Weather Index (FWI), FFMC, and ISI were the most influential predictors
- Environmental dryness and humidity significantly impact fire risk
- Ensemble models performed best on this dataset

---

## 🌐 Web Application

An interactive Streamlit dashboard allows users to input environmental conditions and get real-time fire risk predictions.

### Input Features:
- Temperature
- RH (Humidity)
- Wind Speed
- Rain
- FFMC, DMC, DC, ISI, BUI, FWI

### Output:
- Fire Risk Level (Low / Medium / High)
- Probability Score

---

## 🛠️ Tech Stack

- Python 🐍
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Streamlit
- Joblib

---

## 📁 Project Structure
Forest-Fire-Prediction/
│
├── app.py
├── forest_fire_model.pkl
├── dataset.csv
├── requirements.txt
├── notebooks/
└── README.md

---

## 🚀 Future Improvements

- Integration with satellite data (ISRO/remote sensing datasets)
- SHAP-based model explainability
- Geo-spatial fire risk mapping
- Real-time API-based predictions

---

## 👨‍💻 Author

**Lokesh Yadavalli**  
B.Tech CSE (AI/ML)  
VIT Bhopal University  

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to connect for collaboration.

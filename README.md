# 💳 Credit Card Fraud Detection using Machine Learning

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Alfiya-Simran/Credit-card-fraud-detection-model/blob/main/CreditcardFraudDetection.ipynb)

This project aims to detect fraudulent credit card transactions using machine learning techniques. It leverages a Random Forest Classifier along with preprocessing, visualization, and model evaluation steps to identify anomalies in transaction data.

---

## 📌 Project Overview

This notebook-based project demonstrates:

- ✅ Data preprocessing & standardization  
- 📊 Exploratory Data Analysis (EDA)  
- 🌲 Fraud detection using Random Forest Classifier  
- 🧪 Model evaluation with industry-standard metrics  

---

## 📂 Dataset

The dataset used is [Kaggle’s Credit Card Fraud Detection dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud), containing 284,807 transactions by European cardholders in September 2013. Only 492 (0.172%) of these are fraudulent, making this a highly imbalanced classification problem.

> ⚠️ **Note:** The dataset must be manually downloaded from Kaggle and placed in the project directory as `creditcard.csv`.

---

## 🧾 Features

- `V1` to `V28`: Principal components obtained via PCA
- `Time`: Seconds elapsed since the first transaction
- `Amount`: Transaction amount
- `Class`: Target variable (`0` = legit, `1` = fraud)

---

## 🔁 Workflow

1. **EDA**
   - Class distribution visualization
   - Feature correlations & patterns
2. **Preprocessing**
   - Feature scaling with `StandardScaler`
   - Train/test split
3. **Model Training**
   - `RandomForestClassifier` (robust to imbalance & high-dimensionality)
4. **Evaluation**
   - Confusion Matrix  
   - Classification Report  
   - ROC-AUC Curve  
   - Precision-Recall Curve  

---

## 🛠️ Libraries Used

```bash
pandas
numpy
matplotlib
seaborn
scikit-learn
```
---

## 🚀 How to Run

1. **Clone this repository or download the notebook.**
2. **Download the dataset from [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) and place `creditcard.csv` in the root directory.**
3. **Install dependencies** (choose one):

   - Using `requirements.txt` (recommended):

     ```bash
     pip install -r requirements.txt
     ```

   - Or manually:

     ```bash
     pip install pandas numpy matplotlib seaborn scikit-learn
     ```

4. **Run the notebook using Jupyter or any compatible environment.**

---

## 📄 License
**This project is licensed under the MIT License.**

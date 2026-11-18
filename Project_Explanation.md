# Salon Extra Service Prediction

## Short Project Explanation

### What is this project?
This is an educational machine learning project that predicts whether a salon customer will buy an **extra service**.

### Goal
Build a simple classification model that takes basic customer information and returns the probability of buying an additional service.

### Features
| Feature | Meaning |
|---------|---------|
| Age | Customer age |
| Visits | Number of previous visits |
| Bill_Amount | Current bill amount |
| Is_New_Customer | 1 = New customer, 0 = Returning |
| Service_Type | Haircut / Coloring / Treatment |
| Time_of_Day | Morning / Evening |

**Target:** Bought_Extra_Service (0 = No, 1 = Yes)

### What we did
1. Created a synthetic dataset of 400 customers
2. Split the data into training and testing sets
3. Built a preprocessing pipeline (One-Hot Encoding for categorical features)
4. Trained two models: Logistic Regression and Random Forest
5. Evaluated the models using Accuracy, F1-Score, and ROC-AUC
6. Used the best model to predict the probability of buying an extra service

### Important Note
The dataset is synthetic and created for educational purposes. The goal is to practice the machine learning workflow, not to make real business decisions.

### How to run
- Open the notebook `Salon_Extra_Service_Colab.ipynb` in Google Colab
- Run all cells

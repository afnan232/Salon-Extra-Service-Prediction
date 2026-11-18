# Salon Extra Service Prediction

Educational machine learning project that predicts whether a salon customer will buy an extra service.

## Main File (Recommended for Colab)

**`Salon_Extra_Service_Colab.ipynb`**  
→ Upload this notebook to Google Colab and run all cells.

## Project Files

| File | Description |
|------|-------------|
| `Salon_Extra_Service_Colab.ipynb` | Complete notebook (best for Colab) |
| `Project_Explanation.md` | Short project explanation |
| `generate_data.py` | Script to generate the dataset |
| `train_model.py` | Script to train models |
| `salon_data.csv` | Synthetic dataset (400 customers) |
| `app.py` | Optional Streamlit interface (local use) |
| `requirements.txt` | Required packages |

## Project Summary

- **Type:** Binary Classification
- **Target:** Bought_Extra_Service (0 or 1)
- **Models:** Logistic Regression & Random Forest
- **Dataset:** Synthetic (400 samples)

## Features

- Age
- Visits
- Bill_Amount
- Is_New_Customer
- Service_Type
- Time_of_Day

## How to use in Google Colab

1. Upload `Salon_Extra_Service_Colab.ipynb` to Google Colab
2. Run all cells
3. In the last section, change the customer values to test different predictions

## Important Note

This is an educational project with synthetic data.  
The goal is to practice the machine learning workflow.

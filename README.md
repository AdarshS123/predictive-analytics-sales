# Predictive Analytics - Sales Forecasting

A machine learning project that predicts sales prices using a Random Forest Regressor, built on a retail sales dataset.

## Overview

This project performs end-to-end sales analysis and prediction:
- Loads and cleans sales data from Excel
- Engineers time-based features (Month, Year, Quarter)
- Visualizes monthly sales trends and sales by category
- Trains a Random Forest model to predict sale prices
- Evaluates model performance using RMSE and R² Score

## Project Structure

```
Predictive ANALYTICS/
├── Analysis.py          # Main analysis and ML pipeline
└── Sales Dataset.xlsx   # Source sales data
```

## Tech Stack

| Library | Purpose |
|---|---|
| `pandas` | Data loading and manipulation |
| `numpy` | Numerical operations |
| `matplotlib` / `seaborn` | Data visualization |
| `scikit-learn` | ML model (Random Forest), train-test split, evaluation |

## How to Run

1. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn openpyxl
   ```

2. Run the script:
   ```bash
   python Analysis.py
   ```

## Features Used for Prediction

| Feature | Description |
|---|---|
| `Month` | Extracted from Order Date |
| `Year` | Extracted from Order Date |
| `Quarter` | Extracted from Order Date |
| `Quantity Ordered` | Number of units ordered |

**Target variable:** `Sale Price`

## Model Performance Metrics

- **RMSE** (Root Mean Squared Error)
- **R² Score** (Coefficient of Determination)

## Visualizations

- Monthly Sales Trend (line chart)
- Sales by Service Category (bar chart)
- Actual vs Predicted Sales (scatter plot)

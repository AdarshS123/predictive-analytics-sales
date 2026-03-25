# 📊 Sales Forecasting using Predictive Analytics

## 🚀 Project Overview  
This project focuses on building a predictive analytics model to forecast future sales using historical retail data. The workflow includes data cleaning, feature engineering, exploratory data analysis (EDA), and machine learning model development.

The objective is to demonstrate how data-driven approaches can support business decisions such as demand forecasting, inventory planning, and revenue optimisation.

---

## 📂 Dataset  
The dataset contains transactional sales data with over 1,000 records, including:
- Order details (Order Date, Ship Date)
- Product information (Category, Sub-Category, Product Name)
- Customer segmentation (Segment, Region)
- Sales, Quantity, Discount, and Profit

---

## ⚙️ Tech Stack  
- Python  
- Pandas, NumPy (Data preprocessing)  
- Matplotlib, Seaborn (Data visualisation)  
- Scikit-learn (Machine Learning - Random Forest)  
- OpenPyXL (Excel file handling)  

---

## 🔧 Project Workflow  

### 1. Data Preprocessing  
- Handled missing values  
- Converted date columns to datetime format  
- Removed irrelevant columns such as IDs and names  

### 2. Feature Engineering  
- Extracted time-based features (Month, Quarter, Year)  
- Created additional derived features to improve prediction  

### 3. Exploratory Data Analysis (EDA)  
- Analysed monthly sales trends  
- Compared performance across product categories  
- Identified patterns and variability in sales  

### 4. Model Development  
- Built a Random Forest Regressor  
- Split dataset into training and testing sets  
- Generated predictions on test data  

### 5. Model Evaluation  
- Mean Absolute Error (MAE)  
- Root Mean Squared Error (RMSE)  
- R² Score  

---

## 📊 Results  

| Metric | Value |
|--------|------|
| MAE    | ~259,000 |
| RMSE   | ~509 |
| R² Score | -0.017 |

The model shows low predictive performance, indicating that the current feature set is insufficient to capture complex sales patterns.

---

## 📈 Key Insights  
- Sales show seasonal variation across months  
- Certain product categories contribute more to revenue  
- Basic features alone are not sufficient for accurate predictions  
- Model performance is limited due to lack of strong business-related features  

---

## ⚠️ Limitations  
- Limited feature set (missing customer behaviour and pricing dynamics)  
- Presence of outliers affecting model performance  
- No hyperparameter tuning performed  
- No cross-validation applied  

---

## 🔥 Future Improvements  
- Add advanced features (customer behaviour, pricing, promotions)  
- Use advanced models such as XGBoost or LightGBM  
- Perform hyperparameter tuning  
- Apply cross-validation  
- Deploy using FastAPI or Streamlit  
- Integrate with BigQuery or cloud-based pipelines  

---

## 💡 Business Value  
- Supports sales forecasting and planning  
- Improves inventory management decisions  
- Enables data-driven business insights  
- Helps identify revenue trends and opportunities  

---

## ▶️ How to Run  

```bash
git clone https://github.com/your-username/sales-forecasting-project.git
cd sales-forecasting-project

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
python analysis.py

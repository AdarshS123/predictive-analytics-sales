# 1. IMPORT LIBRARIES

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 2. LOAD DATA

df = pd.read_excel('Sales Dataset.xlsx')

print(df.head())

#3. DATA CLEANING

df=df.dropna() #drop rows with missing values

df['Order Date'] = pd.to_datetime(df['Order Date']) #convert order date to datetime format

#feature engineering: extract year and month from order date

df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year
df['Quarter'] = df['Order Date'].dt.quarter

print("\nColumns after feature engineering:", df.columns)

#4 Visualization

#monthly sales trend
monthly_sales = df.groupby('Month')['Sale Price '].sum()

plt.figure(figsize=(10,6))
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()

#sales by category

plt.figure(figsize=(10,6))
sns.barplot(x='Service Category', y='Sale Price ', data=df)
plt.title('Sales by Category')
plt.xlabel('Service Category')
plt.ylabel('Total Sales')
plt.show()

#5. Feature Selection

features = [
    'Month', 'Year', 'Quarter', 'Quantity Ordered'
]
target = 'Sale Price '
X = df[features]
Y = df[target]

#6. Train-Test Split

X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=42) 


#7. Model Building

model= RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train,y_train)

#8. Prediction and Evaluation

y_pred = model.predict(X_test)
mae= mean_squared_error(y_test,y_pred)
rmse= np.sqrt(mean_squared_error(y_test,y_pred))
r2= r2_score(y_test,y_pred)
print("\nModel Performance:")
print("MAE:", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)

#10. Visualize Predictions

plt.figure(figsize=(10,6))
plt.scatter(y_test, y_pred)
plt.title('Actual vs Predicted Sales')
plt.xlabel('Actual Sales')
plt.ylabel('Predicted Sales')
plt.show()

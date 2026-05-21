import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

from pandas import set_option
#Reading The data
df=pd.read_excel('ecommerce_orders.xlsx')
set_option('display.max_rows', 500)
set_option('display.max_columns', 500)
set_option('display.width', 1000)
# print(df.shape[1])
# print(df.info())
# print(df.describe(include='all').T)

#Data preprocessing
df.columns=df.columns.str.strip().str.lower()
text_columns=["customer_name","order_id","product","category","payment_method","status"]

for column in text_columns:
    df[column]=df[column].astype(str).str.strip()
    df[column]=df[column].replace('nan',np.nan)
    df[column]=df[column].str.title()

df['order_date']=pd.to_datetime(df['order_date'],errors='coerce')
df['quantity']=pd.to_numeric(df['quantity'],errors='coerce').astype("Int64")
df['price']=pd.to_numeric(df['price'],errors='coerce')
df['price']=df.groupby('product')['price'].transform(lambda x:x.fillna(x.median()))
df['price']=df['price'].fillna(df['price'].median)
df=df.dropna(subset=['order_date','quantity'])
duplicated_orders=df[df.duplicated(subset=['order_id'],keep=False)]
# df=df.drop_duplicates(subset=['order_id'])
#Create Total for every order
df['total']=(df['price'] * df['quantity']).round(2)

df['year']=df['order_date'].dt.year
df['month']=df['order_date'].dt.to_period("M")

category_Sales= df.groupby('category').agg(
    total_Sales=('total','sum'),
    items_sold=('quantity','sum'),
)
product_Sales= df.groupby('product').agg(
    best_saler=('quantity','sum')
)
product_Sales= product_Sales.sort_values(by=['best_saler'],ascending=False)
category_Sales=category_Sales.sort_values(by=['total_Sales'],ascending=False)
print(category_Sales)
print(product_Sales)

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
print(df['quantity'])

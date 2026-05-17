import pandas as pd
df=pd.DataFrame({
    'Name':["Sherif","Omar","Karim","Gamal","Ahmed"],
    'Date':['12-05-2000','05-11-2000','01-01-2001','10-01-2000','03-10-2000']
})
df['Birthday']=pd.to_datetime(df['Date'])
df['Year']=df['Birthday'].dt.year
df['Month']=df['Birthday'].dt.month
df['Day']=df['Birthday'].dt.day
print(df)
import pandas as pd
df= pd.DataFrame({'Name':['Sherif','Omar','Karim','Gamal','Ahmed'],
                  'Job Title':['Data Analyst','Dentist','Engineer','Businessman','Accountant']})
df['Age']=[25,26,25,25,26]
#df= df.stack()
#print(df)
#print("//"*60)
#df=df.unstack()
#print(df)
print(df.query('Age >25'))
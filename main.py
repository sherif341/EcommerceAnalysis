import pandas as pd
df= pd.DataFrame({'Name':['Sherif','Omar','Karim','Gamal','Ahmed'],
                  'Job Title':['Data Analyst','Dentist','Engineer','Businessman','Accountant']})
filter =df[df['Job Title'].str.contains('Engineer')]
print(filter)
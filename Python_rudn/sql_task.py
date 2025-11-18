import pandas as pd 

df = pd.read_csv('data.csv')
data_type = {col: df[col].dtype for col in df.columns}
print(data_type)
import pandas as pd

df = pd.read_csv('/home/t12652/dirtydata.csv')


df["Calories"].fillna(125, inplace = True)


print(df.to_string())
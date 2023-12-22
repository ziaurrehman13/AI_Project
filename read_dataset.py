import pandas as pd
url= "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df=pd.read_csv(url)
print("dataset Preview")
print(df.head())

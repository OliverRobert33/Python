import pandas as pd

#df --> data friend
df = pd.read_csv("archivos_csv/texto1.csv",names= ["name","lastname","age"])
# print(df)

print(df["name"])

print(df)



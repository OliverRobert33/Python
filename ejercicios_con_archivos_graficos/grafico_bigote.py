import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Leo el arvhivo csv
df = pd.read_csv("ejercicios_con_archivos_graficos/texto_bigote.csv")

#creamoas el grafico de bigote 
sns.barplot(x="categoria", y="valor", data=df)
print(df)


#Esto nos permite mostrar la grafica
plt.show()
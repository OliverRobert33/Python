import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Leo el arvhivo csv
df = pd.read_csv("ejercicios_con_archivos_graficos/texto_lineal_grafico.csv")

#creamoas el grafico 
sns.barplot(x="tiempo", y="dinero", data=df)
print(df)


#Esto nos permite mostrar la grafica
plt.show()
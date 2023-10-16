import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ejercicios_con_archivos_graficos/texto_datos_lineal.csv")
print(df)

#Creamos el grafico
#lineplot --> crea un grafico de lineas
sns.lineplot(x="fecha",y="cantidad",data = df)

#Creamaos un punto en lo mas alto
plt.plot("08-03", 34,"o")

#Te permite mostrar el grafico
plt.show()


import pandas as pd

#df --> datafrands
df = pd.read_csv("archivos_csv/texto1.csv")
# print(df)

df2 = pd.read_csv("archivos_csv/texto1.csv")


df_ordenado_ascendente = df.sort_values("EDAD", ascending=True)
# print(df_ordenado_ascendente)

df_ordenado_descendente = df.sort_values("EDAD", ascending=False)
# print(df_ordenado_descendente)

#Concadenando los 2 dataframes
df_concadenado = pd.concat([df, df2])
# print(df_concadenado)

#Accediendo a las primeras filas
df_primeras_filas = df_concadenado.head(3)
# print(df_primeras_filas)

#Accediendo a las ultimas lineas
df_ultimas_filas = df_concadenado.tail(3)
# print(df_ultimas_filas)

#accediendo a las filas y columnas con shape
#usamos el desempaquetado
filas, columnas = df.shape
# print(filas)
# print(columnas)

#accediendo a la data estadista del data friend
data_estadistica = df.describe()
# print(data_estadistica)

#accediendo a un dato especifico de df con loc
usando_loc = df.loc[3, "NOMBRE"]
# print(usando_loc)

#accediendo a un dato especifico de df con iloc
usando_iloc = df.iloc[3, 2] #fila 3(4) columna 2
# print(usando_iloc)

#accediendo a toda la columna de los APELLIDOS
columna = df.loc[:, "APELLIDO"]
# print(columna)

#accediendo a toda la fila 
fila = df.loc[3, :]
# print(fila)

#presentando solo a los datos mayores a 30
mayores_30 = df.loc[df["EDAD"]>30,:]
print(mayores_30)

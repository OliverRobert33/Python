
import pandas as pd

df = pd.read_csv("ejercicios_con_archivos/texto1.csv")
# print(df)

#convertir a string los datos de edades que son enteros
df["EDAD"] = df["EDAD"].astype(str)

#presentando el tipo de datos para comprobar que se convirtio en cadena
# print(type(df["EDAD"][3]))

# print(df["EDAD"][3])


#Reemplazar en la columna APELLIDO de SARAGURO a FAMILIA SARAGURO
df["APELLIDO"].replace("SARAGURO", "FAMILIA SARAGURO", inplace=True)
# print(df["APELLIDO"])

#Eliminar las filas de df que no se encuentren completas
df = df.dropna()
# print(df)

#Eliminar las filas repetidas del df
df = df.drop_duplicates()
# print(df)

#Creando un csv nuevo con los datos limpios
df.to_csv("ejercicios_con_archivos/texto1_limpios.csv")

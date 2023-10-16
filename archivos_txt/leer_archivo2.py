
#Cuanso se utiliza el with open no es nescesario cerrar el archivo
with open("archivos_txt/texto1.txt", encoding = "UTF-8") as archivo:
    print(archivo.read())
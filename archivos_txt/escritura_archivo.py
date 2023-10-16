

#"w --> write" te sobreescribe el archivo
with open("archivos_txt/texto1.txt", "w", encoding="UTF-8") as archivo:
    for i in range(6):
        archivo.write(f"Linea {i+1} agregada con 'w'.\n")
    archivo.write("----------------\n")    
    
#"a --> append"  te a añade en el archivo
with open("archivos_txt/texto1.txt", "a", encoding="UTF-8") as archivo:
    for i in range(6):
        archivo.write(f"Linea {i+1} agregada con 'a'.\n")

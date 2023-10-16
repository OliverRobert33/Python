
#Le pedimos que nos diga la frase
frase = input("Hey parcero decime una frase y te calculo el tiempo en decirlo: ")

#Separamos a la frase obtenida
frase_separada = frase.split(" ")

#Contamos cuantas palbras tiene la frase
conteo_frase = len(frase_separada)

if conteo_frase >= 100:
    print("Hey mano no te mano un testamento")


print(f"Dijiste {conteo_frase} palabras y en decirlo tardarias {conteo_frase/2} segundos en decirlo")
promdeio_otras_personas = conteo_frase/2
print(f"Dalto dijo {conteo_frase} palabras y en decirlo tardaria {promdeio_otras_personas*0.7} segundos en decirlo")

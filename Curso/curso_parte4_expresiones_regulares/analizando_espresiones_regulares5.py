import re

texto = "Este es un ejemplo de una pagina web: 'https://ahynaraFashion.com'"

patente = "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

resultado = re.findall(patente, texto)

if resultado:
    print("Es valido")
else:
    print("Es invalido")

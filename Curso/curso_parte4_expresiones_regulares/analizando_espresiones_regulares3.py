import re

texto = "Reemplazando todas las vocales por arterisco."

texto_reemplazado = re.sub("[aeiou]", "*", texto)

print(texto_reemplazado)
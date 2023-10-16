
import re

frase = '''FILA 1. : Que tal chaval
FILA 2. : como te va en el curso de dalto. 
FILA 333: como te va en la high school. 
FILA 4ee44: como te va en el amor chaval
FILA 5: como esta tu?.
'''

#\d --> te muestra todos los numeros del texto
resultado1 = re.findall(r"\d", frase)
# print(resultado1)

#\d --> te muestra todos MENOS los numeros del texto
resultado2 = re.findall(r"\D", frase)
# print(resultado2)

#\w --> te muestra todos los datos A;fanumericos [a-z A-Z _] 
resultado3 = re.findall(r"\w", frase)
# print(resultado3)

#\W --> te muestra todos MENOS los datos A;fanumericos [a-z A-Z _] 
resultado4 = re.findall(r"\W", frase)
# print(resultado4)

#\s --> te muestra todos los espacios en blanco 
resultado5 = re.findall(r"\s", frase)
# print(resultado5)

#\S --> te muestra todos MENOS los espacios en blanco 
resultado6 = re.findall(r"\S", frase)
# print(resultado6)

#\n --> busca todos los saltos de linea del texto 
resultado7 = re.findall(r"\n", frase)
# print(resultado7)

#. --> pone todo el texto pero sin saltos de linea  
resultado8 = re.findall(r".", frase)
# print(resultado8)

#\. --> busca todos los puntos del texto. Con la barra invertida cancela la funcion del '.'  
resultado9 = re.findall(r"\.", frase)
# print(resultado9)

#\d\.\s --> busca un numero seguido de un punto seguido de un espacio.  
resultado10 = re.findall(r"\d\.\s", frase)
# print(resultado10)

#busca el comienzo de una linea o texto
# flags=re.M --> Esto te permite saber el comienzo de cada fila
resultado11 = re.findall(r"^FILA", frase, flags=re.M)
# print(resultado11)

# $ --> Busca el final de la fila
resultado12 = re.findall(r"chaval$", frase,  flags=re.M)
# print(resultado12)

# {} --> Busca n cantidad que repite el numero letra palabra etc
resultado13 = re.findall(r"\w{4}", frase,  flags=re.M)
# print(resultado13)

resultado14 = re.findall(r"\d{3}", frase,  flags=re.M)
# print(resultado14)

# {n,m} --> al menos n como maximo m
resultado15 = re.findall(r"\d{2,4}", frase,  flags=re.M)
# print(resultado15)

resultado16 = re.findall(r"(FILA){1}", frase)
# print(resultado16)

# | Te devuelve las 2 si las encuentra O SI NO SOLO UNA
resultado17 = re.findall(r"\d{2,4}|FILA", frase)
print(resultado17)

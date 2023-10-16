
frase1 = "Aprendiendo lo principal en python"
frase2 = "Enseñando lo principal en python"
frase3 = "12345" #es numerico
frase4 = "abcde" #es alfanumerico
frase5 = "Aprendiendo, lo ,principal, en, python"


# print(dir(frase1)) #Devuelve la lista de atributos validos del objeto pasadado 

resultado =  frase1.upper() # mayuscula
resultado1 =  frase1.lower() # minuscula
resultado2 =  frase1.capitalize() #primera mayuscula

resultado3 = frase2.find("o") #buscar una cadena en otra cadena; si no encuentra bota -1
resultado4 = frase2.index("ñ") #buscar una cadena en otra cadena; si  no enuentre sale error

resultado5 = frase3.isalnum() #si es numerico
resultado6 = frase4.isalpha() #si el alfa numerico

resultado7 = frase1.count("p") #numero de ocurrencias
resultado8 = len(frase1) #caracteres de una cadena

resultado9 = frase2.startswith("E") #si enpieza con la letra presenta TRUE
resultado10 = frase2.endswith("n") #si la ultima termina en la letra presenta FALSE

resultado11 = frase2.replace("Enseñando", "REPLACE") #remplaza una palabra con otra

resultado12 = frase5.split(",") #separa la cadena


# print(resultado)
# print(resultado1)
# print(resultado2)

# print(resultado3)
# print(resultado4)

# print(resultado5)
# print(resultado6)

print(resultado7)
# print(resultado8)

# print(resultado9)
# print(resultado10)

# print(resultado11)

# print(resultado12)
# print(type(resultado12))








def saludo (nombre, sexo):
    sexo = sexo.lower()
    if sexo == 'mujer':
        adjetivo = "Mi Reina <3"
    elif sexo == "hombre":
        adjetivo = "Titan"
    else:
        adjetivo = "Amor"
    print(f"Hola {nombre}, como estas {adjetivo}?")
        
saludo("Oliver", "HOMBRE")
saludo("Celeste", "MUJER")
saludo("Ruben", "no binario")


#Crear contraseñas 
def contraseñas_numero (num):
    chars = "abcdefjhij"
    temp = str(num)
    num = int(temp[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    key = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return key 
    
password = contraseñas_numero(7)

print(f"Tu contraseña es: {password}")

#forma no optima de sumar valores 
lista = [4,34,5,35,34]
def suma_no_optima(lista):
    suma = 0
    for num in lista:
        suma += num
    print (suma)
    
suma_no_optima(lista)

#forma optima de sumar valores 
def suma_optima(nombre,*numeros):
    # print(sum(numeros))
    return f"Joven {nombre} la suma de todos los valores es {sum(numeros)}"
    
resultado = suma_optima("Oliver",4,34,5,35,34)
print(resultado)



     


        
    
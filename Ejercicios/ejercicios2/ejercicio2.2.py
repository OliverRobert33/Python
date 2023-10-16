
# def numeros_impares(num):
#     cont = 1
#     while cont < num:
#         if cont%2 != 0:
#             print(cont)
#         cont += 1
        
            
# numeros_impares(15)

def es_primo(num):
    for i in range(2,num-1):
        print(i)
        #verificar si el numero pasado no puede dividirse por ningun 
        # numero entre 2 y ese mismo numero -1
        if num%i == 0: 
            #si es divisible por alguno retornamos false y termina el bucle
            return False
    #si termina el bucle singnifica que no fue divisible entonces es primo
    return True

def primos_hasta(num):
    numeros = []
    for i in range(2,num+1):
        resultado = es_primo(i)
        #verificamos si el numero es primo
        if resultado == True:
            #si es verdadero lo añadimos
            numeros.append(i)
    return numeros
        
resultado = primos_hasta(7)
print(resultado)


#Lo mas optimizado el codigo

primos = lambda num: list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)), range(2,num)))
print(primos(15))

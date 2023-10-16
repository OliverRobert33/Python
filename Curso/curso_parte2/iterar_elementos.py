
numeros = [1,2,3,4,5,6,7,8,9,10]

for num in numeros:
    if num%2 == 0:
        print(f'Numero par {num}')
    else:
        print(f'Numero impar {num}')
else:
    print("El bucle terminoo :)")
    print("--------------------------------------------")
    

lista1 = [1,2,3,4]
lista2 = [15,26,38,49]


#recorer dos listas al mismo tiempo del mismo tamaño
for l1, l2 in zip(lista1,lista2):
    print(f"Lista 1 {l1}")
    print(f"Lista 2 {l2}")
print("--------------------------------------------")
    
    
#for dentro de un rango 
for num in range(10,20):
    print (num)
print("--------------------------------------------")
    
    
    
# for correcto cuando se desea saber el indice
for list1 in enumerate(lista1):
    indice = list1[0]
    valor = list1[1]
    
    print(f"El indice es {indice} y el valor es {valor}.")
print("--------------------------------------------")
    
#-----------------------------------------------------------
# Definir una tupla y un conjunto
tupla = (1, 2, 3, 4, 5)
conjunto = {3, 4, 5, 6, 7}

# Iterar sobre la tupla
print("Iterando sobre la tupla:")
for tup in tupla:
    print(tup)

# Iterar sobre el conjunto
print("\nIterando sobre el conjunto:")
for conj in conjunto:
    print(conj)



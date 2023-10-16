
#Funcion comun
numeros = [1,2,3,4,5,6,7,8,9,10]

def num(num):
    if num%2 == 0:
        print(f"El {num} es par.")

numeros_pares = filter(num, numeros)

for num in numeros_pares:
    print(f"El {num} es par.")

print("--------------------")
#------------------------------------------
#Funcion lambda
numeros_pares2 = filter(lambda num: num %2==0, numeros)
# print(list(numeros_pares))

for num in numeros_pares2:
    print(f"El {num} es par.")



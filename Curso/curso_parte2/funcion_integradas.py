 
conjunto = {2,13,34,35,22,23}
tupla = (2,13,34,35,22,23)
lista = [2,13,34,35,22,23]

# Encontrando el numero mayor 
mayor_conjunto = max(conjunto)
mayor_tupla = max(tupla)
mayor_lista = max(lista)

print(f"{mayor_conjunto} - {mayor_tupla} - {mayor_lista}")

# Encontrando el numero menor 
menor_conjunto = min(conjunto)
menor_tupla = min(tupla)
menor_lista = min(lista)

print(f"{menor_conjunto} - {menor_tupla} - {menor_lista}")

#redondear numero 
numero = round(22.23443,2)

print(numero)

#retorna false si es == 0 y True si es diferente de 0
resultado = bool([23,23])
print(resultado)

#retorna si todos los valores osn verdaderos diferentes de 0 y none
resultado2 = all([23,23,["Oliver"]])
print(resultado2)

#suma todos los numeros
numbers = [12,1231,3,324]
print(sum(numbers))







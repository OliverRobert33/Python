
#meter un conjunto dentro de otro 
conjunto1 = frozenset({"Oliver", "Saraguro", "Remache"})
conjunto2 = {conjunto1, "Roberto"}

print(conjunto2)

#teoria de conjuntos
conjunto3 = {1,3,5,7}
conjunto4 = {1,3,5}
conjunto5 = {2,8,2}

#Verificar si es un subconjunto
resultado = conjunto4.issubset(conjunto3)
resultado = conjunto4 <= conjunto3
print(resultado)

#Verificar si es un superconjunto
resultado2 = conjunto3.issuperset(conjunto4)
resultado2 = conjunto3 > conjunto4
print(resultado2)

#Verificar si en el conjunto no ahy numeros en comun
resultado3 = conjunto5.isdisjoint(conjunto3)
print(resultado3)




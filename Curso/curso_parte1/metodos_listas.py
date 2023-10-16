

lista = list(["Hola", "Oliver", "Saraguro"])
lista_numeros = list([23,234,43,33,312])

resultado1 = len(lista) #cantidad de elementos

lista.append("Computacion") #añadir a la lista 

lista.insert(3, "Ingeniero") #agrega un elemento a la lista en la poscicion que tu desees

lista.extend(['III', "CICLO"]) #agrega varios elementos a una lista.

# lista.pop(-1) #el -1 ellimina al ultimo de la lista, -2 al penultimo y asi sucesivamente

# lista.pop(0) #el 1 ellimina al primero de la lista, 2 al segundo y asi sucesivamente

lista.remove('Hola') #ellimina el elemento si encuentra el valor

lista.clear() #elimina todos los elementos de la lista

# ordena la lista en orden y el metodo reverse=True pone a la lista ordenada de reversa
#[312, 234, 43, 33, 23]
lista_numeros.sort(reverse=True) 

#invierte una listasea ordenada o desordenada
# [23, 33, 43, 234, 312]
lista_numeros.reverse() 

print(resultado1)
print(lista)
print(lista_numeros)

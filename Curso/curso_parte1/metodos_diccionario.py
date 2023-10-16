
#keys() devuelve las claves
#get() devuelve el valor de una clave
#clear() elimina todos los elementos
#pop() elimina un elemento
#items() para iterar el dict


diccionario = {
    "nombre" : "OLiver",
    "apellido" : "Saraguro",
    "edad" : 18,
}

resultado1 = diccionario.keys()
resultado2 = diccionario.get("nombre") #Devuelve el valor 
resultado4 = diccionario.pop("apellido") #elimina la clave apellido y el valor del mismo
resultado5 = diccionario.items()
# resultado3 = diccionario.clear()


print(resultado1)
print(resultado2)
print(resultado4)
print(resultado5)
# print(resultado3)

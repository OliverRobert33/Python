
#creando diccionario con dict() // con este se puede crear diccionarios vacios
diccionario = dict(nombre = "Oliver", apellido = "Saraguro", celular = "0991249995")

# #Otra forma de crear diccionarios
# diccionario = {"nombre" : "Oliver", 
#                "apellido" : "Saraguro",
#                "celular" : "0991249995"}


#Las tuplas si pueden ser claves
diccionario2 = {("nombre", "apellido") : "saraguro"} 

#Un conjunto como clave se lo puede meter con el frozenset
diccionario3 = {frozenset({"nombre", "apellido"}) : "saraguro"} 


#Una lista como clave se lo puede meter con el frozenset
diccionario4 = {frozenset(["nombre", "apellido"]) : "saraguro"} 

#Creadno diccionario con fromkeys() esto nos permite crear con todos los valores none
diccionario5 = dict.fromkeys("12345", "Valor")
diccionario5 = dict.fromkeys(["12345", "Valor"])



print(diccionario5)
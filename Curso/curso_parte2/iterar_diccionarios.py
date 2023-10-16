diccionario = {
    "nombre" : "OLIVER",
    "apellido": "SARAGURO",
    "edad" : 18
}

for con in diccionario.items():
    clave = con[0]
    valor = con[1]
    
    print(f"La clave es '{clave}' y el valor es '{valor}'.")
    
#-----------------------------------------------------------------
frutas = ['pera', 'manzana','papaya', 'melon', 'maduro']


#no continua desde la papaya, se termina el ciclo
for fruta in frutas:
    if fruta == "papaya":
        break
    print(f"La fruta que voy a comer es {fruta}") 
    
#continua pero se salta la papaya
for fruta in frutas:
    if fruta == "papaya":
        continue
    print(f"La fruta que voy a comer es {fruta}") 
    
#-----------------------------------------------------------
lista = [2,4,6,8,10]
#elevando la lista con un for en una sola linea
lista_elevada = [num*2 for num in lista]

print(lista_elevada)
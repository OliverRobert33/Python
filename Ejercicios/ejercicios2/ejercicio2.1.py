

def obtener_profesor_asistente(cantidad_colleagues):
    colleagues = []
    
    for cant in range(cantidad_colleagues):
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        
        #creo una tupla donde se encuentren ambos valores
        colleague = (nombre, edad)
        
        #añado la tupla a la lista
        colleagues.append(colleague)
        
        #Ordeno la lista el campo 1 que es edad
        colleagues.sort(key= lambda e : e[1])
        
        #Asigno la poscicion 0 el menor en edad y 1 al mayor en edad.
        asistente = colleagues[0][0]
        profesor = colleagues[-1][0]
        
    #Hacemos la tupla y la retornamos 
    return asistente, profesor
    

asistente, profesor = obtener_profesor_asistente(2)

print(f"El profesor es {profesor} y el asistente es {asistente}")
        
        
        
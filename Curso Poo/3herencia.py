class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def saludar(self):
        print(f"Hola {self.nombre} saludando desde la funcion 'saludar'.")

#Heredar (Persons) 
class Cliente(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, sueldo):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.sueldo = sueldo
    def saludar(self):
        print(f"Hola {self.nacionalidad} renombrando la funcion 'saludar' desde la clase Cliente.")




cliente1 = Cliente("Oliver", 19, "Española", "Full stack", 2000.00)

print(cliente1.nacionalidad)

cliente1.saludar()





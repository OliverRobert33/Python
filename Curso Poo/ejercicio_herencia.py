class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def imprimir(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    def imprimir2(self):
        print(f"Grado: {self.grado}")

estudiante = Estudiante("Oliver", 19, "III Ciclo de Computacion")
estudiante.imprimir()    
estudiante.imprimir2()    




        
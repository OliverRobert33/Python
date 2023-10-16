class Estudiante:
    def __init__(self, n, e, g):
        self.nombre = n
        self.edad = e
        self.grado = g
    def estudiar(self):
        print(f"""
    Datos Estudiante:\n\n
        Nombre: {self.nombre}. \n
        Edad: {self.edad}.\n
        Grado: {self.grado}. \n
              """)


estudiante1 = Estudiante("Oliver", 19, "III ciclo")

nombre = input("Ingrese el Nombre: ")
edad = int(input("Ingrese la Edad: ") )
grado = input("Ingrese el Grado: ") 

estudiante2 = Estudiante(nombre, edad, grado)



# estudiante1.estudiar()
estudiante2.estudiar()

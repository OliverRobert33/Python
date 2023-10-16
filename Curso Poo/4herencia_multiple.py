
class Persona:
    def __init__(self, nombre, edad, identificacion):
        self.nombre = nombre
        self.edad = edad
        self.identificacion = identificacion

    

class Habilidades:
    def __init__(self, habilidad, t_practicandola):
        self.habilidad = habilidad
        self.t_practicandola = t_practicandola
    def mostrar_habilidad(self):
        print(f"Tu habilidad es un poco absurda {self.habilidad}")

class Empleado(Persona, Habilidades):
    def __init__(self, nombre, edad, identificacion, habilidad, t_practicandola, sueldo):
        Persona.__init__(self, nombre, edad, identificacion)
        Habilidades .__init__(self, habilidad, t_practicandola)
        self.sueldo = sueldo

empleado1 = Empleado("Oliver", 19, 1727135996, "Ver Youtube", "2 años", 2000.00)

print(empleado1.identificacion)

empleado1.mostrar_habilidad()

#verificar si Empleado es una subclase de Persona y Habilidades
subclase = issubclass(Empleado, Habilidades)

#verificar si empleado es una instancia de Empleado, Habilidades y Persona
instancia = isinstance(empleado1, Habilidades)
print(subclase)
print(instancia)


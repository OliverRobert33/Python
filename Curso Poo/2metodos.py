
class Celulares:
    def __init__(self, m, p, t):
        self.marca = m
        self.precio = p
        self.tamano = t
    def llamar (self):
        print(f"LLamaste desde un {self.marca}")
    def cortar (self):
        print(f"Cortaste desde un {self.marca} de tamaño {self.tamano}")


celulares1 = Celulares("Apple", 23.32, 9.8)
celulares2 = Celulares("Samsung", 23.32, 9.8)
celulares3 = Celulares("Xiaomi", 23.32, 9.8)

celulares1.llamar()
celulares2.cortar()

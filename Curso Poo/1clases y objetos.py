
class Celulares:
    def __init__(self, m, p, t):
        self.marca = m
        self.precio = p
        self.tamano = t

celulares1 = Celulares("apple", 23.32, 9.8)
celulares2 = Celulares("Samsung", 23.32, 9.8)
celulares3 = Celulares("Xiaomi", 23.32, 9.8)

print(celulares1.marca)


#--------------------------------------------------------------------------------
class Camionetas:
    def __init__(self, m, t, p):
        self.marca = m
        self.traccion = t
        self.precio = p
        

lista = [["Ford", "4*4", 35.999], 
         ["Toyota", "4*4", 27.999],
         ["Isuzu", "4*4", 32.999]]

for l in lista:
    m, t, p = l
    c = Camionetas(m,t,p)
    print(f"MARCA: {c.marca} - TRACCIONX: {c.traccion} - PRECIO: {c.precio}")


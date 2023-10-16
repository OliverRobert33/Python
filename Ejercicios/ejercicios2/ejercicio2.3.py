#SERIE FIBONACCI

def fibonacci(num):
    a,b = 0,1
    lista_fibonacci = [0]
    for i in range(num):
        if b > num:
            return lista_fibonacci
        else:
            lista_fibonacci.append(b)
            a,b = b, b+a

lista = fibonacci(34)
print(lista)

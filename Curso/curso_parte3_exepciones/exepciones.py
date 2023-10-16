
def suma():
    #este ciclo no servira para que cada vez que salte la exepcion vuelva a pedir datos
    while True:
        try:
            a = input("Ingrese el numero 1: ")
            b = input("Ingrese el numero 2: ")
            resultado = int(a) + int(b)
        except Exception as e:
            #en vez de saltar la exepcion saldra el siguiente print
            print("Boludo es numero no texto.")
            print(f"El error fue: {e}")
        else:
            #si a ingresado numeros correctamente cortara el ciclo de lo
            #contrario iria al except            
            break
    return resultado


print(suma())

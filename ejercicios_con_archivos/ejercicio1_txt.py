
#Creando 2 listas una con nombres y apellidos
nombres = ["Oliver","Roberto","Jose","Elian","Ahynara","Leonel"]
apellidos = ["Saraguro","Loarte","Remache","Quishpi","Vivanco","Rojas"]

with open("ejercicios_con_archivos/texto_escritura.txt", "w") as arch:
    arch.writelines("Los datos son: \n")
    [arch.writelines(f"\nNombre: {n}\nApellido: {a}\n")for n,a in zip(nombres, apellidos)]
    
    # for n,a in zip(nombres, apellidos):
    #     arch.writelines(f"\nNombre: {n}\nApellido: {a}\n")
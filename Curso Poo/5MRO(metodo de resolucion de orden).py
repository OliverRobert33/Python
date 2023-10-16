
class A():
    def hablar(self):
        print("DESDE A")
    # pass

class B():
    def hablar(self):
        print("DESDE B")
    # pass

class C(B):
    def hablar(self):
        print("DESDE C")
    # pass

class D(A):
    def hablar(self):
        print("DESDE D")
    # pass

class E (C,D):
    def hablar(self):
        print("DESDE E")
    pass


e = E()
e.hablar()  #E-C-B-D-A // DESDE E
# print(E.mro()) #te permite saber el orden en que se ejcutara

#ejecutar el metodo de la funcion que nosotros queramos 
A.hablar(e) #DESDE A



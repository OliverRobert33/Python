
#creando mi propia exepcion
class MiExepcion(Exception):
    def __init__ (self, err):
        print(f"Boludo cometiste un error {err}: ")

#Lanzando mi propia exepcion
# raise MiExepcion("Sos un tarara..")

#manejando mi exepcion
try:
    raise MiExepcion("Sos un tarara..")
except:
    print("Como vas a cometer ese error boludoooo.")

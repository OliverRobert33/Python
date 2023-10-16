
import re

frase = ''' Que tal chaval como te va en el curso de dalto, como te va en la high school, 
            como te va en el amor chaval, como esta tu?
'''

# search --> te verifica si la palabra que buscas esta en el texto
#re.IGNORECASE --> no le importan las mayusculas o las minusculas
resultado1 = re.search("Como", frase, flags= re.IGNORECASE)
print(resultado1)


#findall --> te muestra en una lista las veces que esta repetido la palabra
resultado = re.findall("como", frase)
print(resultado)
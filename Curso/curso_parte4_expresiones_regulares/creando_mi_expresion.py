import re

#Encontrando el numero CABA y ocultandolo
texto = "Hello I am Oliver Saraguro my number is +54 99 9124-9995"

patente= r"\+\d{1,3}\s\d{2}\s\d{4}-\d{4}"

result = re.sub(patente, ("(Numero Oculto)"),texto)
print(result)
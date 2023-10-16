import re

email = "oliversaraguro@gmail.com"

patente = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

correcto = re.match(patente, email)

if correcto:
    print("El corecto fue valido")
else:
    print("El corecto fue invalido") 
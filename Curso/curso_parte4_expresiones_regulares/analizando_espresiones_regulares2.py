import re

text = "La fecha es 23/23/2004 y el telefono es +1 -555-555-5555"

patente = r"\d{2}/\d{2}/\d{4}"

reemplazar = "Fecha Oculta"

text_new = re.sub(patente, reemplazar, text)

print(f"Texto modificado es: {text_new}")

import csv

with open("archivos_csv/texto1.csv") as text:
    archivo = csv.reader(text)
    for line in archivo:
        print(line) 

#variables promedio de duracion de cursos
otro_cursos_min = 2.5
otro_cursos_max = 7
cursos_promedio = 4
curso_dalto = 1.5

#variablea duracion crudo
crudo_promedio = 5
crudo_dalto = 3.5

#diferencias de duracion
diferencia_max = 100 - curso_dalto * 10000 // otro_cursos_max / 100 
diferencia_min = 100 - curso_dalto / otro_cursos_min * 100
diferencia_promedio = 100 - curso_dalto / cursos_promedio * 100

#calculando el oircentaje de tiempo vacio removido
tiempo_crudo_promedio = 100 - cursos_promedio * 10000 // crudo_promedio / 100 
tiempo_crudo_dalto = 100 - curso_dalto * 10000 // crudo_dalto / 100 



#Mostrando diferencias de duaracion
print(f"El curso de Dalto dura un {diferencia_max}% menos que el mas lento.")
print(f"El curso de Dalto dura un {diferencia_min}% menos que el mas lento.")
print(f"El curso de Dalto dura un {diferencia_promedio}% menos que el mas lento.")

#Mostrando la cantidad de espacios vacios que se remueven
print()
print(f"Un curso promedio elimina un {tiempo_crudo_promedio}% de tiempo vacio")
print(f"Este curso promedio elimina un {tiempo_crudo_dalto}% de tiempo vacio")

#Mostrando diferencias si los cursos duraran 10 horas 
print()
print(f"Ver 10 de este curso equivale a ver {cursos_promedio *100 //curso_dalto /10}% de otros cursos.")
print(f"Ver 10 de otro cursos equivale a ver {curso_dalto *100 //cursos_promedio /10}% de este curso.")



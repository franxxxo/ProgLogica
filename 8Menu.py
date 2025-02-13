# Ejercicio 8
# Realizar un menu que contenga los primeros 6 ejercicios.
from pick import pick

title = 'Escoge el programa que quiera ejecutar: '
options = ['Pared', 'Ventanas', 'Castillos', 'Suelo', 'Techo', 'Cuarto']
option, index = pick(options, title)
print(option)
print(index)

if index == 0:
    def pared():
        L = float(input("Ingrese la longitud del muro en metros: "))
        H = float(input("Ingrese la altura del muro en metros: "))
        CL = round((L * H) * (1 / ((0.23 + 0.010) * (0.05 + 0.015))), 2)
        print(f"La cantidad de ladrillos que se necsita es de : {CL}")

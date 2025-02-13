#Ejercicio 1 Cantidad de  ladrillos.

L = float(input("Ingrese la longitud del muro en metros: "))
H = float(input("Ingrese la altura del muro en metros: "))

CL= round((L*H)*(1/((0.23+0.010)*(0.05+0.015))), 2)

print(f"La cantidad de ladrillos que se necsita es de : {CL}")
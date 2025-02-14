#Ejercicio 6
#Cantidad de ladrillos o blocks necesarios de un cuartito

# medidas fijas: puerta largo 1m y alto 1.90m
# medidas fijas: ventanas largo 1.20m y alto 1.50m

A = float(input("\nIngrese el frente del cuarto en metros: "))
H= float(input("Ingrese la altura del cuarto en metros: "))
L= float(input("Ingrese lo largo del cuarto en metros: "))

APTrasera = A*H
APDelantera = APTrasera-1.9
APLateral = (((L*H)-1.8)*2)
ATotalCasa = APDelantera+APLateral+APTrasera

CL= round(ATotalCasa*(1/((0.23+0.010)*(0.05+0.015))), 2)
LMC= round((1/((0.23+0.010)*(0.05+0.015))), 2)

print(f"\nCantidad de ladrillos por metro cuadrado: {LMC}")
print(f"La cantidad de ladrillos que se necsita es de: {CL}\n")
#print(f"Delantera: {APDelantera} Trasera: {APTrasera} Lateral: {APLateral} Total: {ATotalCasa}")
# Ejercicio 8
# Calcular la cantidad de ladrillos necesarios para un cuarto
# con largo, ancho y alto variables, y tambien con las medidas de la puerta ventanas laterales y traseras variables.

# Solicitar las dimensiones del cuarto
A = float(input("\nIngrese el ancho del cuarto en metros: "))
L = float(input("Ingrese el largo del cuarto en metros: "))
H = float(input("Ingrese la altura del cuarto en metros: "))

# Solicitar las dimensiones de la puerta
LPuerta = float(input("\nIngrese el largo de la puerta en metros: "))
HPuerta = float(input("Ingrese la altura de la puerta en metros: "))

# Solicitar las dimensiones de las ventanas laterales
LVentanaIzq = float(input("\nIngrese el largo de la ventana izquierda en metros: "))
HVentanaIzq = float(input("Ingrese la altura de la ventana izquierda en metros: "))

LVentanaDer = float(input("\nIngrese el largo de la ventana derecha en metros: "))
HVentanaDer = float(input("Ingrese la altura de la ventana derecha en metros: "))

# Solicitar las dimensiones de las ventanas traseras
LVentanaTra = float(input("\nIngrese el largo de la ventana trasera en metros: "))
HVentanaTra = float(input("Ingrese la altura de la ventana trasera en metros: "))

# Calcular el área de las paredes
APFrontal = A*H
APTrasera = APFrontal
APLateral = L*H*2

# Calcular el área de la puerta
APuerta = LPuerta*HPuerta

# Calcular el área de las ventanas laterales
AVentanaIzq = LVentanaIzq*HVentanaIzq
AVentanaDer = LVentanaDer*HVentanaDer

# Calcular el área de las ventanas traseras
AVentanaTra = LVentanaTra*HVentanaTra

# Calcular el área total a cubrir con ladrillos
ATotal = (APFrontal+APTrasera+APLateral)-(APuerta+AVentanaIzq+AVentanaDer+AVentanaTra)

# Calcular la cantidad de ladrillos necesarios
ALadrillo = (0.23+0.01)*(0.05+0.015)
CanLadrillos = round(ATotal/ALadrillo, 2)

print(f'\nEl area total del cuarto es de: {ATotal:.2f} m2')
print(f"La cantidad de ladrillos necesarios: {CanLadrillos}")
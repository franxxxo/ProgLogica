#Ejercicio 3 Cantidad de varillas, metros de varilla y anillos

altoCastillo = float(input("\nIntroduce el alto de los castillos en metros: "))
numCastillos = float(input("Introduce el numero de castillos: "))

Var = 4*numCastillos
metrosVar = round(altoCastillo*Var,2)
Anillos = int((numCastillos*altoCastillo)/0.10)

print(f"\nLa cantidad de varillas necesarios son: {Var}")
print(f"Los metros de varilla necesarias son:  {metrosVar}")
print(f"La cantidad de anillos necesarios son: {Anillos}")
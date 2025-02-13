#Ejercicio 2 Cantidad de ladrillos cuando hay dos ventanas.

L = float(input("Ingrese la longitud del muro en metros: "))
H = float(input("Ingrese la altura del muro en metros: "))

sim = input("\n¿Las ventanas son simétricas?" " \n  1) Si \n  2) No\nIngresa tu opcion: ")

def ventanas_simetricas():
    LV = float(input("\nIngrese la longitud de las ventanas en metros: "))
    HV = float(input("Ingrese la altura de las ventanas en metros: "))
    return LV*HV, LV*HV

def ventanas_asimetricas():
    LV1 = float(input("\nIngrese la longitud de la primera ventana en metros: "))
    HV1 = float(input("Ingrese la altura de la primera ventana en metros: "))
    LV2 = float(input("Ingrese la longitud de la segunda ventana en metros: "))
    HV2 = float(input("Ingrese la altura de la segunda ventana en metros: "))
    return LV1*HV1, LV2*HV2

opciones = {
    "1": ventanas_simetricas,
    "2": ventanas_asimetricas
}

AV1, AV2 = opciones[sim]()
AVT = AV1+AV2

AM = L*H
AT = AM-AVT

CL = round((AT)*(1/((0.23+0.010)*(0.05+0.015))), 2)

print(f"\nLa cantidad de ladrillos que se necesitaran es de: {CL}")
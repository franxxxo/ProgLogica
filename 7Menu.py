# Ejercicio 8
# Realizar un menu que contenga los primeros 6 ejercicios.
from pick import pick

def Pared():
    L = float(input("Ingrese la longitud del muro en metros: "))
    H = float(input("Ingrese la altura del muro en metros: "))

    CL= round((L*H)*(1/((0.23+0.010)*(0.05+0.015))), 2)
    print(f"La cantidad de ladrillos que se necsita es de : {CL}")

def Ventanas():
    return

def Castillos():
    return

def Suelo():
    return

def Techo():
    return

def Cuarto():
    return

title = 'Escoge el programa que quiera ejecutar: '
options = ['1. Pared', '2. Ventanas', '3. Castillos', '4. Suelo', '5. Techo', '6. Cuarto']
option, index = pick(options, title, default_index=1)



if index == 1:
    Pared()
elif index == 2:
    L = float(input("Ingrese la longitud del muro en metros: "))
    H = float(input("Ingrese la altura del muro en metros: "))

    LV1 = float(input("\nIngrese la longitud de la primera ventana en metros: "))
    HV1 = float(input("Ingrese la altura de la primera ventana en metros: "))
    LV2 = float(input("Ingrese la longitud de la segunda ventana en metros: "))
    HV2 = float(input("Ingrese la altura de la segunda ventana en metros: "))

    AV1 = LV1*HV1
    AV2 = LV2*HV2

    AVT = AV1+AV2

    AM = L*H
    AT = AM-AVT

    CL = round((AT)*(1/((0.23+0.010)*(0.05+0.015))), 2)

    print(f"\nLa cantidad de ladrillos que se necesitaran es de: {CL}")

elif index ==3:
    altoCastillo = float(input("\nIntroduce el alto de los castillos en metros: "))
    numCastillos = float(input("Introduce el numero de castillos: "))

    Var = 4*numCastillos
    metrosVar = round(altoCastillo*Var,2)
    Anillos = int((numCastillos*altoCastillo)/0.10)

    print(f"\nLa cantidad de varillas necesarios son: {Var}")
    print(f"Los metros de varilla necesarias son:  {metrosVar}")
    print(f"La cantidad de anillos necesarios son: {Anillos}")
elif index == 4:
    Largo = float(input(f"\nIngrese lo largo en metros: "))
    Ancho = float(input(f"Ingrese lo ancho en metros: "))

    MetrosCubicos = (Largo*Ancho*0.15)

    Cemento = MetrosCubicos*350
    SacosCemento = Cemento/50
    Arena = round(MetrosCubicos*0.56,2)
    Grava = round(MetrosCubicos*0.84,2)
    Agua = round(MetrosCubicos*180,2)

    print(f"\nPara {MetrosCubicos} metros cubicos se necesitan: "
          f"\n {Cemento} kilos de cemento que son {SacosCemento} sacos de cemento."
          f"\n {Arena} metros cubicos de arena."
          f"\n {Grava} metros cubicos de grava."
          f"\n {Agua} litros de agua.\n")
elif index == 5:
    Largo = float(input(f"\nIngrese lo largo en metros: "))
    Ancho = float(input(f"Ingrese lo ancho en metros: "))

    MetrosCubicos = (Largo*Ancho*0.10)

    Cemento = MetrosCubicos*350
    SacosCemento = Cemento/50
    Arena = round(MetrosCubicos*0.56,2)
    Grava = round(MetrosCubicos*0.84,2)
    Agua = round(MetrosCubicos*180,2)

    print(f"\nPara {MetrosCubicos} metros cubicos se necesitan: "
          f"\n {Cemento} kilos de cemento que son {SacosCemento} sacos de cemento."
          f"\n {Arena} metros cubicos de arena."
          f"\n {Grava} metros cubicos de grava."
          f"\n {Agua} litros de agua.\n")
elif index == 6:
    F = float(input("\nIngrese el frente del cuarto en metros: "))
    H= float(input("Ingrese la altura del cuarto en metros: "))
    D= float(input("Ingrese lo largo del cuarto en metros: "))

    APTrasera = F*H
    APDelantera = APTrasera-1.9
    APLateral = (((D*H)-1.8)*2)
    ATotalCasa = APDelantera+APLateral+APTrasera

    CL= round(ATotalCasa*(1/((0.23+0.010)*(0.05+0.015))), 2)
    LMC= round((1/((0.23+0.010)*(0.05+0.015))), 2)

    print(f"\nCantidad de ladrillos por metro cuadrado: {LMC}")
    print(f"La cantidad de ladrillos que se necsita es de: {CL}\n")    
# Ejercicio 8
# Realizar un menu que contenga los primeros 6 ejercicios.
from pick import pick

def calcular_ladrillos(area):
    return round(area * (1 / ((0.23 + 0.010) * (0.05 + 0.015))), 2)

def calcular_materiales(metros_cubicos):
    cemento = metros_cubicos * 350
    sacos_cemento = cemento / 50
    arena = round(metros_cubicos * 0.56, 2)
    grava = round(metros_cubicos * 0.84, 2)
    agua = round(metros_cubicos * 180, 2)
    return cemento, sacos_cemento, arena, grava, agua

def pared():
    L = float(input("Ingrese la longitud del muro en metros: "))
    H = float(input("Ingrese la altura del muro en metros: "))
    area = L * H
    CL = calcular_ladrillos(area)
    print(f"\nLa cantidad de ladrillos que se necesita es de: {CL}")
    input("Presiona Enter para continuar...")

def ventanas():
    L = float(input("\nIngrese la longitud del muro en metros: "))
    H = float(input("Ingrese la altura del muro en metros: "))

    LV1 = float(input("\nIngrese la longitud de la primera ventana en metros: "))
    HV1 = float(input("Ingrese la altura de la primera ventana en metros: "))
    LV2 = float(input("Ingrese la longitud de la segunda ventana en metros: "))
    HV2 = float(input("Ingrese la altura de la segunda ventana en metros: "))

    AV1 = LV1 * HV1
    AV2 = LV2 * HV2
    AVT = AV1 + AV2

    AM = L * H
    AT = AM - AVT

    CL = calcular_ladrillos(AT)
    print(f"\nLa cantidad de ladrillos que se necesitarán es de: {CL}")
    input("Presiona Enter para continuar...")

def castillos():
    alto_castillo = float(input("\nIntroduce el alto de los castillos en metros: "))
    num_castillos = float(input("Introduce el número de castillos: "))

    var = 4 * num_castillos
    metros_var = round(alto_castillo * var, 2)
    anillos = int((num_castillos * alto_castillo) / 0.10)

    print(f"\nLa cantidad de varillas necesarias son: {var}")
    print(f"Los metros de varilla necesarios son: {metros_var}")
    print(f"La cantidad de anillos necesarios son: {anillos}")
    input("Presiona Enter para continuar...")

def suelo():
    Largo = float(input("\nIngrese lo largo en metros: "))
    Ancho = float(input("Ingrese lo ancho en metros: "))
    MetrosCubicos = Largo * Ancho * 0.15
    cemento, sacos_cemento, arena, grava, agua = calcular_materiales(MetrosCubicos)

    print(f"\nPara {MetrosCubicos} metros cúbicos se necesitan: "
          f"\n {cemento} kilos de cemento que son {sacos_cemento} sacos de cemento."
          f"\n {arena} metros cúbicos de arena."
          f"\n {grava} metros cúbicos de grava."
          f"\n {agua} litros de agua.\n")
    input("Presiona Enter para continuar...")

def techo():
    Largo = float(input("\nIngrese lo largo en metros: "))
    Ancho = float(input("Ingrese lo ancho en metros: "))
    MetrosCubicos = Largo * Ancho * 0.10
    cemento, sacos_cemento, arena, grava, agua = calcular_materiales(MetrosCubicos)

    print(f"\nPara {MetrosCubicos} metros cúbicos se necesitan: "
          f"\n {cemento} kilos de cemento que son {sacos_cemento} sacos de cemento."
          f"\n {arena} metros cúbicos de arena."
          f"\n {grava} metros cúbicos de grava."
          f"\n {agua} litros de agua.\n")
    input("Presiona Enter para continuar...")

def cuarto():
    F = float(input("\nIngrese el frente del cuarto en metros: "))
    H = float(input("Ingrese la altura del cuarto en metros: "))
    D = float(input("Ingrese lo largo del cuarto en metros: "))

    APTrasera = F * H
    APDelantera = APTrasera - 1.9
    APLateral = (((D * H) - 1.8) * 2)
    ATotalCasa = APDelantera + APLateral + APTrasera

    CL = calcular_ladrillos(ATotalCasa)
    LMC = round((1 / ((0.23 + 0.010) * (0.05 + 0.015))), 2)

    print(f"\nCantidad de ladrillos por metro cuadrado: {LMC}")
    print(f"La cantidad de ladrillos que se necesita es de: {CL}\n")
    input("Presiona Enter para continuar...")

def main():
    title = 'Escoge el programa que quiera ejecutar: '
    options = ['1. Pared', '2. Ventanas', '3. Castillos', '4. Suelo', '5. Techo', '6. Cuarto', '7. Salir']
    while True:
        option, index = pick(options, title, default_index=1)
        if index == 0:
            pared()
        elif index == 1:
            ventanas()
        elif index == 2:
            castillos()
        elif index == 3:
            suelo()
        elif index == 4:
            techo()
        elif index == 5:
            cuarto()
        elif index == 6:
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()
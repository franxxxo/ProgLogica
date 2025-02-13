#EJercicio 6
#Calcular la cantidad de materiales que se necesitaran por la cantidad de metros cubicos

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
from automation import Automation
from palabras_autos import palabras_autos


palabras_autos = palabras_autos.split("\n")
print(palabras_autos)
n = 0
automation = Automation()

for palabra in palabras_autos:
    # titulo = automation.generar_palabra()
    resultado = automation.buscar(palabra)
    if resultado == None:
        print("hola")
    n += 1

    print(f"{n}")


automation.cerrar()










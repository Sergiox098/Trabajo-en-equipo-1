Ancho_corral = int(input("Ingrese el ancho del corral en metros: "))
Largo_corral = int(input("Ingrese el largo del corral en metros: "))

Metros = Ancho_corral * Largo_corral
Litros = Metros * 24
Dias_semana = 7

Litros_semana = Metros * Litros/ Dias_semana
Metros_semana = Metros * Dias_semana

print(f"En una semana, la vaca produce {Litros_semana} litros de leche, usando {Metros_semana} metros cuadrados de pasto")

aves=int(input("Ingrese la cantidad de aves del galpón: "))
def granja(x):
    gallina=x/3
    huevo3=(30/3)*(gallina/2)
    huevo5=(30/5)*(gallina/2)
    huevomes=huevo5+huevo3
    return huevomes
print("Las gallinas del galpón producen", granja(aves), "Huevos al mes.")

Ancho_corral = int(input("Ingrese el ancho del corral en metros: "))
Largo_corral = int(input("Ingrese el largo del corral en metros: "))

Metros = Ancho_corral * Largo_corral
Litros = Metros * 24
Dias_semana = 7

Litros_semana = Metros * Litros/ Dias_semana
Metros_semana = Metros * Dias_semana

print(f"En una semana, la vaca produce {Litros_semana} litros de leche, usando {Metros_semana} metros cuadrados de pasto")


aves=int(input("Ingrese la cantidad de aves del galpón: "))
def granja(x):
    gallina=x/3
    huevo3=(30/3)*(gallina/2)
    huevo5=(30/5)*(gallina/2)
    huevomes=huevo5+huevo3
    return huevomes
print("Las gallinas del galpón producen", granja(aves), "Huevos al mes.")

print("Holaaa")
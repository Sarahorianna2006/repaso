# Área y perímetro de un círculo, Pide el radio de un círculo y muestra el área y el perímetro (circunferencia).📌 Usa pi = 3.1416

pi = 3.1416
radio = float(input("Ingrese el radio del circulo a consultar:\n>"))

area = pi * radio **2
perimetro = 2 * pi * radio

print(f"Area del circulo: {round(area, 2)} unidades cuadradas\n Perimetro (circunferencia): {round(perimetro,2)} unidades")


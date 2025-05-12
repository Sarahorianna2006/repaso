#Calculadora de salario neto
#Pide:
#Sueldo bruto
#Porcentaje de descuento (por ejemplo: 13)
#Calcula el sueldo neto usando la fórmula:
#sueldo_neto = sueldo_bruto - (sueldo_bruto * descuento / 100)
#Ejemplo de salida:
#Sueldo bruto: 1000 Descuento: 13 Sueldo neto: 870.0

sueldo_bruto = int(input("Ingresa el sueldo bruto a consulta:\n>"))
porcentaje_descuento = int(input("Ingrese el porcentaje de descuento a consultar:\n> %"))

sueldo_neto = sueldo_bruto - (porcentaje_descuento / 100)

print(f"El sueldo bruto: {sueldo_bruto} Descuento:% {porcentaje_descuento} Sueldo neto: {sueldo_neto}")


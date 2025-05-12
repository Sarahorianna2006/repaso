#Cálculo de propina y cuenta total, Pide el costo de una comida y calcula el 10%, 15% y 20% de propina. Muestra el total a pagar en cada caso.
print("Consulta de propina y cuenta total")
costo_comida = int(input("Ingrese el precio de la comida a consultar:\n>"))

propina_10 = costo_comida * 0.10
propina_15 = costo_comida * 0.15
propina_20 = costo_comida * 0.20


cuenta_total_10 = costo_comida + propina_10
cuenta_total_15 = costo_comida + propina_15
cuenta_total_20 = costo_comida + propina_20

print(f"Con el 10% de propina: {propina_10} y el total a pagar seria: {cuenta_total_10}")
print(f"Con el 15% de propina: {propina_15} y el total a pagar seria: {cuenta_total_15}")
print(f"Con el 20% de propina: {propina_20} y el total a pagar seria: {cuenta_total_20}")


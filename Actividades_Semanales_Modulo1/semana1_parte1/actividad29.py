#Conversor de minutos a días y horas, Pide una cantidad de minutos y muestra a cuántos días, horas y minutos equivale.

minutos_total = int(input("Ingresa la cantidad de minutos a consultar en numeros enteros:\n>"))

#1 dia = 1440 minutos

dias = minutos_total // 1440
horas = (minutos_total % 1440) // 60
minutos = minutos_total % 60

print(f"{minutos_total} minutos son: {dias} dia(s), {horas} hora(s), {minutos} minuto(s)")
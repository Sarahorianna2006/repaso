# Extraer hora, minuto y segundo de segundos totales,Pide al usuario un número de segundos y muestra cuántas horas, minutos y segundos son. 📌 Ejemplo: 3665 segundos → 1 hora, 1 minuto, 5 segundos.

segundos_totales = int(input("Ingrese una cantidad de segundos:\n>"))
hora = segundos_totales // 3600
minutos =(segundos_totales % 3600) //60
segundos = segundos_totales % 60

print(f"la cantidad de segundos que ingresaste en horas y minutos seria:\n {hora} hora(s), {minutos} minuto(s),{segundos} segundo(s)")




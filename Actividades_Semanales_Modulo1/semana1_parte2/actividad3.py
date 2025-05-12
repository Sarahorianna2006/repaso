#Pide una edad y muestra si está fuera del rango de 0 a 120.

edad = int(input("Ingresa tu edad:\n>"))

resultado = edad >= 0 and edad <= 120

print(f"La edad ingresada esta dentro del rango?\n {resultado}")

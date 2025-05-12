#Convertir temperatura (F ↔ C), Pide una temperatura en Fahrenheit y muestra el equivalente en Celsius.

temperatura_f = float(input("Ingrese una temperatura en Fahrenheit:\n>"))

temperatura_c = (temperatura_f - 31)*5/9

print(f"{temperatura_f}°F equivale a {temperatura_c,}°C")
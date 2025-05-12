#Inverso de número de tres cifras, Pide un número de tres cifras (ej. 123) y muestra sus cifras en orden inverso (321). 💡 Usa operaciones matemáticas para extraer centenas, decenas y unidades.

num = int(input("Ingrese un numero de tres cifras:\n>"))

centena = num // 100
decena = (num % 100) //10
unidad = num % 10

inversion = unidad * 100 + decena * 10 + centena

print(f"el numero invertido es:\n{inversion}")


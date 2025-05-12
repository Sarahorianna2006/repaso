#Extraer dígitos de un número de 4 cifras, Pide un número de 4 cifras e imprime cada dígito por separado, separados por coma.📌 Ejemplo: Entrada → 1234 → Salida → 1, 2, 3, 4

num = int(input("Ingresa un numero de cuatro cifras\n>"))

mil = num // 1000
centena = (num % 1000) //100
decena = (num % 100) //10
unidad = num %10

print(f"El numero ingresado separado por coma (,) es:\n {mil},{centena},{decena},{unidad}")


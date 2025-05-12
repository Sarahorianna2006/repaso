# Divisible por 5, Pide un número entero y muestra si es divisible entre 5 (usar % y ==).

num = int(input("Ingrese un numero entero:\n.>"))

resultado = num % 5 == 0

print(f"El numero ingresado es divisible entre 5?\n {resultado}")
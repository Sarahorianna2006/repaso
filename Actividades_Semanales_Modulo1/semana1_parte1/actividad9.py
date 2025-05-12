#Todas las operaciones; Pide al usuario dos números y muestra: suma, resta, multiplicación y división, separadas por coma.

num1 = int(input("Ingrese el primer numero a consultar: \n> "))
num2 = int(input("Ingrese el segundo numero a consultar: \n> "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"el resultado de ambos numeros es: \n suma:{suma}, resta:{resta}, multiplicacion:{multiplicacion} y division:{division}")
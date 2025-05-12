#Pide dos números y muestra si el primero es mayor y distinto del segundo.

num1 = int(input("Ingresa el primer numero a consultar\n>"))
num2 = int(input("Ingresa el segundo numero a consultar\n>"))

resultado = (num1 > num2) and (num1 != num2)

print(f"El primer numero es mayor y distinto del segundo numero? \n {resultado}")

#Pide tres números y muestra si el primero es menor que el segundo y mayor que el tercero.

num1 = int(input("Ingresa el primer numero entero a consulta:\n>"))
num2 = int(input("Ingresa el segundo numero entero a consulta:\n>"))
num3 = int(input("Ingresa el tercer numero entero a consulta:\n>"))

resultado = (num1 <= num2) and (num1 >= num3)

print(f"El primer numero es menor que el segundo numero y mayor que el tercero?\n {resultado}")


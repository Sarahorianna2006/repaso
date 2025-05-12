#Pide tres números y muestra si todos son diferentes.

num1 = int(input("Ingresa el primer numero a consultar:\n>"))
num2 = int(input("Ingresa el segundo numero a consultar:\n>"))
num3 = int(input("Ingresa el tercer numero a consultar:\n>"))

resultado = num1 != num2 != num3 != num1

print(f"Los numeros son diferentes?\n{resultado}")



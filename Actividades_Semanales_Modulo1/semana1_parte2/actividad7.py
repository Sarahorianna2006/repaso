#Pide tres números y muestra si alguno de ellos es igual a 0.

num1 = int(input("Ingresa el primer numero a consultar:\n>"))
num2 = int(input("Ingresa el segundo numero a consultar:\n>"))
num3 = int(input("Ingresa el tercer numero a consultar:\n>"))

if num1 == 0 or num2 == 0 or num3 == 0:
    print("Al menos uno de los numeros es igual a 0")
else:
    print("Ninguno de los numeros es igual a 0")


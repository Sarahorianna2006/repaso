#Ambos mayores que 10, Pide dos números y muestra si ambos son mayores que 10 (usar and).

num1 = int(input("Ingrese el primer numero entero:\n>"))
num2 = int(input("Ingrese el segundo numero entero:\n>"))

resultado = num1 >= 10 and num2 >= 10


print(f"Ambos numeros son mayor o igual a 10?\n {resultado}")
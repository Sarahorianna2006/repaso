#Calculadora de múltiplos
#Pide dos números y verifica si el primero es múltiplo del segundo usando %.
#Ejemplo:
#12 es múltiplo de 4 → True 15 es múltiplo de 6 → False

num1 = int(input("Ingrese el primer numero a consultar:\n>"))
num2 = int(input("Ingrese el segundo numero a consultar:\n>"))

numeros = num1 % num2 == 0

print(f"{num1} es multiplo de {num2}: {numeros} ")
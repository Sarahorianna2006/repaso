#No son iguales, Pide dos números y muestra si el primero no es igual al segundo (usar not y ==).

num1 = int(input("Ingrese el primer numero entero:\n>"))
num2 = int(input("Ingrese el segundo numero entero:\n>"))

resultado = not num1 == num2 

print(f"el primer numero no es igual al segundo?\n {resultado}")

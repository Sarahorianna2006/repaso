#Pide dos números y muestra si no son iguales y el primero es mayor que 5.

num1 = int(input("Ingresa el primer numero a consultar:\n>"))
num2 = int(input("Ingresa el segundo numero a consultar:\n>"))

if num1 != num2 and num1 >=5:
    print(f"Los numeros no son iguales y el primer numero es mayor a 5")
elif num1 == num2 and num1 >=5:
    print("Los numeros son iguales y el primer numero es mayor a 5 ")
elif num1 == num2 and num1 <=4:
    print("Los numeros son iguales y el primer numero no es mayor a 5" )
elif num1 != num2 and num1 <=4:
    print("Los numeros no son iguales y el primer numero no es mayor a 5")

else:
    print("No se cumple ninguna condicion")
#Pide un número y muestra si no es igual a 0 ni a 1.

num = int(input("Ingresa un numero entero a consultar:\n>"))

respuesta = num != 0 and num != 1

print(f"El numero ingresado no es igual a 0 o a 1 \n{respuesta}")

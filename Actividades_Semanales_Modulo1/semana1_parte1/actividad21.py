#Intercambio de variables, Pide dos valores al usuario e imprime los valores intercambiados. 📌 Ejemplo: Entrada → a = 3, b = 5 → Salida → a = 5, b = 3

a = input("Ingresa el valor de a:\n> a =")
b = input("Ingresa el valor de b:\n> b = ")

#respuesta1 = a, b 
#respuesta2 = b, a
a, b = b, a
print(f"El intercambio de ambos valores seria:\n a= {a}, b = {b}")

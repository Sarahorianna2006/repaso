#Pide una palabra y muestra si su longitud es menor o igual a 5 caracteres.

palabra = input("Ingresa una palabra:\n>")

if len(palabra) <= 5:
    print("La palabra ingresada tiene 5 o menos caracteres")
else:
    print("La palabra ingresada tiene mas de 5 caracteres")

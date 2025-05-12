#Repetir palabra, Pide al usuario una palabra y un número entero. Muestra la palabra repetida ese número de veces.

palabra = input("Ingresa una palabra: \n>")
num1 = int(input("Ingrese un numero: \n>"))


print(f"{(palabra + "\n") * num1}")
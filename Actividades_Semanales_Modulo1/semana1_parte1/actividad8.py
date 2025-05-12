#División entera y módulo; Pide al usuario dos números y muestra la división entera (//) y el módulo (%) entre ellos.

num1 = int(input("Ingrese el primer numero a dividir: \n>"))
num2 =int(input("Ingrese el segundo numero a dividir: \n>"))

division = num1 // num2
modulo = num1 % num2

print(f"El resultado de la division de ambos numeros es: {division} y su modulo {modulo}")
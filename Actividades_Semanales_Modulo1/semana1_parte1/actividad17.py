# Al menos uno mayor que 10, Pide dos números y muestra si al menos uno es mayor que 10 (usar or).

num1 = int(input("Ingrese el primer numero entero:\n>"))
num2 = int(input("Ingrese el segundo numero entero:\n>"))

resultado = num1 >= 10 or num2 >= 10

print(f"Uno o ambos numeros ingresados son mayor o igual a 10?\n {resultado}")

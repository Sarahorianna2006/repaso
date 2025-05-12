#Calculadora de promedio con validación
#Pide al usuario 3 notas (entre 0 y 10).
#Si alguna nota está fuera del rango, muestra un mensaje de error.
#Si todas son válidas, calcula el promedio y muestra si el estudiante aprueba (≥ 6) o reprueba.

nota1 = float(input("Ingresa la primera nota a consultar(0 al 10):\n>"))
nota2 = float(input("Ingresa la segunda nota a consultar(0 al 10):\n>"))
nota3 = float(input("Ingresa la tercera nota a consultar(0 al 10):\n>"))                  

#notas = nota1, nota2, nota3
#calcular_promedio = (nota1 + nota2 + nota3) /3

if 0 <= nota1 <= 10 and 0<= nota2 <= 10 and 0<= nota3 <=10:
    calcular_promedio = (nota1 + nota2 + nota3) /3
    print(f"Promedio: {calcular_promedio:.2f}")

    if calcular_promedio >=6:
        print("El estudiante aprueba")
    else:
        print("El estudiante reprueba")
else:
    print("Dato invalido: Todas las notas deben estar entre 0 a 10")
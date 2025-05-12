#Pide una calificación del 0 al 10 y muestra si es válida (entre 0 y 10, sin incluir extremos).

calificacion = float(input("Ingrese una calificacion del 0 al 10:\n>"))

if 0 < calificacion <10:
    print("La calificacion es valida")
else:
    print("La calificacion es invalida")



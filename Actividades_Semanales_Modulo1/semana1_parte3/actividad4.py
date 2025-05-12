#¿Compatibles?
#Pide:
#Nombre y edad de dos personas
#Verifica si:
#Ambos tienen al menos 18 años
#Se llaman distinto
#La diferencia de edad no supera los 10 años
#Si cumplen todo, imprime un mensaje gracioso diciendo que son compatibles 💞
#Si no, di por qué no lo son.

nombre1 = input("Ingresa el nombre de la persona:\n>")
edad1 = int(input(f"Ingresa la edad de {nombre1}:\n>"))
nombre2 = input("Ingresa el nombre de la persona:\n>")
edad2 = int(input(f"Ingresa la edad de {nombre2}:\n>"))

mayoria = edad1 >= 18 and edad2 >= 18
nombre_distintos = nombre1.lower() != nombre2.lower()
diferencia_edad = abs(edad1 - edad2) <=10

if mayoria and nombre_distintos and diferencia_edad:
    print("Son compatibles")
else:
    print("No son compatibles porque:")
    if not mayoria:
        print("Al menos una persona es menos de 18 anos")
    if not nombre_distintos:
        print("Tienen el mismo nombre")
    if not diferencia_edad:
        print("La diferencia de edad es mas de 10 anos")




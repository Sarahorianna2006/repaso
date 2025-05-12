# Años para jubilarse
#Pide la edad y el género del usuario ("M" para mujer, "H" para hombre).
#Mujer se jubila a los 60 años
#Hombre se jubila a los 65 años
#Si ya se puede jubilar, muestra un mensaje celebratorio.
#Si no, indica cuántos años faltan para la jubilación.

edad = int(input("Ingrese su edad:\n>"))
genero = input("Ingrese su género (M si es mujer y H si es hombre):\n>").upper()

if genero == "M":
    edad_jubilacion = 60
elif genero == "H":
    edad_jubilacion = 65
else:
    print("Genero no válido, por favor ingrese 'M' o 'H'") 
    exit()
if edad >= edad_jubilacion:
   print("Felicidades puedes jubilarte") 
else:
    anos_restantes = edad_jubilacion - edad
    print(f"Te faltan {anos_restantes} anos para poder jubilarte")




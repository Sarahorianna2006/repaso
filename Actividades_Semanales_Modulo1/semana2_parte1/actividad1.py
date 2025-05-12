#Asistente de clima y vestimenta 🌦️
#Crea un programa que pida la temperatura y si está lloviendo o no.
#🧥 Según los datos, sugiere qué ropa usar: abrigo, paraguas, ropa ligera, etc.
#Hazlo reutilizable para futuras ampliaciones.

temperatura = int(input("Ingresa la temperatura:\n> Grados Celsius: "))
#estado_clima = input("Ingrese el estado del clima (lluvioso o soleado):\n>")

if temperatura <= 27:
    print("Prevencion de dia lluvioso. Se sugiere llevar: abrigo, paraguas o impermeable")
elif temperatura >= 28:
    print("Prevencion de dia soleado. Se recomienda llevar: ropa ligera, hidratacion y bloqueador solar")
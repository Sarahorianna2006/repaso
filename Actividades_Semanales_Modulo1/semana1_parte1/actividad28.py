# Formato de precio con dos decimales,Pide al usuario un precio (float) y muestra el resultado con dos decimales y símbolo de moneda (por ejemplo: $123.45).
                                                                                                
precio = float(input("Ingrese un numero con decimal (separado por . ):\n>"))


print(f"El numero que ingreso en precio seria:\n ${precio:.2f}")

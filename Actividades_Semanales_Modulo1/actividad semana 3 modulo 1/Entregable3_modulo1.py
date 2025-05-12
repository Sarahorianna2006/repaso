#inventario en el cual aplico diccionario con tupla

inventory = {}

#anadir prodcuto al inventario

def add_produc():
    name = input("\033[46mIngresa el nombre del producto:\033[0m\n>").lower()

    try:
        price = int(input("\033[46mIngrese el precio del producto:\033[0m\n>"))
        amount = int(input("\033[46mIngresa la cantidad del producto:\033[0m\n>"))
    except ValueError:
        print("\033[31mDebes ingresar numeros validos, intente nuevamente\033[0m")
        return
    if name in inventory:
        print("El producto ya existe, se actualizara con los nuevos datos")
    else:
        print("\033[35mProducto añadido al inventario\033[0m")

    inventory[name] = (price, amount)
    print(f"Inventario actualizado:\n Producto: {name}, precio: {price}, cantidad: {amount}")
   # print(f"Inventario actualizado: {inventory}")

#busquedad de producto en el inventario por nombre

def search_produc():
    name = input("\033[46mIngrese el nombre del producto que desea buscar:\033[0m\n>")
    product = inventory.get(name)

    if product:
        print(f"Precio: {product[0]}:")
        print(f"Cantidad disponible: {product[1]}:")
    else:
        print("\033[31mEl producto no existe, intente nuevamente\033[0m")

#Actualizacion de precio de producto

def update_price():
    name = input("\033[46mIngrese el nombre del producto a actualizar:\033[0m\n>").lower()

    if name in inventory:
        try:
            new_price = int(input("\033[46mIngresa el nuevo precio:\033[0m\n>"))
        except ValueError:
            print("\033[31mprecio no valido, ingresa un numero valido\033[0m")
            return
        
        _,amount = inventory[name]
        inventory[name] = (new_price, amount)
        print(f"\033[35mPrecio actualizado para el producto: {name}\033[0m")
        print(f"Nuevo precio: {new_price}")
    else:
        print("\033[31mEl producto introducido no esxite en el inventario\033[0m")

#Eliminacion de producto

def revome_produc():
    name = input("\033[46mIngrese el nombre del producto a eliminar:\033[0m\n>").lower()

    if name in inventory:
        del inventory[name]
        print(f"\033[35mProducto {name}, eliminado del inventario\033[0m")
    else:
        print("\033[31mEl producto ingresado no existe en el inventario\033[0m")

#Calcular valor total inventario usando lambda

def calculate_total_value():
    calculate = lambda inv: sum(price * amount for price, amount in inv.values())
    total = calculate(inventory)
    print(f"El valor total del inventario es: {total}")

#Menu para permitir al usuario escoger que hacer
def menu():
    while True:
        print("\033[46mmenu\033[0m")
        print("\033[34m1. \033[0mAnadir producto")
        print("\033[34m2. \033[0mBuscar producto")
        print("\033[34m3. \033[0mActualizar precio")
        print("\033[34m4. \033[0mEliminar producto")
        print("\033[34m5. \033[0mCalcular valor total del inventario")
        print("\033[34m6. \033[0mVer inventario completo")
        print("\033[34m7. \033[0mSalir")

        option = input("\033[35mSeleccione la opcion a consultar:\033[m \n>")

        if option == "1":
            add_produc()
        elif option == "2":
            search_produc()
        elif option == "3":
            update_price()
        elif option == "4":
            revome_produc()
        elif option == "5":
            calculate_total_value()
        elif option == "6":
            print("\033[46mInventario actual:\033[0m\n>")
            for product, data in inventory.items():
                print(f"{product.title()}, precio: {data[0]}, cantidad: {data[1]} ")
        elif option == "7":
            print("\033[35msaliendo del programa...\033[0m")
            break
        else:
            print("\033[31mOpcion invalida, intente nuevamente\033[0m")

#llamar a funcion para iniciar programa
menu()
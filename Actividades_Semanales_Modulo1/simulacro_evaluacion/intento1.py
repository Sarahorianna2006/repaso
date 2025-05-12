#
inventario = {}

generos_validos = ["Fiction", "Non-Fiction", "Science", "Biography","Children"]

def anadir_libro():
    titulo_libro = input("Ingrese el nombre del libro:\n>")
    if titulo_libro in inventario:
        print("El libro ya exixte en el inventario")
        return
    

    autor_libro = input("Ingrese el nombre del autor del libro:\n>")
    try:
        cantidad_libro = int(input("Ingrese la cantidad de copias del libro:\n>"))
    except ValueError:
        print("Cantidad inválida. Intente de nuevo.")
        return
    

    genero_literario_libro = input("Ingrese el genero del libro:\n")
    if genero_literario_libro not in generos_validos:
        print(f"Género inválido. Géneros válidos: {generos_validos}")
        return
    
    inventario[titulo_libro] = {
            "autor": autor_libro,
            "copias_disponibles": cantidad_libro,
            "copias_totales": cantidad_libro,
            "genero": genero_literario_libro
        }
    print(f"Libro '{titulo_libro}' añadido con éxito.")
        
    inventario [titulo_libro] = (autor_libro, cantidad_libro, genero_literario_libro)
    print(f"Inventario actualizado:\n Libro:{titulo_libro}, Autor:{autor_libro}, Cantidad:{cantidad_libro}, Genero:{genero_literario_libro} ")

def buscar_libro():
    titulo_libro = input("Ingrese el nombre del libro que desea buscar:\n>")
    libro = inventario.get(titulo_libro)

    if libro:
        print(f"Autor: {libro['autor']}:")
        print(f"Cantidad disponible: {libro['copias_disponibles']}:")
        print(f"Genero literario: {libro['genero']}:")
    else:
        print("El libro no existe, intente nuevamente")

def eliminar_libro():
    titulo_libro = input("ingrese el nombre del libro a eliminar\n>")
    if titulo_libro in inventario:
        libro = inventario[titulo_libro]
        if libro["copias_disponibles"] == libro["copias_totales"]:
            del inventario[titulo_libro]
            print(f"Libro '{titulo_libro}' eliminado del inventario.")
        else:
            print("No se puede eliminar el libro porque hay copias prestadas.")
    else:
        print("El libro no existe en el inventario.")

def prestar_libro():
    titulo_libro = input("Ingrese el título del libro a prestar:\n> ")
    if titulo_libro in inventario:
        if inventario[titulo_libro]["copias_disponibles"] > 0:
            inventario[titulo_libro]["copias_disponibles"] -= 1
            print(f"Libro '{titulo_libro}' prestado con éxito.")
        else:
            print("No hay copias disponibles para prestar.")
    else:
        print("El libro no existe, intente nuevamente")  

def devolver_libro():
    titulo_libro = input("Ingrese el título del libro a devolver:\n> ")
    if titulo_libro in inventario:
        if inventario[titulo_libro]["copias_disponibles"] < inventario[titulo_libro]["copias_totales"]:
            inventario[titulo_libro]["copias_disponibles"] += 1
            print(f"Libro '{titulo_libro}' devuelto con éxito.")
        else:
            print("Todas las copias ya están en la biblioteca.")
    else:
        print("El libro no existe, intente nuevamente")


def listar_por_genero():
    genero_literario_libro = input("Ingrese el género a listar:\n> ")
    if genero_literario_libro not in generos_validos:
        print(f"Género inválido. Géneros válidos: {generos_validos}")
        return
    encontrados = False
    for titulo, datos in inventario.items():
        if datos["genero"] == genero_literario_libro:
            print(f"Libro: {titulo}, Autor: {datos['autor']}, Copias disponibles: {datos['copias_disponibles']}")
            encontrados = True
    if not encontrados:
        print("No hay libros de ese género en el inventario.")

def resumen_inventario():
    total_libros = len(inventario)
    total_copias = sum(libro["copias_disponibles"] for libro in inventario.values())
    print(f"Resumen del inventario:\nTotal de títulos: {total_libros}\nTotal de copias disponibles: {total_copias}")


def menu():
    while True:
        print("\n--Menú Biblioteca--")
        print("1. Añadir libro")
        print("2. Buscar libro")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Eliminar libro")
        print("6. Listar libros por género")
        print("7. Resumen de inventario")
        print("8. Salir")

        opcion = input("Seleccione una opción:\n> ")

        if opcion == "1":
            anadir_libro()
        elif opcion == "2":
            buscar_libro()
        elif opcion == "3":
            prestar_libro()
        elif opcion == "4":
            devolver_libro()
        elif opcion == "5":
            eliminar_libro()
        elif opcion == "6":
            listar_por_genero()
        elif opcion == "7":
            resumen_inventario()
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente de nuevo.")

menu()

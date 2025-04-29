# ------------------------------------------------
# Ejemplo de Taxonomía: Categorías y Objetos
# ------------------------------------------------

# Estructura jerárquica de categorías
# Cada clave representa una categoría principal, y su valor es una lista de subcategorías.
taxonomia = {
    "vehiculo": ["terrestre", "acuatico", "aereo"],
    "terrestre": ["automovil", "motocicleta", "bicicleta"],
    "acuatico": ["barco", "lancha"],
    "aereo": ["avion", "helicoptero"]
}

# Objetos y sus categorías
# Cada clave es un objeto, y su valor es la categoría a la que pertenece.
objetos = {
    "Honda Civic": "automovil",
    "Yamaha R6": "motocicleta",
    "Boeing 737": "avion",
    "Lancha Rápida": "lancha",
    "Bicicleta de Montaña": "bicicleta"
}

# ---------------------------
# Función: encontrar supercategoría
# ---------------------------
def encontrar_categoria_base(objeto):
    """
    Encuentra la categoría base (supercategoría) de un objeto dado.
    Si el objeto no existe, muestra un mensaje de error.
    """
    # Buscar la categoría del objeto en el diccionario 'objetos'
    categoria = objetos.get(objeto)
    if not categoria:
        print(f"No se encuentra el objeto: {objeto}")
        return

    # Recorrer la jerarquía de categorías para encontrar la supercategoría
    for padre, hijos in taxonomia.items():
        if categoria in hijos:
            print(f"{objeto} es un '{categoria}', que pertenece a la categoría '{padre}'.")
            return

    # Si no se encuentra la categoría en la jerarquía
    print(f"Categoría de {objeto} no está en la jerarquía.")

# ---------------------------
# Función: listar objetos de una categoría
# ---------------------------
def listar_objetos_en_categoria(categoria):
    """
    Lista todos los objetos que pertenecen a una categoría específica.
    Si la categoría no existe, muestra un mensaje de error.
    """
    # Verificar si la categoría existe en la taxonomía o en los valores de objetos
    if categoria not in taxonomia and categoria not in objetos.values():
        print(f"La categoría '{categoria}' no existe.")
        return

    # Buscar todos los objetos que pertenecen a la categoría
    encontrados = [obj for obj, cat in objetos.items() if cat == categoria]
    print(f"\nObjetos en la categoría '{categoria}':")
    if encontrados:
        # Imprimir cada objeto encontrado
        for obj in encontrados:
            print(f"  - {obj}")
    else:
        # Si no hay objetos registrados en la categoría
        print("  (No hay objetos registrados)")

# ---------------------------
# Función: subcategorías de una categoría
# ---------------------------
def listar_subcategorias(categoria):
    """
    Lista todas las subcategorías de una categoría dada.
    Si no hay subcategorías, muestra un mensaje indicando que no existen.
    """
    # Obtener las subcategorías de la categoría dada
    subcats = taxonomia.get(categoria, [])
    print(f"\nSubcategorías de '{categoria}': {', '.join(subcats) if subcats else '(ninguna)'}")

# ---------------------------
# Función: mostrar toda la taxonomía
# ---------------------------
def mostrar_taxonomia():
    """
    Muestra toda la jerarquía de categorías de manera estructurada.
    Cada categoría principal se muestra con sus subcategorías.
    """
    print("\nTaxonomía completa:")
    for categoria, subcategorias in taxonomia.items():
        print(f"- {categoria}: {', '.join(subcategorias)}")

# ---------------------------
# Menú interactivo
# ---------------------------
def menu():
    """
    Menú interactivo para explorar la taxonomía.
    Permite al usuario seleccionar diferentes opciones para interactuar con las categorías y objetos.
    """
    while True:
        # Mostrar las opciones del menú
        print("\n--- Menú ---")
        print("1. Encontrar categoría base de un objeto")
        print("2. Listar objetos en una categoría")
        print("3. Listar subcategorías de una categoría")
        print("4. Mostrar toda la taxonomía")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        # Procesar la opción seleccionada
        if opcion == "1":
            # Opción para encontrar la categoría base de un objeto
            objeto = input("Ingrese el nombre del objeto: ")
            encontrar_categoria_base(objeto)
        elif opcion == "2":
            # Opción para listar objetos en una categoría
            categoria = input("Ingrese el nombre de la categoría: ")
            listar_objetos_en_categoria(categoria)
        elif opcion == "3":
            # Opción para listar subcategorías de una categoría
            categoria = input("Ingrese el nombre de la categoría: ")
            listar_subcategorias(categoria)
        elif opcion == "4":
            # Opción para mostrar toda la taxonomía
            mostrar_taxonomia()
        elif opcion == "5":
            # Opción para salir del programa
            print("Saliendo del programa.")
            break
        else:
            # Mensaje de error para opciones no válidas
            print("Opción no válida. Intente de nuevo.")

# ---------------------------
# Ejecución del programa
# ---------------------------
if __name__ == "__main__":
    # Iniciar el menú interactivo
    menu()

# Algoritmo de Inducción Gramatical mejorado
# Este ejemplo verifica el patrón aⁿbⁿ y permite la interacción con el usuario

def verificar_patron_anbn(cadenas):
    """
    Verifica si las cadenas cumplen el patrón aⁿbⁿ.
    Retorna True si todas las cadenas cumplen el patrón, False en caso contrario.
    """
    for cadena in cadenas:
        # Calcula la longitud de la cadena
        n = len(cadena)
        # Divide la longitud entre 2 para obtener la mitad
        mitad = n // 2

        # Revisa si la longitud de la cadena es par
        if n % 2 != 0:
            # Si no es par, no puede cumplir el patrón aⁿbⁿ
            print(f"La cadena '{cadena}' no tiene longitud par.")
            return False

        # Divide la cadena en dos partes: la primera mitad y la segunda mitad
        parte_a = cadena[:mitad]  # Primera mitad (debe ser solo 'a')
        parte_b = cadena[mitad:]  # Segunda mitad (debe ser solo 'b')

        # Verifica si la primera mitad es solo 'a' y la segunda mitad es solo 'b'
        if parte_a != 'a' * mitad or parte_b != 'b' * mitad:
            # Si no cumple el patrón, se informa al usuario
            print(f"La cadena '{cadena}' no sigue el patrón aⁿbⁿ.")
            return False

    # Si todas las cadenas cumplen el patrón, retorna True
    return True

def inducir_gramatica_anbn(cadenas):
    """
    Induce una gramática para el patrón aⁿbⁿ si las cadenas cumplen el patrón.
    """
    # Llama a la función para verificar si las cadenas cumplen el patrón
    if verificar_patron_anbn(cadenas):
        # Si cumplen el patrón, imprime la gramática inducida
        print("\nLas cadenas siguen el patrón aⁿbⁿ.")
        print("Gramática inducida:")
        print("  S → aSb | ε")  # Regla de producción para el patrón aⁿbⁿ
    else:
        # Si no cumplen el patrón, informa que no se puede inducir una gramática
        print("\nLas cadenas no siguen un patrón de tipo aⁿbⁿ.")
        print("No se puede inducir una gramática simple.")

def main():
    """
    Función principal que permite al usuario ingresar cadenas y ejecuta la inducción gramatical.
    """
    # Mensaje inicial para el usuario
    print("Inducción Gramatical: Verificación del patrón aⁿbⁿ")
    print("Ingrese las cadenas separadas por comas (ejemplo: ab, aabb, aaabbb):")
    
    # Solicita al usuario que ingrese las cadenas
    entrada = input("> ")
    # Divide la entrada en una lista de cadenas, eliminando espacios en blanco
    cadenas = [cadena.strip() for cadena in entrada.split(",")]

    # Llama a la función para inducir la gramática con las cadenas ingresadas
    inducir_gramatica_anbn(cadenas)

# Ejecuta el programa principal si el archivo se ejecuta directamente
if __name__ == "__main__":
    main()
# -------------------------------------------------------------------
# Jerarquía de Chomsky: ejemplos en Python para cada tipo de gramática
# -------------------------------------------------------------------

import re

# -------------------------------------------------------------------
# Función para gramática Tipo 3: Regular
# -------------------------------------------------------------------
def tipo_3_regular(cadena):
    """
    Tipo 3: Simula gramática regular (acepta solo cadenas del tipo a+b+).
    Una gramática regular genera cadenas con un patrón fijo, como 'a+b+'.
    Ejemplo válido: "aaabbb"
    Ejemplo inválido: "abab", "aaa"
    """
    if not cadena:
        # Si la cadena está vacía, no es válida para esta gramática.
        return False, "Cadena vacía no válida para gramática regular."
    # Verifica si la cadena cumple con el patrón 'a+b+' usando expresiones regulares.
    match = re.fullmatch(r"a+b+", cadena)
    return match is not None, "Cumple con el patrón 'a+b+'" if match else "No cumple con el patrón 'a+b+'"

# -------------------------------------------------------------------
# Función para gramática Tipo 2: Independiente del contexto
# -------------------------------------------------------------------
def tipo_2_cfg(cadena):
    """
    Tipo 2: Gramática independiente del contexto (aⁿbⁿ).
    La cadena debe tener el mismo número de 'a' seguido del mismo número de 'b'.
    Ejemplo válido: "aaabbb"
    Ejemplo inválido: "abab", "aaa"
    """
    if not cadena or len(cadena) % 2 != 0:
        # Si la cadena está vacía o su longitud no es par, no es válida.
        return False, "Longitud no válida para aⁿbⁿ."
    # Divide la longitud de la cadena entre 2 para verificar la cantidad de 'a' y 'b'.
    n = len(cadena) // 2
    # Verifica si la cadena tiene exactamente 'n' 'a' seguidas de 'n' 'b'.
    match = cadena == "a" * n + "b" * n
    return match, "Cumple con la forma aⁿbⁿ" if match else "No cumple con la forma aⁿbⁿ"

# -------------------------------------------------------------------
# Función para gramática Tipo 1: Sensible al contexto
# -------------------------------------------------------------------
def tipo_1_context_sensitive(cadena):
    """
    Tipo 1: Gramática sensible al contexto (aⁿbⁿcⁿ).
    La cadena debe tener el mismo número de 'a', 'b' y 'c' en ese orden.
    Ejemplo válido: "aaabbbccc"
    Ejemplo inválido: "aabbcc", "abcabc"
    """
    if not cadena or len(cadena) % 3 != 0:
        # Si la cadena está vacía o su longitud no es múltiplo de 3, no es válida.
        return False, "Longitud no válida para aⁿbⁿcⁿ."
    # Divide la longitud de la cadena entre 3 para verificar la cantidad de 'a', 'b' y 'c'.
    n = len(cadena) // 3
    # Verifica si la cadena tiene exactamente 'n' 'a', seguidas de 'n' 'b', seguidas de 'n' 'c'.
    match = cadena == "a" * n + "b" * n + "c" * n
    return match, "Cumple con la forma aⁿbⁿcⁿ" if match else "No cumple con la forma aⁿbⁿcⁿ"

# -------------------------------------------------------------------
# Función para gramática Tipo 0: Irrestricta
# -------------------------------------------------------------------
def tipo_0_turing_completo(cadena):
    """
    Tipo 0: Gramática irrestricta (palíndromos simétricos ww).
    La cadena debe ser de la forma ww, donde la primera mitad es igual a la segunda.
    Ejemplo válido: "abab"
    Ejemplo inválido: "abcabc", "aaabbb"
    """
    if not cadena or len(cadena) % 2 != 0:
        # Si la cadena está vacía o su longitud no es par, no es válida.
        return False, "Longitud no válida para ww."
    # Divide la cadena en dos mitades.
    mitad = len(cadena) // 2
    # Verifica si la primera mitad es igual a la segunda mitad.
    match = cadena[:mitad] == cadena[-mitad:]
    return match, "Cumple con la forma ww" if match else "No cumple con la forma ww"

# -------------------------------------------------------------------
# Función para probar las gramáticas con un conjunto de cadenas
# -------------------------------------------------------------------
def probar_gramaticas(cadenas):
    """
    Prueba las cadenas con cada tipo de gramática y muestra los resultados.
    """
    print("Resultados por tipo de gramática:\n")
    for w in cadenas:
        print(f"Cadena: '{w}'")
        # Itera sobre cada tipo de gramática y su función correspondiente.
        for tipo, funcion in [
            ("Tipo 3 (Regular)", tipo_3_regular),
            ("Tipo 2 (CFG aⁿbⁿ)", tipo_2_cfg),
            ("Tipo 1 (aⁿbⁿcⁿ)", tipo_1_context_sensitive),
            ("Tipo 0 (ww)", tipo_0_turing_completo),
        ]:
            # Llama a la función correspondiente y obtiene el resultado.
            resultado, mensaje = funcion(w)
            # Muestra el resultado con un símbolo ✔ o ✘.
            estado = "✔" if resultado else "✘"
            print(f"  {tipo}: {estado} - {mensaje}")
        print()

# -------------------------------------------------------------------
# Cadenas de prueba
# -------------------------------------------------------------------
cadenas = [
    "aaabbb",      # Cumple con Tipo 3 y Tipo 2
    "aaabbbccc",   # Cumple con Tipo 1
    "abab",        # Cumple con Tipo 0
    "abcabc",      # No cumple con ninguna
    "aaaaabbbbb",  # Cumple con Tipo 3
    "aaaabbbbcccc",# Cumple con Tipo 1
    "abc",         # No cumple con ninguna
    "",            # Cadena vacía
    "aabbcc",      # No cumple con ninguna
    "aaaa"         # No cumple con ninguna
]

# Llama a la función para probar las cadenas.
probar_gramaticas(cadenas)

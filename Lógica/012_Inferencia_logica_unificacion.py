# Algoritmo de Unificación para inferencia lógica
# Este ejemplo unifica términos lógicos simples con variables, constantes y funciones representadas como tuplas.

def es_variable(x):
    """
    Verifica si un término es una variable.
    Una variable es un string que comienza con una letra minúscula.
    Ejemplo:
        - 'x' -> True
        - 'Juan' -> False
    """
    return isinstance(x, str) and x.islower()

def es_constante(x):
    """
    Verifica si un término es una constante.
    Una constante es un string que comienza con una letra mayúscula.
    Ejemplo:
        - 'Juan' -> True
        - 'x' -> False
    """
    return isinstance(x, str) and x[0].isupper()

def unificar(x, y, sustituciones=None):
    """
    Unifica dos expresiones lógicas x e y.
    Parámetros:
        - x, y: Expresiones lógicas que pueden ser variables, constantes o funciones (tuplas).
        - sustituciones: Diccionario que almacena las sustituciones realizadas durante la unificación.
    Retorna:
        - Un diccionario con las sustituciones si la unificación es exitosa.
        - None si la unificación falla.
    """
    if sustituciones is None:
        # Inicializa el diccionario de sustituciones si no se proporciona.
        sustituciones = {}

    # Caso 1: Si x e y son iguales, no se necesita ninguna sustitución.
    if x == y:
        return sustituciones
    # Caso 2: Si x es una variable, intenta unificarla con y.
    elif es_variable(x):
        return unificar_variable(x, y, sustituciones)
    # Caso 3: Si y es una variable, intenta unificarla con x.
    elif es_variable(y):
        return unificar_variable(y, x, sustituciones)
    # Caso 4: Si x e y son funciones (tuplas), unifica sus elementos recursivamente.
    elif isinstance(x, tuple) and isinstance(y, tuple):
        # Si las funciones tienen diferente número de argumentos, no se pueden unificar.
        if len(x) != len(y):
            return None
        # Unifica cada par de elementos de las tuplas.
        for a, b in zip(x, y):
            sustitaciones_nuevas = unificar(a, b, sustituciones)
            if sustitaciones_nuevas is None:
                # Si alguna unificación falla, retorna None.
                return None
            # Actualiza las sustituciones con las nuevas encontradas.
            sustituciones.update(sustitaciones_nuevas)
        return sustituciones
    else:
        # Caso 5: Si no se cumple ninguno de los casos anteriores, la unificación falla.
        return None

def unificar_variable(var, x, sustituciones):
    """
    Maneja la unificación de una variable con otro término.
    Parámetros:
        - var: La variable a unificar.
        - x: El término con el que se intenta unificar la variable.
        - sustituciones: Diccionario con las sustituciones actuales.
    Retorna:
        - Un diccionario actualizado con las nuevas sustituciones si la unificación es exitosa.
        - None si la unificación falla.
    """
    if var in sustituciones:
        # Si la variable ya tiene una sustitución, intenta unificar el valor sustituido con x.
        return unificar(sustituciones[var], x, sustituciones)
    elif x in sustituciones:
        # Si x ya tiene una sustitución, intenta unificar la variable con el valor sustituido.
        return unificar(var, sustituciones[x], sustituciones)
    else:
        # Si la variable no tiene sustitución y no es igual a x, realiza la sustitución.
        if var != x:
            sustituciones[var] = x
        return sustituciones

# Ejemplos de uso
if __name__ == "__main__":
    # Lista de ejemplos para probar el algoritmo de unificación.
    ejemplos = [
        (('padre', 'x'), ('padre', 'Juan')),  # Caso simple: unifica una variable con una constante.
        (('padre', 'x'), ('padre', 'y')),    # Caso con dos variables diferentes.
        (('padre', 'x'), ('madre', 'Juan')), # Caso con funciones diferentes (no se pueden unificar).
        (('padre', ('abuelo', 'x')), ('padre', ('abuelo', 'Juan'))),  # Caso con estructura anidada.
        (('padre', 'x'), ('padre', 'x')),    # Caso donde los términos ya son iguales.
    ]

    # Itera sobre los ejemplos y aplica el algoritmo de unificación.
    for exp1, exp2 in ejemplos:
        print(f"Intentando unificar: {exp1} y {exp2}")
        resultado = unificar(exp1, exp2)
        if resultado:
            # Si la unificación es exitosa, muestra las sustituciones encontradas.
            print("Unificación exitosa. Sustituciones encontradas:")
            print(resultado)
        else:
            # Si la unificación falla, muestra un mensaje indicando el fallo.
            print("No se pudo unificar.")
        print("-" * 40)  # Separador para mayor claridad en la salida.

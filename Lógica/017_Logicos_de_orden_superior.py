# ----------------------------------------
# Lógica de Orden Superior 
# ----------------------------------------

# Lista de elementos sobre los que vamos a razonar
# Cada elemento es un diccionario que representa a una persona con su nombre, edad y profesión
personas = [
    {"nombre": "Ana", "edad": 20, "profesion": "ingeniera"},
    {"nombre": "Luis", "edad": 17, "profesion": "estudiante"},
    {"nombre": "Clara", "edad": 25, "profesion": "doctora"},
    {"nombre": "Pedro", "edad": 30, "profesion": "ingeniero"}
]

# Predicado de orden 1: Verifica si una persona es mayor de edad
def es_mayor_de_edad(persona):
    """
    Devuelve True si la persona tiene 18 años o más, False en caso contrario.
    """
    return persona["edad"] >= 18

# Predicado de orden 1: Verifica si una persona trabaja en ingeniería
def es_ingenieria(persona):
    """
    Devuelve True si la profesión de la persona contiene la palabra "ingenier".
    Esto incluye tanto "ingeniera" como "ingeniero".
    """
    return "ingenier" in persona["profesion"]

# Predicado de orden 1: Verifica si una persona es estudiante
def es_estudiante(persona):
    """
    Devuelve True si la profesión de la persona es exactamente "estudiante".
    """
    return persona["profesion"] == "estudiante"

# Predicado de orden 2: Verifica si todos los elementos de un conjunto cumplen un predicado
def para_todos(predicado, conjunto):
    """
    Aplica el predicado a cada elemento del conjunto.
    Devuelve True si todos los elementos cumplen el predicado, False en caso contrario.
    """
    return all(predicado(x) for x in conjunto)

# Predicado de orden 2: Verifica si al menos un elemento de un conjunto cumple un predicado
def existe(predicado, conjunto):
    """
    Aplica el predicado a cada elemento del conjunto.
    Devuelve True si al menos un elemento cumple el predicado, False en caso contrario.
    """
    return any(predicado(x) for x in conjunto)

# Predicado de orden 2: Combina dos predicados con un operador lógico "y"
def combinar_predicados_y(predicado1, predicado2):
    """
    Devuelve un nuevo predicado que combina dos predicados con una operación lógica "y".
    El nuevo predicado devuelve True solo si ambos predicados son True para un elemento.
    """
    return lambda x: predicado1(x) and predicado2(x)

# Uso de los predicados de orden superior
# Verifica si todos los elementos cumplen con ser mayores de edad
print("¿Todos son mayores de edad?", para_todos(es_mayor_de_edad, personas))

# Verifica si al menos un elemento trabaja en ingeniería
print("¿Al menos uno trabaja en ingeniería?", existe(es_ingenieria, personas))

# Verifica si al menos un elemento es estudiante
print("¿Al menos uno es estudiante?", existe(es_estudiante, personas))

# Ejemplo de combinación de predicados
# Combina los predicados "es mayor de edad" y "trabaja en ingeniería"
es_mayor_y_ingeniero = combinar_predicados_y(es_mayor_de_edad, es_ingenieria)

# Verifica si al menos un elemento cumple con ser mayor de edad y trabajar en ingeniería
print("¿Al menos uno es mayor de edad y trabaja en ingeniería?", existe(es_mayor_y_ingeniero, personas))

# Ejemplo adicional: Filtrar personas que cumplen un predicado
def filtrar(predicado, conjunto):
    """
    Devuelve una lista con los elementos del conjunto que cumplen con el predicado.
    """
    return [x for x in conjunto if predicado(x)]

# Filtra las personas que son mayores de edad
personas_mayores = filtrar(es_mayor_de_edad, personas)
print("Personas mayores de edad:", personas_mayores)

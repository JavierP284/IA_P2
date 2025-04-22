# ---------------------------
# RELACIONES FAMILIARES (versión de Prolog)
# ---------------------------

# Diccionario que contiene los hechos sobre las relaciones familiares.
# Cada clave es un hijo, y el valor es una tupla con los nombres del padre y la madre.
padres = {
    "maria": ("juan", "ana"),
    "jose": ("juan", "ana"),
    "carlos": ("jose", "luisa"),
    "ana": ("pedro", "marta")
}

# Función para determinar si una persona X es hijo de otra persona Y.
def es_hijo(x, y):
    """
    Verifica si X es hijo de Y.
    - x: Nombre del hijo.
    - y: Nombre del posible padre o madre.
    """
    if x in padres:  # Verifica si X está en el diccionario de padres.
        return y in padres[x]  # Comprueba si Y es uno de los padres de X.
    return False  # Si X no está en el diccionario, devuelve False.

# Función para determinar si dos personas son hermanos.
def son_hermanos(x, y):
    """
    Verifica si X y Y son hermanos.
    - x: Nombre de la primera persona.
    - y: Nombre de la segunda persona.
    """
    if x not in padres or y not in padres or x == y:  # Verifica que ambos estén en el diccionario y no sean la misma persona.
        return False
    return padres[x] == padres[y]  # Comprueba si tienen los mismos padres.

# Función para determinar si una persona X es padre de otra persona Y.
def es_padre(x, y):
    """
    Verifica si X es el padre de Y.
    - x: Nombre del posible padre.
    - y: Nombre del hijo.
    """
    for hijo, (padre, madre) in padres.items():  # Recorre el diccionario de padres.
        if hijo == y and padre == x:  # Comprueba si Y es el hijo y X es el padre.
            return True
    return False  # Si no se encuentra la relación, devuelve False.

# Función para determinar si una persona X es abuelo de otra persona Y.
def es_abuelo(x, y):
    """
    Verifica si X es abuelo de Y.
    - x: Nombre del posible abuelo.
    - y: Nombre del nieto.
    """
    for hijo, (padre, madre) in padres.items():  # Recorre el diccionario de padres.
        # Comprueba si X es padre de alguno de los padres de Y.
        if hijo == y and (es_padre(x, padre) or es_padre(x, madre)):
            return True
    return False  # Si no se encuentra la relación, devuelve False.

# Pruebas para verificar las funciones de relaciones familiares.
print("¿Es María hija de Juan?", es_hijo("maria", "juan"))        # True
print("¿José y María son hermanos?", son_hermanos("jose", "maria"))  # True
print("¿Es Juan padre de Carlos?", es_padre("juan", "carlos"))    # False
print("¿Es Pedro abuelo de María?", es_abuelo("pedro", "maria"))  # True


# ---------------------------
# SISTEMA EXPERTO DE BEBIDAS (versión de CLIPS)
# ---------------------------

# Función para recomendar una bebida basada en el clima, la edad y opcionalmente la hora del día.
def recomendar_bebida(clima, edad, hora_del_dia=None):
    """
    Recomienda una bebida basada en las condiciones dadas.
    - clima: Puede ser "frío", "caluroso" u otro.
    - edad: Edad de la persona.
    - hora_del_dia: Opcional, puede ser "mañana", "tarde", etc.
    """
    # Si la persona es un niño (12 años o menos), recomienda bebidas para niños.
    if edad <= 12:
        return "Te recomiendo un jugo natural o leche."
    
    # Si el clima es frío, recomienda bebidas calientes.
    elif clima == "frío":
        if hora_del_dia == "mañana":  # Por la mañana, recomienda café o té caliente.
            return "Te recomiendo un café o té caliente."
        return "Te recomiendo un chocolate caliente."  # En otros momentos, recomienda chocolate caliente.
    
    # Si el clima es caluroso, recomienda bebidas frías.
    elif clima == "caluroso":
        if hora_del_dia == "tarde":  # Por la tarde, recomienda refresco o agua fría.
            return "Te recomiendo un refresco o agua fría."
        return "Te recomiendo una limonada."  # En otros momentos, recomienda limonada.
    
    # Si no se cumplen las condiciones anteriores, no tiene una recomendación específica.
    else:
        return "No tengo una recomendación específica."

# Pruebas para verificar las recomendaciones del sistema experto de bebidas.
print("\nRecomendación para persona de 8 años:")
print(recomendar_bebida("frío", 8))  # Debería recomendar jugo o leche.

print("\nRecomendación para persona de 25 años en clima caluroso:")
print(recomendar_bebida("caluroso", 25, "tarde"))  # Debería recomendar refresco o agua fría.

print("\nRecomendación para persona de 30 años en clima frío por la mañana:")
print(recomendar_bebida("frío", 30, "mañana"))  # Debería recomendar café o té caliente.

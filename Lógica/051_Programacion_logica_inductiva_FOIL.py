# --------------------------------------------------------------------
# Simulación de FOIL (simplificado): Aprender la relación abuelo(X, Z)
# --------------------------------------------------------------------

# Base de hechos: padre(padre, hijo)
# Esta lista representa las relaciones padre-hijo en la base de datos.
hechos_padre = [
    ("juan", "carlos"),   # juan es padre de carlos
    ("carlos", "pedro"),  # carlos es padre de pedro
    ("roberto", "ana"),   # roberto es padre de ana
    ("ana", "lucas")      # ana es padre de lucas
]

# Ejemplos positivos: (abuelo, nieto)
# Estos son los ejemplos que queremos que el sistema aprenda a cubrir.
positivos = [
    ("juan", "pedro"),    # juan es abuelo de pedro (a través de carlos)
    ("roberto", "lucas")  # roberto es abuelo de lucas (a través de ana)
]

# Ejemplos negativos: (abuelo, nieto)
# Estos son ejemplos que NO deberían ser cubiertos por las reglas inducidas.
negativos = [
    ("carlos", "lucas"),  # carlos no es abuelo de lucas
    ("juan", "lucas"),    # juan no es abuelo de lucas
    ("pedro", "lucas")    # pedro no es abuelo de lucas
]

# ----------------------------------------
# Función auxiliar para verificar si abuelo(X,Z)
def es_abuelo(x, z):
    """
    Verifica si existe una relación abuelo(X, Z) basada en los hechos.
    Parámetros:
        x: posible abuelo
        z: posible nieto
    Retorna:
        True si x es abuelo de z, False en caso contrario.
    """
    # Iteramos sobre los hechos para encontrar si x es padre de alguien
    for (a, b) in hechos_padre:
        if a == x:  # Si x es padre de b
            # Buscamos si b es padre de z
            for (c, d) in hechos_padre:
                if b == c and d == z:  # Si b es padre de z
                    return True  # x es abuelo de z
    return False  # No se encontró la relación abuelo

# ----------------------------------------
# Función para verificar ejemplos positivos
def verificar_positivos():
    """
    Verifica si los ejemplos positivos cumplen la relación abuelo(X, Z).
    Imprime un mensaje indicando si cada ejemplo positivo es válido.
    """
    print("\nVerificando ejemplos positivos...")
    for (x, z) in positivos:
        if es_abuelo(x, z):  # Si la relación abuelo(X, Z) es verdadera
            print(f"[OK] ({x}, {z}) es un ejemplo positivo válido.")
        else:  # Si no se cumple la relación
            print(f"[ERROR] ({x}, {z}) no cumple la relación abuelo.")

# ----------------------------------------
# Función para verificar ejemplos negativos
def verificar_negativos():
    """
    Verifica si los ejemplos negativos no cumplen la relación abuelo(X, Z).
    Imprime un mensaje indicando si cada ejemplo negativo es correctamente rechazado.
    """
    print("\nVerificando ejemplos negativos...")
    for (x, z) in negativos:
        if es_abuelo(x, z):  # Si la relación abuelo(X, Z) es verdadera (error)
            print(f"[ERROR] ({x}, {z}) fue cubierto pero es negativo.")
        else:  # Si no se cumple la relación (correcto)
            print(f"[OK] ({x}, {z}) no fue cubierto, como se esperaba.")

# ----------------------------------------
# FOIL simplificado: inducir regla lógica
def inducir_regla_abuelo():
    """
    Induce reglas lógicas para la relación abuelo(X, Z) basada en ejemplos positivos.
    Retorna:
        Una lista de reglas inducidas.
    """
    reglas = []  # Lista para almacenar las reglas inducidas
    print("\nFOIL: Inducción de regla lógica para abuelo(X, Z)\n")

    # Iteramos sobre los ejemplos positivos
    for (x, z) in positivos:
        if es_abuelo(x, z):  # Si la relación abuelo(X, Z) es verdadera
            # Generamos una regla lógica basada en los hechos
            regla = f"abuelo({x}, {z}) :- padre({x}, Y), padre(Y, {z})"
            print(f"Regla encontrada para positivo ({x}, {z}):")
            print(f"   {regla}")
            reglas.append(regla)  # Agregamos la regla a la lista
        else:  # Si no se cumple la relación
            print(f"No se puede inducir regla para ({x}, {z})")

    return reglas  # Retornamos las reglas inducidas

# ----------------------------------------
# Ejecutar FOIL simplificado
print("=== Simulación de FOIL ===")

# Inducimos reglas basadas en los ejemplos positivos
reglas = inducir_regla_abuelo()

# Verificamos los ejemplos positivos
verificar_positivos()

# Verificamos los ejemplos negativos
verificar_negativos()

# Mostramos las reglas inducidas
print("\nReglas inducidas:")
for regla in reglas:
    print(f" - {regla}")

# --------------------------------------------------------
# Espacio de Versiones: Límites S (específico) y G (general)
# --------------------------------------------------------

# Ejemplos de entrenamiento
# Cada ejemplo tiene una lista de atributos y una clase ("sí" o "no").
ejemplos = [
    (["rojo", "pequeño", "redonda"], "sí"),  # Ejemplo positivo
    (["rojo", "mediano", "redonda"], "sí"),  # Ejemplo positivo
    (["verde", "grande", "redonda"], "no"),  # Ejemplo negativo
    (["rojo", "grande", "alargada"], "no"),  # Ejemplo negativo
    (["rojo", "mediano", "redonda"], "sí")   # Ejemplo positivo
]

# Inicializamos S como la hipótesis más específica posible.
# "Ø" indica que no hay información específica aún.
S = ["Ø", "Ø", "Ø"]

# Inicializamos G como la hipótesis más general posible.
# "?" indica que cualquier valor es aceptable.
G = [["?", "?", "?"]]

def es_consistente(h, ejemplo):
    """
    Verifica si la hipótesis h cubre el ejemplo dado.
    Una hipótesis cubre un ejemplo si todos los atributos coinciden
    o si la hipótesis tiene un "?" en esa posición.
    """
    return all(h[i] == "?" or h[i] == ejemplo[i] for i in range(len(h)))

def actualizar_espacio_versiones(ejemplos):
    """
    Actualiza los límites S (más específico) y G (más general) 
    basados en los ejemplos de entrenamiento.
    """
    global S, G  # Usamos las variables globales S y G
    for atributos, clase in ejemplos:
        if clase == "sí":  # Si el ejemplo es positivo
            # Actualizamos S para hacerlo más específico
            for i in range(len(S)):
                if S[i] == "Ø":  # Si no hay información en S, tomamos el valor del ejemplo
                    S[i] = atributos[i]
                elif S[i] != atributos[i]:  # Si hay conflicto, generalizamos con "?"
                    S[i] = "?"
            # Filtramos G para eliminar hipótesis inconsistentes con el ejemplo positivo
            G = [g for g in G if es_consistente(g, atributos)]
        else:  # Si el ejemplo es negativo
            # Necesitamos especializar G para excluir este ejemplo negativo
            G_nueva = []
            for g in G:
                if es_consistente(g, atributos):  # Si g cubre el ejemplo negativo
                    # Generamos nuevas hipótesis más específicas
                    for i in range(len(g)):
                        if g[i] == "?":  # Solo especializamos los atributos generales
                            nuevo = g.copy()
                            nuevo[i] = S[i]  # Usamos el valor específico de S
                            # Agregamos la nueva hipótesis si no cubre el ejemplo negativo
                            if not es_consistente(nuevo, atributos):
                                G_nueva.append(nuevo)
                else:
                    # Si g no cubre el ejemplo negativo, lo mantenemos
                    G_nueva.append(g)
            G = G_nueva  # Actualizamos G con las nuevas hipótesis
        # Mostrar el estado intermedio de S y G después de cada ejemplo
        print(f"Ejemplo: {atributos}, Clase: {clase}")
        print("S:", S)
        print("G:", G)
        print("-" * 40)

# Actualizamos el espacio de versiones con los ejemplos de entrenamiento
actualizar_espacio_versiones(ejemplos)

# Mostramos los resultados finales
print("Hipótesis más específica (S):", S)
print("Hipótesis más generales (G):", G)

# --------------------------------------------------------
# Algoritmo AQ: Generar reglas que cubran los positivos
# --------------------------------------------------------

# Ejemplos positivos y negativos para el algoritmo AQ
positivos = [
    ["rojo", "pequeño", "redonda"],
    ["rojo", "mediano", "redonda"],
    ["rojo", "mediano", "redonda"]
]

negativos = [
    ["verde", "grande", "redonda"],
    ["rojo", "grande", "alargada"]
]

def cubre_regla(regla, ejemplo):
    """
    Verifica si una regla cubre un ejemplo.
    Una regla cubre un ejemplo si todos los atributos coinciden
    o si la regla tiene un "?" en esa posición.
    """
    return all(r == "?" or r == e for r, e in zip(regla, ejemplo))

def generar_reglas(positivos, negativos):
    """
    Genera reglas específicas que cubren todos los ejemplos positivos
    y excluyen todos los ejemplos negativos.
    """
    reglas = []
    for pos in positivos:  # Iteramos sobre cada ejemplo positivo
        candidatos = []
        for i in range(len(pos)):  # Para cada atributo del ejemplo positivo
            for val in set(p[i] for p in positivos):  # Consideramos todos los valores posibles
                regla = ["?"] * len(pos)  # Creamos una regla general
                regla[i] = val  # Especificamos el valor en la posición i
                # Verificamos que la regla cubra todos los positivos y excluya los negativos
                if all(cubre_regla(regla, p) for p in positivos) and all(not cubre_regla(regla, n) for n in negativos):
                    candidatos.append(regla)
        reglas.extend(candidatos)  # Agregamos los candidatos a la lista de reglas
    # Eliminamos reglas duplicadas
    reglas_unicas = []
    for r in reglas:
        if r not in reglas_unicas:
            reglas_unicas.append(r)
    return reglas_unicas

# Generamos y mostramos las reglas aprendidas por el algoritmo AQ
reglas_aprendidas = generar_reglas(positivos, negativos)
print("\nReglas aprendidas por AQ:")
for r in reglas_aprendidas:
    print(" -", r)


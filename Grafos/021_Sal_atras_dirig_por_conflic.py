# Definimos un problema de satisfacción de restricciones (CSP)
# usando el algoritmo de Salto Atrás Dirigido por Conflictos (CBJ).

# Diccionario que representa las regiones y sus vecinos
mapa = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

# Lista de colores disponibles
colores = ['Rojo', 'Verde', 'Azul']

def es_valida(region, color, asignacion):
    """
    Verifica si asignar 'color' a 'region' es válido.
    No debe haber conflictos con los vecinos ya asignados.
    """
    for vecino in mapa[region]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False  # Hay conflicto si un vecino ya tiene el mismo color
    return True

def salto_atras_conflicto(asignacion, orden, conflictos, indice):
    """
    Algoritmo de Salto Atrás Dirigido por Conflictos (CBJ).
    """
    if indice == len(orden):  # Si todas las regiones tienen color, terminamos
        return asignacion

    region = orden[indice]  # Seleccionamos la región actual a colorear

    for color in colores:
        if es_valida(region, color, asignacion):
            asignacion[region] = color  # Asignamos el color
            conflictos[indice] = set()  # Limpiamos conflictos previos
            resultado = salto_atras_conflicto(asignacion, orden, conflictos, indice + 1)
            if resultado:
                return resultado  # Si encontramos solución, la retornamos
            asignacion.pop(region)  # Si no funcionó, eliminamos la asignación

    # Si ningún color funciona, identificamos el conflicto
    conflicto_salto = max(conflictos[indice], default=0)
    conflictos[indice - 1].add(conflicto_salto)  # Guardamos el conflicto en la región anterior
    return None if conflicto_salto == 0 else salto_atras_conflicto(asignacion, orden, conflictos, conflicto_salto)

# Definimos el orden de las regiones a colorear
orden_regiones = list(mapa.keys())

# Ejecutamos el algoritmo CBJ
solucion = salto_atras_conflicto({}, orden_regiones, [set() for _ in orden_regiones], 0)

# Mostramos el resultado
if solucion:
    print("Coloreo válido encontrado:")
    for region, color in solucion.items():
        print(f"Región {region} -> Color {color}")
else:
    print("No se encontró solución")

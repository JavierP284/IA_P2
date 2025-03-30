# Definimos un problema de satisfacción de restricciones (CSP)
# en el que se colorea un mapa sin que dos regiones vecinas tengan el mismo color.

# Definimos un diccionario con las regiones y sus vecinos
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
    for vecino in mapa[region]:  # Recorremos los vecinos de la región
        if vecino in asignacion and asignacion[vecino] == color:
            return False  # No es válido si un vecino ya tiene el mismo color
    return True  # Si no hay conflictos, la asignación es válida

def backtracking(asignacion):
    """
    Algoritmo de backtracking para asignar colores al mapa.
    """
    if len(asignacion) == len(mapa):  # Si todas las regiones tienen color, terminamos
        return asignacion

    # Elegimos la siguiente región sin asignación
    for region in mapa:
        if region not in asignacion:  # Si aún no ha sido coloreada
            for color in colores:  # Probamos cada color disponible
                if es_valida(region, color, asignacion):
                    asignacion[region] = color  # Asignamos el color
                    resultado = backtracking(asignacion)  # Llamado recursivo
                    if resultado:  # Si encontramos una solución, la retornamos
                        return resultado
                    asignacion.pop(region)  # Si no funcionó, deshacemos la asignación
            return None  # Si ningún color es válido, retrocedemos (Backtracking)
    
    return None  # Si no hay solución, retornamos None

# Ejecutamos el algoritmo
solucion = backtracking({})
if solucion:
    print("Coloreo válido encontrado:")
    for region, color in solucion.items():
        print(f"Región {region} -> Color {color}")
else:
    print("No se encontró solución")

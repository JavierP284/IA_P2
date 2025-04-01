# Definir los estados posibles del mercado y sus probabilidades
eventos = {
    "Alta demanda": 0.7,  # Probabilidad del 70%
    "Baja demanda": 0.3   # Probabilidad del 30%
}

if sum(eventos.values()) != 1:
    raise ValueError("Las probabilidades de los eventos deben sumar 1.")

# Definir las utilidades asociadas a cada decisión y resultado
utilidades = {
    "Lanzar": {
        "Alta demanda": 100000,  # Ganancia si la demanda es alta
        "Baja demanda": -50000   # Pérdida si la demanda es baja
    },
    "No lanzar": {
        "Alta demanda": 0,  # No hay ganancia ni pérdida
        "Baja demanda": 0
    }
}

# Calcular la utilidad esperada para cada decisión
def utilidad_esperada(decision):
    """
    Calcula la utilidad esperada de una decisión.
    
    Parámetros:
    - decision: "Lanzar" o "No lanzar"

    Retorna:
    - Valor de la utilidad esperada.
    """
    utilidad_total = 0
    for estado, probabilidad in eventos.items():
        utilidad_total += probabilidad * utilidades[decision][estado]
    return utilidad_total

# Evaluar ambas opciones
utilidad_lanzar = utilidad_esperada("Lanzar")
utilidad_no_lanzar = utilidad_esperada("No lanzar")

# Elegir la mejor decisión
mejor_decision = "Lanzar" if utilidad_lanzar > utilidad_no_lanzar else "No lanzar"

# Mostrar los resultados
print(f"Utilidad esperada de lanzar el producto: ${utilidad_lanzar:,.2f}")
print(f"Utilidad esperada de NO lanzar el producto: ${utilidad_no_lanzar:,.2f}")
print(f"\nMejor decisión recomendada: {mejor_decision}")

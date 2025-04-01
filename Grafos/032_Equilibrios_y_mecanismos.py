import numpy as np
import nashpy as nash  # Librería para teoría de juegos

# Definimos las matrices de pagos para los jugadores A y B
pago_jugador_A = np.array([[3, 1],   # Jugador A elige Arriba
                           [5, 2]])  # Jugador A elige Abajo

pago_jugador_B = np.array([[3, 5],   # Jugador B elige Izquierda
                           [1, 2]])  # Jugador B elige Derecha

# Validar que las matrices de pago tienen las mismas dimensiones
if pago_jugador_A.shape != pago_jugador_B.shape:
    raise ValueError("Las matrices de pago deben tener las mismas dimensiones.")

# Crear el juego bimatriz
juego = nash.Game(pago_jugador_A, pago_jugador_B)

# Encontrar equilibrios de Nash
equilibrios = list(juego.support_enumeration())

# Mostrar los equilibrios encontrados
print("\nEquilibrios de Nash encontrados:")
if equilibrios:
    for i, eq in enumerate(equilibrios, start=1):
        print(f"\nEquilibrio {i}:")
        print(f"  Estrategia Jugador A: {eq[0]}")
        print(f"  Estrategia Jugador B: {eq[1]}")
else:
    print("No se encontraron equilibrios de Nash.")

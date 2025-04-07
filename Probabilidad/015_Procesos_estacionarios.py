import numpy as np

# -------------------------------
# 🔢 Paso 1: Definir la matriz de transición
# -------------------------------
# Ejemplo: Estados
# A: Descansando, B: Trabajando, C: Vacaciones
P = np.array([
    [0.7, 0.2, 0.1],  # Transiciones desde el estado A
    [0.3, 0.4, 0.3],  # Transiciones desde el estado B
    [0.2, 0.3, 0.5]   # Transiciones desde el estado C
])

# Validar que la matriz de transición es estocástica
if not np.allclose(P.sum(axis=1), 1):
    raise ValueError("La matriz de transición no es estocástica. Las filas deben sumar 1.")

# -------------------------------
# 🔄 Paso 2: Iterar hasta encontrar el estado estacionario
# -------------------------------
def encontrar_estado_estacionario(P, tol=1e-8, max_iter=1000, verbose=False):
    """
    Encuentra el estado estacionario de una cadena de Markov.

    Args:
        P (np.ndarray): Matriz de transición.
        tol (float): Tolerancia para la convergencia.
        max_iter (int): Número máximo de iteraciones.
        verbose (bool): Si es True, imprime la evolución del estado.

    Returns:
        np.ndarray: Distribución estacionaria.
    """
    # Empezamos con una distribución uniforme inicial
    estado = np.array([1/3, 1/3, 1/3])  # [π_A, π_B, π_C]

    for i in range(max_iter):
        nuevo_estado = np.dot(estado, P)  # π * P

        # Mostrar la evolución del estado si verbose=True
        if verbose:
            print(f"Iteración {i+1}: {nuevo_estado}")

        # Revisamos si ya estamos suficientemente cerca del equilibrio
        if np.linalg.norm(nuevo_estado - estado) < tol:
            print(f"Convergencia alcanzada en {i+1} iteraciones.")
            return nuevo_estado

        estado = nuevo_estado  # Actualizamos el estado

    print("No se alcanzó la convergencia.")
    return estado

# -------------------------------
# 🖨️ Paso 3: Ejecutar y mostrar resultado
# -------------------------------
estado_estacionario = encontrar_estado_estacionario(P, verbose=True)
print("\nDistribución estacionaria:")
print(f"π_A (Descansando): {estado_estacionario[0]:.4f}")
print(f"π_B (Trabajando):  {estado_estacionario[1]:.4f}")
print(f"π_C (Vacaciones):  {estado_estacionario[2]:.4f}")

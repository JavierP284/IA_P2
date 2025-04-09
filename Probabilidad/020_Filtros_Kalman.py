import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# 1. Inicialización del modelo
# -------------------------------

def inicializar_modelo():
    dt = 1  # Paso de tiempo (1 segundo)

    # Estado inicial: posición = 0, velocidad = 1
    x = np.array([[0], [1]])  # [posición, velocidad]

    # Matriz de transición del estado A (modelo del sistema)
    A = np.array([
        [1, dt],
        [0, 1]
    ])

    # Matriz de observación H (solo se mide la posición)
    H = np.array([[1, 0]])

    # Matriz de covarianza del proceso (incertidumbre del modelo)
    Q = np.array([
        [1, 0],
        [0, 1]
    ])

    # Matriz de covarianza de medición (ruido del sensor)
    R = np.array([[4]])

    # Matriz de covarianza del error estimado (inicial)
    P = np.eye(2)

    return x, A, H, Q, R, P

# -------------------------------
# 2. Funciones del Filtro de Kalman
# -------------------------------

def filtro_kalman(z_mediciones, x, A, H, Q, R, P):
    """
    Aplica el filtro de Kalman a una serie de mediciones ruidosas.

    Args:
        z_mediciones: Lista de mediciones ruidosas.
        x: Estado inicial.
        A, H, Q, R, P: Matrices del modelo de Kalman.

    Returns:
        Lista de estimaciones del estado.
    """
    estimaciones = []

    for z in z_mediciones:
        # -------- PREDICCIÓN --------
        x_pred = A @ x
        P_pred = A @ P @ A.T + Q

        # -------- ACTUALIZACIÓN --------
        z = np.array([[z]])  # Convertir medición a columna
        y = z - H @ x_pred  # Residuo de innovación
        S = H @ P_pred @ H.T + R  # Incertidumbre de la innovación
        K = P_pred @ H.T @ np.linalg.inv(S)  # Ganancia de Kalman

        x = x_pred + K @ y  # Estado corregido
        P = (np.eye(2) - K @ H) @ P_pred  # Covarianza corregida

        estimaciones.append(x.copy())

    return estimaciones

# -------------------------------
# 3. Generar mediciones ruidosas de posición
# -------------------------------

np.random.seed(0)
posicion_real = [i for i in range(20)]  # Posiciones reales de 0 a 19
mediciones = [p + np.random.normal(0, 2) for p in posicion_real]  # Con ruido

# Inicializar modelo
x, A, H, Q, R, P = inicializar_modelo()

# Aplicar filtro de Kalman a las mediciones
estimaciones = filtro_kalman(mediciones, x, A, H, Q, R, P)

# -------------------------------
# 4. Visualización de resultados
# -------------------------------

# Extraer estimaciones de posición y velocidad
estimaciones_pos = [est[0, 0] for est in estimaciones]
estimaciones_vel = [est[1, 0] for est in estimaciones]

# Graficar resultados
plt.figure(figsize=(10, 6))
plt.plot(posicion_real, label="Posición Real", linestyle="--", marker="o")
plt.plot(mediciones, label="Mediciones Ruidosas", linestyle=":", marker="x")
plt.plot(estimaciones_pos, label="Estimación de Posición", marker="s")
plt.xlabel("Tiempo")
plt.ylabel("Posición")
plt.title("Filtro de Kalman - Estimación de Posición")
plt.legend()
plt.grid()
plt.show()

# Mostrar resultados en consola
print("Tiempo | Medición | Estimación Pos | Estimación Vel")
for t in range(len(mediciones)):
    est = estimaciones[t]
    print(f"{t:6d} | {mediciones[t]:8.2f} | {est[0,0]:14.2f} | {est[1,0]:14.2f}")

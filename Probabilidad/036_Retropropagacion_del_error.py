import numpy as np
import matplotlib.pyplot as plt

# Función de activación sigmoide y su derivada
def sigmoid(x):
    """Calcula la función sigmoide."""
    return 1 / (1 + np.exp(-x))

def derivada_sigmoid(x):
    """Calcula la derivada de la función sigmoide."""
    return x * (1 - x)  # x ya es sigmoid(x), evita recalcular

def propagacion_hacia_adelante(entradas, pesos_entrada_oculta, pesos_oculta_salida):
    """Realiza la propagación hacia adelante."""
    capa_oculta_entrada = np.dot(entradas, pesos_entrada_oculta)
    capa_oculta_salida = sigmoid(capa_oculta_entrada)
    salida_final = sigmoid(np.dot(capa_oculta_salida, pesos_oculta_salida))
    return capa_oculta_salida, salida_final

def retropropagacion(entradas, salidas, capa_oculta_salida, salida_final, pesos_entrada_oculta, pesos_oculta_salida, tasa_aprendizaje):
    """Realiza la retropropagación del error y actualiza los pesos."""
    # Cálculo del error
    error = salidas - salida_final

    # Derivadas para retropropagación
    delta_salida = error * derivada_sigmoid(salida_final)
    error_oculta = delta_salida.dot(pesos_oculta_salida.T)
    delta_oculta = error_oculta * derivada_sigmoid(capa_oculta_salida)

    # Actualización de pesos
    pesos_oculta_salida += capa_oculta_salida.T.dot(delta_salida) * tasa_aprendizaje
    pesos_entrada_oculta += entradas.T.dot(delta_oculta) * tasa_aprendizaje

    return pesos_entrada_oculta, pesos_oculta_salida, np.mean(np.abs(error))

# Entradas y salidas para la compuerta XOR
entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
salidas = np.array([[0], [1], [1], [0]])

# Semilla para reproducibilidad
np.random.seed(42)

# Inicialización de pesos
pesos_entrada_oculta = np.random.uniform(size=(2, 2))
pesos_oculta_salida = np.random.uniform(size=(2, 1))

# Hiperparámetros
tasa_aprendizaje = 0.5
épocas = 10000

# Almacenar errores para graficar
errores = []

# Entrenamiento
for epoca in range(épocas):
    # Propagación hacia adelante
    capa_oculta_salida, salida_final = propagacion_hacia_adelante(entradas, pesos_entrada_oculta, pesos_oculta_salida)

    # Retropropagación
    pesos_entrada_oculta, pesos_oculta_salida, error_promedio = retropropagacion(
        entradas, salidas, capa_oculta_salida, salida_final, pesos_entrada_oculta, pesos_oculta_salida, tasa_aprendizaje
    )

    # Almacenar error
    errores.append(error_promedio)

    # Mostrar error cada 1000 épocas
    if epoca % 1000 == 0:
        print(f"Época {epoca}, Error promedio: {error_promedio:.4f}")

# Visualización del error
plt.plot(errores)
plt.title("Evolución del error durante el entrenamiento")
plt.xlabel("Épocas")
plt.ylabel("Error promedio")
plt.show()

# Pruebas finales
print("\nPrueba final del modelo:")
for i in range(len(entradas)):
    entrada = entradas[i]
    capa_oculta_salida, salida = propagacion_hacia_adelante(entrada, pesos_entrada_oculta, pesos_oculta_salida)
    print(f"Entrada: {entrada} → Salida estimada: {salida[0]:.4f}")

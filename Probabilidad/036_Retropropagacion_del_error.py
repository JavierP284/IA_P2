import numpy as np
import matplotlib.pyplot as plt

# Función de activación sigmoide y su derivada
def sigmoid(x):
    """Calcula la función sigmoide.
    Convierte cualquier valor en un rango entre 0 y 1.
    """
    return 1 / (1 + np.exp(-x))

def derivada_sigmoid(x):
    """Calcula la derivada de la función sigmoide.
    Se utiliza para calcular los gradientes durante la retropropagación.
    """
    return x * (1 - x)  # x ya es sigmoid(x), evita recalcular

def propagacion_hacia_adelante(entradas, pesos_entrada_oculta, pesos_oculta_salida):
    """Realiza la propagación hacia adelante.
    Calcula las salidas de la capa oculta y la salida final del modelo.
    """
    # Calcular la entrada y salida de la capa oculta
    capa_oculta_entrada = np.dot(entradas, pesos_entrada_oculta)  # Producto punto entre entradas y pesos
    capa_oculta_salida = sigmoid(capa_oculta_entrada)  # Aplicar función sigmoide

    # Calcular la salida final
    salida_final = sigmoid(np.dot(capa_oculta_salida, pesos_oculta_salida))  # Producto punto con pesos de salida
    return capa_oculta_salida, salida_final

def retropropagacion(entradas, salidas, capa_oculta_salida, salida_final, pesos_entrada_oculta, pesos_oculta_salida, tasa_aprendizaje):
    """Realiza la retropropagación del error y actualiza los pesos.
    Ajusta los pesos del modelo para minimizar el error.
    """
    # Cálculo del error entre la salida deseada y la salida obtenida
    error = salidas - salida_final

    # Calcular el gradiente de la salida (delta de salida)
    delta_salida = error * derivada_sigmoid(salida_final)

    # Propagar el error hacia la capa oculta
    error_oculta = delta_salida.dot(pesos_oculta_salida.T)  # Error proyectado hacia atrás
    delta_oculta = error_oculta * derivada_sigmoid(capa_oculta_salida)  # Gradiente de la capa oculta

    # Actualizar los pesos de la capa oculta a la salida
    pesos_oculta_salida += capa_oculta_salida.T.dot(delta_salida) * tasa_aprendizaje

    # Actualizar los pesos de las entradas a la capa oculta
    pesos_entrada_oculta += entradas.T.dot(delta_oculta) * tasa_aprendizaje

    # Retornar los pesos actualizados y el error promedio
    return pesos_entrada_oculta, pesos_oculta_salida, np.mean(np.abs(error))

# Entradas y salidas para la compuerta XOR
# Entradas: combinaciones de 0 y 1
# Salidas: resultado esperado de la compuerta XOR
entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
salidas = np.array([[0], [1], [1], [0]])

# Semilla para reproducibilidad
np.random.seed(42)

# Inicialización de pesos con valores aleatorios
# Pesos entre la capa de entrada y la capa oculta
pesos_entrada_oculta = np.random.uniform(size=(2, 2))
# Pesos entre la capa oculta y la capa de salida
pesos_oculta_salida = np.random.uniform(size=(2, 1))

# Hiperparámetros
tasa_aprendizaje = 0.5  # Velocidad de aprendizaje
épocas = 10000  # Número de iteraciones de entrenamiento

# Lista para almacenar los errores en cada época
errores = []

# Entrenamiento del modelo
for epoca in range(épocas):
    # Propagación hacia adelante: calcular salidas intermedias y finales
    capa_oculta_salida, salida_final = propagacion_hacia_adelante(entradas, pesos_entrada_oculta, pesos_oculta_salida)

    # Retropropagación: ajustar los pesos en función del error
    pesos_entrada_oculta, pesos_oculta_salida, error_promedio = retropropagacion(
        entradas, salidas, capa_oculta_salida, salida_final, pesos_entrada_oculta, pesos_oculta_salida, tasa_aprendizaje
    )

    # Almacenar el error promedio de la época actual
    errores.append(error_promedio)

    # Mostrar el error cada 1000 épocas para monitorear el progreso
    if epoca % 1000 == 0:
        print(f"Época {epoca}, Error promedio: {error_promedio:.4f}")

# Visualización del error durante el entrenamiento
plt.plot(errores)
plt.title("Evolución del error durante el entrenamiento")
plt.xlabel("Épocas")
plt.ylabel("Error promedio")
plt.show()

# Pruebas finales del modelo entrenado
print("\nPrueba final del modelo:")
for i in range(len(entradas)):
    entrada = entradas[i]
    # Realizar propagación hacia adelante para cada entrada
    capa_oculta_salida, salida = propagacion_hacia_adelante(entrada, pesos_entrada_oculta, pesos_oculta_salida)
    # Mostrar la entrada y la salida estimada
    print(f"Entrada: {entrada} → Salida estimada: {salida[0]:.4f}")

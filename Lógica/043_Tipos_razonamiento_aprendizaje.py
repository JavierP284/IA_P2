# ----------------------------------------------------------------
# Tipos de Razonamiento y Aprendizaje: Diagnóstico de enfermedades
# ----------------------------------------------------------------

# Importamos las bibliotecas necesarias
from sklearn.tree import DecisionTreeClassifier  # Para aprendizaje supervisado
from sklearn.cluster import KMeans  # Para aprendizaje no supervisado
import matplotlib.pyplot as plt  # Para visualización de datos

# ------------------------
# Razonamiento Deductivo
def razonamiento_deductivo(sintomas):
    """
    Realiza razonamiento deductivo basado en reglas generales.
    Entrada:
        sintomas (list): Lista de síntomas observados.
    Salida:
        str: Diagnóstico basado en las reglas.
    """
    # Si los síntomas incluyen fiebre y tos, se diagnostica gripe
    if "fiebre" in sintomas and "tos" in sintomas:
        return "gripe"
    # Si no se cumplen las reglas, el diagnóstico no está determinado
    return "no determinado"

# ------------------------
# Razonamiento Abductivo
def razonamiento_abductivo(observacion):
    """
    Realiza razonamiento abductivo para encontrar la mejor explicación.
    Entrada:
        observacion (list): Lista de observaciones.
    Salida:
        str: Explicación probable.
    """
    # Si se observa fiebre, se asume que puede haber una infección
    if "fiebre" in observacion:
        return "posible infección"
    # Si no hay observaciones claras, la causa es desconocida
    return "causa desconocida"

# ------------------------
# Razonamiento Inductivo (Aprendizaje Supervisado)
def razonamiento_inductivo():
    """
    Realiza razonamiento inductivo utilizando un modelo supervisado.
    Salida:
        str: Predicción del diagnóstico para un nuevo paciente.
    """
    # Datos de entrenamiento (X: características, y: etiquetas)
    # Cada fila representa un paciente con características:
    # [fiebre, tos, dolor de cabeza]
    X = [
        [1, 1, 0],  # gripe
        [1, 1, 1],  # gripe
        [0, 1, 1],  # resfriado
        [0, 0, 1],  # migraña
        [0, 0, 0]   # sano
    ]
    y = ["gripe", "gripe", "resfriado", "migraña", "sano"]

    # Creamos y entrenamos un clasificador de árbol de decisión
    clf = DecisionTreeClassifier()
    clf.fit(X, y)

    # Nuevo paciente con fiebre y tos, pero sin dolor de cabeza
    nuevo_paciente = [[1, 1, 0]]
    # Predicción del diagnóstico para el nuevo paciente
    prediccion = clf.predict(nuevo_paciente)
    return prediccion[0]

# ------------------------
# Aprendizaje No Supervisado (Agrupamiento)
def aprendizaje_no_supervisado():
    """
    Realiza agrupamiento no supervisado utilizando k-means.
    Salida:
        int: Grupo asignado al nuevo paciente.
    """
    # Datos de entrada: cada punto representa un paciente con características:
    # [fiebre, tos]
    datos = [
        [1, 1], [1, 0], [0, 1], [0, 0], [1, 1], [0, 0]
    ]

    # Creamos un modelo k-means con 2 clusters
    modelo = KMeans(n_clusters=2, n_init=10)
    modelo.fit(datos)

    # Nuevo paciente con fiebre y tos
    nuevo = [[1, 1]]
    # Asignamos el grupo al que pertenece el nuevo paciente
    grupo = modelo.predict(nuevo)
    
    # Visualización de los clusters
    plt.scatter([d[0] for d in datos], [d[1] for d in datos], c=modelo.labels_, cmap='viridis')
    plt.scatter(nuevo[0][0], nuevo[0][1], c='red', marker='x', label='Nuevo paciente')
    plt.title("Clustering de síntomas")
    plt.xlabel("Fiebre")
    plt.ylabel("Tos")
    plt.legend()
    plt.show()

    return grupo[0]

# ------------------------
# Ejecutar ejemplos
if __name__ == "__main__":
    # Ejemplo de razonamiento deductivo
    print("Razonamiento Deductivo:")
    print("Resultado:", razonamiento_deductivo(["fiebre", "tos"]))

    # Ejemplo de razonamiento abductivo
    print("\nRazonamiento Abductivo:")
    print("Resultado:", razonamiento_abductivo(["fiebre"]))

    # Ejemplo de razonamiento inductivo (aprendizaje supervisado)
    print("\nRazonamiento Inductivo (supervisado):")
    print("Resultado:", razonamiento_inductivo())

    # Ejemplo de aprendizaje no supervisado (k-means)
    print("\nAprendizaje No Supervisado (k-means):")
    print("Grupo asignado:", aprendizaje_no_supervisado())

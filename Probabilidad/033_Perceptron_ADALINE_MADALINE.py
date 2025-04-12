import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score, confusion_matrix

# Función para graficar los datos y las fronteras de decisión
def graficar_frontera_decision(X, y, modelo, titulo):
    """
    Grafica los datos y la frontera de decisión de un modelo.
    
    Args:
        X (ndarray): Datos de entrada.
        y (ndarray): Etiquetas de salida.
        modelo: Modelo entrenado con un método `predict` o `predecir`.
        titulo (str): Título del gráfico.
    """
    # Definimos los límites del gráfico
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))
    
    # Verificamos si el modelo tiene el método `predict` o `predecir`
    if hasattr(modelo, 'predict'):
        Z = modelo.predict(np.c_[xx.ravel(), yy.ravel()])
    elif hasattr(modelo, 'predecir'):
        Z = modelo.predecir(np.c_[xx.ravel(), yy.ravel()])
    else:
        raise AttributeError("El modelo no tiene un método 'predict' o 'predecir'.")
    
    # Damos forma a los resultados para graficar
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.8, cmap='coolwarm')  # Frontera de decisión
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', cmap='coolwarm')  # Datos
    plt.title(titulo)
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.show()

# Generamos datos de ejemplo para clasificación binaria
X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_clusters_per_class=1, random_state=42)

# Dividimos los datos en entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.3, random_state=42)

# Normalizamos los datos para que tengan media 0 y desviación estándar 1
escalador = StandardScaler()
X_entrenamiento = escalador.fit_transform(X_entrenamiento)
X_prueba = escalador.transform(X_prueba)

# ** Perceptrón **
# Creamos un modelo Perceptrón con un máximo de 1000 iteraciones y tolerancia de 1e-3
modelo_perceptron = Perceptron(max_iter=1000, tol=1e-3)
modelo_perceptron.fit(X_entrenamiento, y_entrenamiento)  # Entrenamos el modelo
predicciones_perceptron = modelo_perceptron.predict(X_prueba)  # Realizamos predicciones
print(f"Precisión del Perceptrón: {accuracy_score(y_prueba, predicciones_perceptron):.2f}")
graficar_frontera_decision(X_prueba, y_prueba, modelo_perceptron, "Frontera de decisión del Perceptrón")

# ** ADALINE **
class AdalineGD:
    """
    Implementación del algoritmo ADALINE (Adaptive Linear Neuron) con descenso de gradiente.
    """
    def __init__(self, tasa_aprendizaje=0.01, epocas=50):
        """
        Inicializa el modelo ADALINE.
        
        Args:
            tasa_aprendizaje (float): Tasa de aprendizaje para el descenso de gradiente.
            epocas (int): Número de épocas de entrenamiento.
        """
        self.tasa_aprendizaje = tasa_aprendizaje
        self.epocas = epocas

    def entrenar(self, X, y):
        """
        Entrena el modelo ADALINE utilizando descenso de gradiente.
        
        Args:
            X (ndarray): Datos de entrada.
            y (ndarray): Etiquetas de salida.
        """
        self.pesos = np.zeros(1 + X.shape[1])  # Inicializamos los pesos en 0
        self.errores = []  # Lista para almacenar el costo en cada época

        for _ in range(self.epocas):
            neto = self.net_input(X)  # Calculamos la entrada neta
            salida = self.activacion(neto)  # Aplicamos la función de activación (lineal)
            errores = y - salida  # Calculamos los errores
            # Actualizamos los pesos
            self.pesos[1:] += self.tasa_aprendizaje * X.T.dot(errores)
            self.pesos[0] += self.tasa_aprendizaje * errores.sum()
            # Calculamos el costo (error cuadrático medio)
            costo = (errores**2).mean() / 2.0
            self.errores.append(costo)

    def net_input(self, X):
        """
        Calcula la entrada neta.
        
        Args:
            X (ndarray): Datos de entrada.
        
        Returns:
            ndarray: Entrada neta.
        """
        return np.dot(X, self.pesos[1:]) + self.pesos[0]

    def activacion(self, X):
        """
        Función de activación lineal.
        
        Args:
            X (ndarray): Entrada neta.
        
        Returns:
            ndarray: Salida activada.
        """
        return X

    def predecir(self, X):
        """
        Realiza predicciones utilizando el modelo entrenado.
        
        Args:
            X (ndarray): Datos de entrada.
        
        Returns:
            ndarray: Predicciones (0 o 1).
        """
        return np.where(self.activacion(self.net_input(X)) >= 0.0, 1, 0)

# Entrenamos y evaluamos ADALINE
modelo_adaline = AdalineGD(tasa_aprendizaje=0.01, epocas=50)
modelo_adaline.entrenar(X_entrenamiento, y_entrenamiento)
predicciones_adaline = modelo_adaline.predecir(X_prueba)
print(f"Precisión de ADALINE: {accuracy_score(y_prueba, predicciones_adaline):.2f}")
graficar_frontera_decision(X_prueba, y_prueba, modelo_adaline, "Frontera de decisión de ADALINE")

# ** MADALINE (simulada) **
# Creamos dos ADALINE con subconjuntos diferentes de entrenamiento
midpoint = len(X_entrenamiento) // 2
adaline1 = AdalineGD()
adaline2 = AdalineGD()
adaline1.entrenar(X_entrenamiento[:midpoint], y_entrenamiento[:midpoint])
adaline2.entrenar(X_entrenamiento[midpoint:], y_entrenamiento[midpoint:])

# Promediamos las salidas (votación)
salida1 = adaline1.predecir(X_prueba)
salida2 = adaline2.predecir(X_prueba)
predicciones_madaline = (salida1 + salida2) >= 1  # mayoría de votos
print(f"Precisión de MADALINE (simulada): {accuracy_score(y_prueba, predicciones_madaline):.2f}")
graficar_frontera_decision(X_prueba, y_prueba, modelo_adaline, "Frontera de decisión de MADALINE")

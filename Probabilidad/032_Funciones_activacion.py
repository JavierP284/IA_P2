import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Oculta mensajes de información y advertencias de TensorFlow

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

# Función para generar y visualizar los datos
def generar_datos():
    """
    Genera un conjunto de datos con forma de luna y los visualiza en un gráfico.
    """
    # Generamos los datos con ruido para simular un problema no lineal
    X, y = make_moons(n_samples=1000, noise=0.2, random_state=0)
    
    # Graficamos los datos generados
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', s=10)
    plt.title("Datos generados (forma de luna)")
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.show()
    
    return X, y

# Función para construir y entrenar el modelo
def construir_y_entrenar_modelo(funcion_activacion, X_entrenamiento, y_entrenamiento, X_prueba, y_prueba):
    """
    Construye y entrena un modelo de red neuronal con una función de activación específica.
    
    Args:
        funcion_activacion (str): Nombre de la función de activación a usar en la capa oculta.
        X_entrenamiento (ndarray): Datos de entrada para entrenamiento.
        y_entrenamiento (ndarray): Etiquetas de salida para entrenamiento.
        X_prueba (ndarray): Datos de entrada para prueba.
        y_prueba (ndarray): Etiquetas de salida para prueba.
    
    Returns:
        precision (float): Precisión del modelo en los datos de prueba.
        historia (History): Objeto que contiene el historial de entrenamiento.
    """
    # Creamos el modelo secuencial
    modelo = Sequential([
        Input(shape=(2,)),  # Capa de entrada con 2 características
        Dense(8, activation=funcion_activacion),  # Capa oculta con 8 neuronas y la función de activación especificada
        Dense(1, activation='sigmoid')  # Capa de salida con activación sigmoide para clasificación binaria
    ])
    
    # Compilamos el modelo con el optimizador Adam y la función de pérdida binaria
    modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    # Entrenamos el modelo con los datos de entrenamiento
    historia = modelo.fit(X_entrenamiento, y_entrenamiento, epochs=50, verbose=0)  # Entrenamiento silencioso (verbose=0)
    
    # Evaluamos el modelo con los datos de prueba
    perdida, precision = modelo.evaluate(X_prueba, y_prueba, verbose=0)
    
    # Mostramos los resultados de la evaluación
    print(f"Función de activación: {funcion_activacion} - Precisión: {precision*100:.2f}% - Pérdida: {perdida:.4f}")
    
    return precision, historia

# Función para graficar la precisión de cada función de activación
def graficar_resultados(funciones, precisiones):
    """
    Grafica la precisión obtenida para cada función de activación probada.
    
    Args:
        funciones (list): Lista de nombres de funciones de activación.
        precisiones (list): Lista de precisiones correspondientes a cada función de activación.
    """
    # Creamos un gráfico de barras para comparar las precisiones
    plt.bar(funciones, precisiones, color='skyblue')
    plt.title("Precisión por función de activación")
    plt.xlabel("Función de activación")
    plt.ylabel("Precisión (%)")
    plt.ylim(0, 100)  # Establecemos el rango del eje Y entre 0 y 100
    plt.show()

# Generamos los datos
X, y = generar_datos()

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.3, random_state=42)

# Escalamos los datos para que tengan media 0 y desviación estándar 1
escalador = StandardScaler()
X_entrenamiento = escalador.fit_transform(X_entrenamiento)  # Ajustamos y transformamos los datos de entrenamiento
X_prueba = escalador.transform(X_prueba)  # Transformamos los datos de prueba con el mismo escalador

# Lista de funciones de activación a probar
funciones = ['relu', 'sigmoid', 'tanh']  # Funciones de activación comunes en redes neuronales
precisiones = []  # Lista para almacenar las precisiones obtenidas

# Entrenamos y evaluamos el modelo para cada función de activación
for funcion in funciones:
    # Entrenamos el modelo y obtenemos la precisión
    precision, _ = construir_y_entrenar_modelo(funcion, X_entrenamiento, y_entrenamiento, X_prueba, y_prueba)
    precisiones.append(precision * 100)  # Convertimos la precisión a porcentaje y la almacenamos

# Graficamos los resultados
graficar_resultados(funciones, precisiones)

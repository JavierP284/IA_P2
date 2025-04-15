# Importamos las librerías necesarias
# - numpy: para operaciones matemáticas y manejo de matrices.
# - matplotlib.pyplot: para graficar imágenes y resultados.
# - tensorflow.keras: para construir y entrenar redes neuronales.
# - sklearn.metrics: para calcular métricas como la matriz de confusión y el reporte de clasificación.
# - seaborn: para graficar la matriz de confusión de manera más visual.
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns

# Función para cargar y preprocesar los datos
def cargar_datos():
    """
    Carga el conjunto de datos MNIST y realiza el preprocesamiento necesario:
    - Normaliza las imágenes dividiendo los valores de los píxeles entre 255.
    - Convierte las etiquetas a formato categórico (one-hot encoding).
    """
    (x_entrenamiento, y_entrenamiento), (x_prueba, y_prueba) = mnist.load_data()
    x_entrenamiento = x_entrenamiento / 255.0  # Normalización
    x_prueba = x_prueba / 255.0  # Normalización
    y_entrenamiento = to_categorical(y_entrenamiento, 10)  # One-hot encoding
    y_prueba = to_categorical(y_prueba, 10)  # One-hot encoding
    return (x_entrenamiento, y_entrenamiento), (x_prueba, y_prueba)

# Función para crear el modelo
def crear_modelo():
    """
    Crea un modelo de red neuronal utilizando Keras:
    - Una capa Flatten para convertir las imágenes 2D (28x28) en un vector 1D.
    - Una capa Dense con 128 neuronas y activación ReLU.
    - Una capa Dense con 10 neuronas (una por cada dígito) y activación softmax.
    - Compila el modelo con el optimizador Adam, la función de pérdida de entropía cruzada categórica,
      y la métrica de precisión.
    """
    modelo = Sequential([
        Flatten(input_shape=(28, 28)),  # Aplanar las imágenes 28x28 a un vector de 784 elementos
        Dense(128, activation='relu'),  # Capa oculta con 128 neuronas y activación ReLU
        Dense(10, activation='softmax')  # Capa de salida con 10 neuronas (una por cada clase)
    ])
    modelo.compile(optimizer='adam',  # Optimizador Adam
                   loss='categorical_crossentropy',  # Función de pérdida
                   metrics=['accuracy'])  # Métrica de evaluación
    return modelo

# Función para entrenar el modelo
def entrenar_modelo(modelo, x_entrenamiento, y_entrenamiento, epochs=5, batch_size=32):
    """
    Entrena el modelo con los datos de entrenamiento.
    - epochs: número de iteraciones completas sobre el conjunto de datos.
    - batch_size: número de muestras procesadas antes de actualizar los pesos.
    """
    modelo.fit(x_entrenamiento, y_entrenamiento, epochs=epochs, batch_size=batch_size)
    return modelo

# Función para evaluar el modelo
def evaluar_modelo(modelo, x_prueba, y_prueba):
    """
    Evalúa el modelo con los datos de prueba y muestra la precisión obtenida.
    """
    precision = modelo.evaluate(x_prueba, y_prueba, verbose=0)[1]  # Obtiene la precisión
    print(f'Precisión del modelo en datos de prueba: {precision * 100:.2f}%')

# Función para mostrar ejemplos de imágenes
def mostrar_ejemplos(x, y, cantidad=5):
    """
    Muestra ejemplos de imágenes del conjunto de datos junto con sus etiquetas.
    - cantidad: número de imágenes a mostrar.
    """
    plt.figure(figsize=(10, 2))
    for i in range(cantidad):
        plt.subplot(1, cantidad, i + 1)  # Crear subgráficos
        plt.imshow(x[i], cmap='gray')  # Mostrar la imagen en escala de grises
        plt.title(f'Etiqueta: {np.argmax(y[i])}')  # Mostrar la etiqueta
        plt.axis('off')  # Ocultar los ejes
    plt.show()

# Función para mostrar la matriz de confusión
def mostrar_matriz_confusion(modelo, x_prueba, y_prueba):
    """
    Calcula y muestra la matriz de confusión y el reporte de clasificación.
    - La matriz de confusión muestra cómo se distribuyen las predicciones del modelo.
    - El reporte de clasificación incluye métricas como precisión, recall y F1-score.
    """
    y_pred = np.argmax(modelo.predict(x_prueba), axis=1)  # Predicciones del modelo
    y_true = np.argmax(y_prueba, axis=1)  # Etiquetas reales
    matriz = confusion_matrix(y_true, y_pred)  # Calcular la matriz de confusión
    plt.figure(figsize=(10, 8))
    sns.heatmap(matriz, annot=True, fmt='d', cmap='Blues', xticklabels=range(10), yticklabels=range(10))
    plt.xlabel('Predicción')
    plt.ylabel('Etiqueta real')
    plt.title('Matriz de Confusión')
    plt.show()
    print(classification_report(y_true, y_pred))  # Mostrar el reporte de clasificación

# Función principal
def main():
    """
    Función principal que ejecuta el flujo completo del programa:
    1. Carga y preprocesa los datos.
    2. Muestra ejemplos de imágenes del conjunto de entrenamiento.
    3. Crea y entrena el modelo.
    4. Evalúa el modelo con los datos de prueba.
    5. Muestra la matriz de confusión.
    6. Realiza una predicción de ejemplo.
    """
    # Cargar y preprocesar los datos
    (x_entrenamiento, y_entrenamiento), (x_prueba, y_prueba) = cargar_datos()

    # Mostrar ejemplos de imágenes
    print("Ejemplos de imágenes del conjunto de entrenamiento:")
    mostrar_ejemplos(x_entrenamiento, y_entrenamiento)

    # Crear el modelo
    modelo = crear_modelo()

    # Entrenar el modelo
    modelo = entrenar_modelo(modelo, x_entrenamiento, y_entrenamiento)

    # Evaluar el modelo
    evaluar_modelo(modelo, x_prueba, y_prueba)

    # Mostrar la matriz de confusión
    mostrar_matriz_confusion(modelo, x_prueba, y_prueba)


    # Ejemplo de predicción
    indice = 25  # Índice de la imagen a predecir
    imagen = x_prueba[indice]
    plt.imshow(imagen, cmap='gray')
    plt.title("Imagen de prueba")
    plt.show()
    prediccion = modelo.predict(np.expand_dims(imagen, axis=0))  # Expandir dimensiones para predecir
    print("Predicción:", np.argmax(prediccion))  # Mostrar la predicción

# Ejecutar el programa si se ejecuta directamente
if __name__ == "__main__":
    main()

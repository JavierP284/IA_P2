# Importamos las librerías necesarias
import tensorflow as tf
from tensorflow.keras.datasets import mnist  # Dataset MNIST de dígitos escritos a mano
from tensorflow.keras.models import Sequential  # Modelo secuencial de Keras
from tensorflow.keras.layers import Dense, Flatten, Input  # Capas necesarias para la red
from tensorflow.keras.utils import to_categorical  # Para convertir etiquetas a formato one-hot
from tensorflow.keras.callbacks import EarlyStopping  # Callback para detener el entrenamiento temprano
import matplotlib.pyplot as plt  # Para graficar resultados
import numpy as np  # Para operaciones numéricas

# Función para preprocesar los datos
def preprocesar_datos():
    # Cargamos el dataset MNIST (imágenes de dígitos y sus etiquetas)
    (x_entrenamiento, y_entrenamiento), (x_prueba, y_prueba) = mnist.load_data()
    
    # Normalizamos los valores de las imágenes a un rango entre 0 y 1
    x_entrenamiento = x_entrenamiento / 255.0
    x_prueba = x_prueba / 255.0
    
    # Convertimos las etiquetas (números enteros) a codificación one-hot
    # Ejemplo: 3 -> [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    y_entrenamiento = to_categorical(y_entrenamiento)
    y_prueba = to_categorical(y_prueba)
    
    # Retornamos los datos preprocesados
    return (x_entrenamiento, y_entrenamiento), (x_prueba, y_prueba)

# Función para crear el modelo de red neuronal
def crear_modelo():
    # Creamos un modelo secuencial
    modelo = Sequential()
    
    # Agregamos una capa de entrada explícita con forma de las imágenes (28x28 píxeles)
    modelo.add(Input(shape=(28, 28)))
    
    # Aplanamos las imágenes 2D a un vector 1D para procesarlas en las capas densas
    modelo.add(Flatten())
    
    # Agregamos una capa densa (completamente conectada) con 128 neuronas y activación ReLU
    modelo.add(Dense(128, activation='relu'))
    
    # Agregamos otra capa densa con 64 neuronas y activación ReLU
    modelo.add(Dense(64, activation='relu'))
    
    # Agregamos la capa de salida con 10 neuronas (una por cada dígito) y activación softmax
    # Softmax convierte las salidas en probabilidades
    modelo.add(Dense(10, activation='softmax'))
    
    # Compilamos el modelo con el optimizador Adam, función de pérdida categórica y métrica de precisión
    modelo.compile(optimizer='adam',
                   loss='categorical_crossentropy',
                   metrics=['accuracy'])
    
    # Retornamos el modelo creado
    return modelo

# Función para graficar las métricas de entrenamiento
def graficar_historial(historial):
    plt.figure(figsize=(12, 5))  # Configuramos el tamaño de la figura
    
    # Gráfico de pérdida durante el entrenamiento y validación
    plt.subplot(1, 2, 1)  # Primera gráfica (1 fila, 2 columnas, posición 1)
    plt.plot(historial.history['loss'], label='Pérdida de entrenamiento')
    plt.plot(historial.history['val_loss'], label='Pérdida de validación')
    plt.title('Pérdida durante el entrenamiento')
    plt.xlabel('Épocas')
    plt.ylabel('Pérdida')
    plt.legend()
    
    # Gráfico de precisión durante el entrenamiento y validación
    plt.subplot(1, 2, 2)  # Segunda gráfica (1 fila, 2 columnas, posición 2)
    plt.plot(historial.history['accuracy'], label='Precisión de entrenamiento')
    plt.plot(historial.history['val_accuracy'], label='Precisión de validación')
    plt.title('Precisión durante el entrenamiento')
    plt.xlabel('Épocas')
    plt.ylabel('Precisión')
    plt.legend()
    
    # Mostramos las gráficas
    plt.show()

# Función principal
def main():
    # Preprocesamos los datos (normalización y codificación one-hot)
    (x_entrenamiento, y_entrenamiento), (x_prueba, y_prueba) = preprocesar_datos()
    
    # Creamos el modelo de red neuronal
    modelo = crear_modelo()
    
    # Definimos un callback para detener el entrenamiento si la pérdida de validación no mejora
    early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
    
    # Entrenamos el modelo con los datos de entrenamiento
    # Usamos un 10% de los datos para validación
    historial = modelo.fit(x_entrenamiento, y_entrenamiento, 
                            epochs=20,  # Número máximo de épocas
                            batch_size=32,  # Tamaño del lote
                            validation_split=0.1,  # Porcentaje de datos para validación
                            callbacks=[early_stopping])  # Callback para detener temprano
    
    # Evaluamos el modelo con los datos de prueba
    pérdida, precisión = modelo.evaluate(x_prueba, y_prueba)
    print(f'\nPrecisión en el conjunto de prueba: {precisión:.4f}')
    
    # Graficamos las métricas de entrenamiento y validación
    graficar_historial(historial)
    
    # Guardamos el modelo entrenado en un archivo
    modelo.save('modelo_mnist.h5')
    print("Modelo guardado como 'modelo_mnist.h5'")
    
    # Visualizamos algunas predicciones del modelo
    predicciones = modelo.predict(x_prueba[:5])  # Realizamos predicciones en las primeras 5 imágenes de prueba
    for i in range(5):
        plt.imshow(x_prueba[i], cmap='gray')  # Mostramos la imagen en escala de grises
        plt.title(f"Predicción: {np.argmax(predicciones[i])}")  # Mostramos la predicción del modelo
        plt.axis('off')  # Ocultamos los ejes
        plt.show()

# Ejecutamos el programa principal si este archivo es el principal
if __name__ == "__main__":
    main()

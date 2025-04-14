# Importamos las librerías necesarias
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Input
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
import numpy as np

# Función para preprocesar los datos
def preprocesar_datos():
    # Cargamos el dataset MNIST
    (x_entrenamiento, y_entrenamiento), (x_prueba, y_prueba) = mnist.load_data()
    
    # Normalizamos los datos
    x_entrenamiento = x_entrenamiento / 255.0
    x_prueba = x_prueba / 255.0
    
    # Convertimos las etiquetas a codificación one-hot
    y_entrenamiento = to_categorical(y_entrenamiento)
    y_prueba = to_categorical(y_prueba)
    
    return (x_entrenamiento, y_entrenamiento), (x_prueba, y_prueba)

# Función para crear el modelo
def crear_modelo():
    modelo = Sequential()
    modelo.add(Input(shape=(28, 28)))  # Capa de entrada explícita
    modelo.add(Flatten())
    modelo.add(Dense(128, activation='relu'))
    modelo.add(Dense(64, activation='relu'))
    modelo.add(Dense(10, activation='softmax'))
    modelo.compile(optimizer='adam',
                   loss='categorical_crossentropy',
                   metrics=['accuracy'])
    return modelo

# Función para graficar las métricas de entrenamiento
def graficar_historial(historial):
    plt.figure(figsize=(12, 5))
    
    # Gráfico de pérdida
    plt.subplot(1, 2, 1)
    plt.plot(historial.history['loss'], label='Pérdida de entrenamiento')
    plt.plot(historial.history['val_loss'], label='Pérdida de validación')
    plt.title('Pérdida durante el entrenamiento')
    plt.xlabel('Épocas')
    plt.ylabel('Pérdida')
    plt.legend()
    
    # Gráfico de precisión
    plt.subplot(1, 2, 2)
    plt.plot(historial.history['accuracy'], label='Precisión de entrenamiento')
    plt.plot(historial.history['val_accuracy'], label='Precisión de validación')
    plt.title('Precisión durante el entrenamiento')
    plt.xlabel('Épocas')
    plt.ylabel('Precisión')
    plt.legend()
    
    plt.show()

# Función principal
def main():
    # Preprocesamos los datos
    (x_entrenamiento, y_entrenamiento), (x_prueba, y_prueba) = preprocesar_datos()
    
    # Creamos el modelo
    modelo = crear_modelo()
    
    # Definimos un callback para detener el entrenamiento si no mejora
    early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
    
    # Entrenamos el modelo
    historial = modelo.fit(x_entrenamiento, y_entrenamiento, 
                            epochs=20, 
                            batch_size=32, 
                            validation_split=0.1, 
                            callbacks=[early_stopping])
    
    # Evaluamos el modelo
    pérdida, precisión = modelo.evaluate(x_prueba, y_prueba)
    print(f'\nPrecisión en el conjunto de prueba: {precisión:.4f}')
    
    # Graficamos las métricas
    graficar_historial(historial)
    
    # Guardamos el modelo
    modelo.save('modelo_mnist.h5')
    print("Modelo guardado como 'modelo_mnist.h5'")
    
    # Visualizamos algunas predicciones
    predicciones = modelo.predict(x_prueba[:5])
    for i in range(5):
        plt.imshow(x_prueba[i], cmap='gray')
        plt.title(f"Predicción: {np.argmax(predicciones[i])}")
        plt.axis('off')
        plt.show()

# Ejecutamos el programa principal
if __name__ == "__main__":
    main()

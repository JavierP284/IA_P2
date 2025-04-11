import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suprimir mensajes informativos de TensorFlow

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

# Datos de entrada (XOR)
# Matriz de entradas para la operación XOR
entradas = np.array([[0, 0],
                     [0, 1],
                     [1, 0],
                     [1, 1]])

# Salida esperada para la operación XOR
# Cada entrada tiene una salida correspondiente
salidas = np.array([[0],
                    [1],
                    [1],
                    [0]])

# Hiperparámetros
# Configuración de la red neuronal
neuronas_capa_oculta = 4  # Número de neuronas en la capa oculta
funcion_activacion_oculta = 'relu'  # Función de activación para la capa oculta
funcion_activacion_salida = 'sigmoid'  # Función de activación para la capa de salida
funcion_perdida = 'binary_crossentropy'  # Función de pérdida para problemas de clasificación binaria
optimizador = 'adam'  # Optimizador para ajustar los pesos
metricas = ['accuracy']  # Métrica para evaluar el modelo
epocas = 100  # Número de épocas para entrenar el modelo

# Función para construir el modelo
def construir_modelo():
    # Crear un modelo secuencial
    modelo = Sequential()
    # Capa de entrada con 2 neuronas (correspondientes a las 2 características de entrada)
    modelo.add(Input(shape=(2,)))  # Definir explícitamente la forma de entrada
    # Capa oculta con 4 neuronas y función de activación ReLU
    modelo.add(Dense(neuronas_capa_oculta, activation=funcion_activacion_oculta))
    # Capa de salida con 1 neurona y función de activación Sigmoid
    modelo.add(Dense(1, activation=funcion_activacion_salida))
    # Compilar el modelo con la función de pérdida, optimizador y métricas
    modelo.compile(loss=funcion_perdida, optimizer=optimizador, metrics=metricas)
    return modelo

# Crear el modelo llamando a la función
modelo = construir_modelo()

# Entrenar el modelo
# Se entrena el modelo con los datos de entrada y salida
# Se utiliza un 25% de los datos para validación
historial = modelo.fit(entradas, salidas, epochs=epocas, verbose=0, validation_split=0.25)

# Evaluar el modelo
# Se evalúa el modelo con los datos de entrada y salida
loss, accuracy = modelo.evaluate(entradas, salidas, verbose=0)
print(f"Precisión del modelo: {accuracy*100:.2f}%")  # Imprimir la precisión del modelo

# Hacer predicciones
# Se realizan predicciones con los datos de entrada
predicciones = modelo.predict(entradas)

# Mostrar resultados
# Se imprimen las entradas y las predicciones correspondientes
print("Resultados:")
for i in range(len(entradas)):
    print(f"Entrada: {entradas[i]} => Predicción: {predicciones[i][0]:.4f}")

# Visualizar el entrenamiento
# Graficar la pérdida de entrenamiento y validación a lo largo de las épocas
plt.plot(historial.history['loss'], label='Pérdida de entrenamiento')
plt.plot(historial.history['val_loss'], label='Pérdida de validación')
plt.title('Evolución de la pérdida durante el entrenamiento')
plt.xlabel('Épocas')
plt.ylabel('Pérdida')
plt.legend()
plt.show()

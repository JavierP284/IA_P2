# Importamos las librerías necesarias
import tensorflow as tf
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.utils import to_categorical
import matplotlib.pyplot as plt

# 1. Cargamos el conjunto de datos MNIST (imágenes de dígitos 0 al 9)
(x_entreno, y_entreno), (x_prueba, y_prueba) = mnist.load_data()

# 2. Normalizamos las imágenes dividiendo entre 255 para tener valores entre 0 y 1
x_entreno = x_entreno / 255.0
x_prueba = x_prueba / 255.0

# 3. Convertimos las etiquetas en formato categórico (one-hot encoding)
y_entreno_cat = to_categorical(y_entreno, 10)
y_prueba_cat = to_categorical(y_prueba, 10)

# 4. Creamos el modelo de red neuronal (red multicapa - MLP)
modelo = Sequential([
    Flatten(input_shape=(28, 28)),  # Aplanamos la imagen de 28x28 a 784
    Dense(128, activation='relu'),  # Capa oculta con 128 neuronas y activación ReLU
    Dense(64, activation='relu'),   # Otra capa oculta
    Dense(10, activation='softmax') # Capa de salida con 10 clases (0 al 9)
])

# 5. Compilamos el modelo (definimos optimizador, función de pérdida y métrica)
modelo.compile(optimizer='adam',
               loss='categorical_crossentropy',
               metrics=['accuracy'])

# 6. Entrenamos el modelo con los datos de entrenamiento
historial = modelo.fit(x_entreno, y_entreno_cat, epochs=5, batch_size=32, validation_split=0.2)

# 7. Evaluamos el modelo con los datos de prueba
pérdida, precisión = modelo.evaluate(x_prueba, y_prueba_cat)
print(f"\nPrecisión del modelo en prueba: {precisión:.4f}")

# 8. Graficamos la evolución del entrenamiento
plt.plot(historial.history['accuracy'], label='Precisión en entrenamiento')
plt.plot(historial.history['val_accuracy'], label='Precisión en validación')
plt.xlabel('Épocas')
plt.ylabel('Precisión')
plt.title('Precisión durante el entrenamiento')
plt.legend()
plt.grid(True)
plt.show()

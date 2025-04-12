import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Perceptron
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. Generamos datos linealmente separables
# Parámetros ajustables para experimentar
n_samples = 100  # Número de muestras totales (puntos de datos)
class_sep = 2.0  # Separación entre las clases (mayor valor = más separables)
random_state = 1  # Semilla para reproducibilidad

# Generamos un conjunto de datos sintéticos con dos características (2D)
X, y = make_classification(n_samples=n_samples, n_features=2, n_redundant=0,
                           n_informative=2, n_clusters_per_class=1,
                           class_sep=class_sep, random_state=random_state)

# Visualizamos los datos generados
# Los puntos de la clase 0 se dibujan en rojo y los de la clase 1 en azul
plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='red', label='Clase 0')
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='blue', label='Clase 1')
plt.title("Datos Generados (Linealmente Separables)")  # Título del gráfico
plt.xlabel("Característica 1")  # Etiqueta del eje X
plt.ylabel("Característica 2")  # Etiqueta del eje Y
plt.legend()  # Muestra la leyenda
plt.grid(True)  # Activa la cuadrícula
plt.show()  # Muestra el gráfico

# 2. Creamos el modelo Perceptrón
# Parámetros ajustables
max_iter = 1000  # Número máximo de iteraciones para el entrenamiento
tol = 1e-3  # Tolerancia para la convergencia (criterio de parada)

# Inicializamos el modelo Perceptrón
modelo = Perceptron(max_iter=max_iter, tol=tol, random_state=random_state)

# 3. Entrenamos el modelo
# Ajustamos el modelo a los datos generados
modelo.fit(X, y)

# 4. Hacemos predicciones
# Usamos el modelo entrenado para predecir las etiquetas de los datos
y_pred = modelo.predict(X)

# 5. Evaluamos el modelo
# Calculamos la precisión del modelo (proporción de predicciones correctas)
accuracy = accuracy_score(y, y_pred)

# Calculamos la matriz de confusión (muestra los aciertos y errores por clase)
conf_matrix = confusion_matrix(y, y_pred)

# Mostramos los resultados de la evaluación
print(f"Precisión del modelo: {accuracy:.2f}")  # Precisión con dos decimales
print("Matriz de confusión:")
print(conf_matrix)

# Verificamos si los datos son separables
# Si la precisión es 1.0, significa que el modelo clasificó todos los puntos correctamente
if accuracy == 1.0:
    print("Los datos SON linealmente separables.")
else:
    print("Los datos NO son linealmente separables.")

# 6. Mostramos la frontera de decisión
# Calculamos los valores de la frontera de decisión
# La ecuación de la frontera es: w1*x1 + w2*x2 + b = 0
x_vals = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)  # Valores del eje X
y_vals = -(modelo.coef_[0][0] * x_vals + modelo.intercept_[0]) / modelo.coef_[0][1]  # Ecuación de la recta

# Dibujamos los puntos de las clases y la frontera de decisión
plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='red', label='Clase 0')
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='blue', label='Clase 1')
plt.plot(x_vals, y_vals, color='green', linestyle='--', label='Frontera de decisión')  # Línea de decisión
plt.title("Separación lineal con Perceptrón")  # Título del gráfico
plt.xlabel("Característica 1")  # Etiqueta del eje X
plt.ylabel("Característica 2")  # Etiqueta del eje Y
plt.legend()  # Muestra la leyenda
plt.grid(True)  # Activa la cuadrícula
plt.show()  # Muestra el gráfico

# 7. Explicación adicional
# Nota para el usuario sobre cómo ajustar los parámetros en caso de problemas
print("\nNota: Si los datos no son separables, intente ajustar el parámetro 'class_sep' o aumente 'max_iter'.")

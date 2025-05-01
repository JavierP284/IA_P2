# ------------------------------------------------------------------
# Simulación de Árbol de Regresión (usando sklearn)
# ------------------------------------------------------------------

# Importar las librerías necesarias
import numpy as np
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# ----------------------------
# Datos de entrada: características de las casas
# Cada fila representa una casa con las siguientes características:
# [tamaño_m2, habitaciones]
X = np.array([
    [50, 1],   # Casa de 50 m² con 1 habitación
    [60, 2],   # Casa de 60 m² con 2 habitaciones
    [80, 2],   # Casa de 80 m² con 2 habitaciones
    [100, 3],  # Casa de 100 m² con 3 habitaciones
    [120, 4],  # Casa de 120 m² con 4 habitaciones
    [150, 4],  # Casa de 150 m² con 4 habitaciones
    [170, 5],  # Casa de 170 m² con 5 habitaciones
    [200, 6]   # Casa de 200 m² con 6 habitaciones
])

# Etiquetas (precios de las casas en miles de dólares)
# Cada valor corresponde al precio de la casa en la misma posición de X
y = np.array([100, 120, 150, 200, 250, 300, 340, 400])

# ----------------------------
# Dividir los datos en conjuntos de entrenamiento y prueba
# El conjunto de entrenamiento se usa para ajustar el modelo
# El conjunto de prueba se usa para evaluar el rendimiento del modelo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ----------------------------
# Crear el modelo de Árbol de Regresión
# max_depth=3 limita la profundidad del árbol para evitar sobreajuste
modelo = DecisionTreeRegressor(max_depth=3, random_state=42)
modelo.fit(X_train, y_train)  # Entrenar el modelo con los datos de entrenamiento

# ----------------------------
# Evaluar el modelo con los datos de prueba
# Realizar predicciones sobre el conjunto de prueba
y_pred = modelo.predict(X_test)

# Calcular métricas de evaluación:
# - Error cuadrático medio (MSE): mide el error promedio al cuadrado
# - Coeficiente de determinación (R²): mide qué tan bien el modelo explica los datos
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Mostrar las métricas de evaluación
print(f"Error cuadrático medio (MSE): {mse:.2f}")
print(f"Coeficiente de determinación (R²): {r2:.2f}")

# ----------------------------
# Probar el modelo con nuevos datos
# Predicción para una casa de 110 m² con 3 habitaciones
nueva_casa = np.array([[110, 3]])
prediccion = modelo.predict(nueva_casa)

# Mostrar la predicción
print(f"\nPredicción para casa de 110 m² y 3 habitaciones: ${round(prediccion[0], 2)} mil")

# ----------------------------
# Visualización del árbol de decisión
# Mostrar el árbol de regresión entrenado
plt.figure(figsize=(12, 6))  # Tamaño de la figura
plot_tree(modelo, feature_names=["tamaño_m2", "habitaciones"], filled=True, rounded=True)
plt.title("Árbol de Regresión")  # Título del gráfico
plt.show()

# ----------------------------
# Visualización de resultados
# Comparar los valores reales con las predicciones
plt.figure(figsize=(8, 6))  # Tamaño de la figura
plt.scatter(range(len(y_test)), y_test, color="blue", label="Valores reales")  # Valores reales
plt.scatter(range(len(y_pred)), y_pred, color="red", label="Predicciones")  # Predicciones del modelo
plt.xlabel("Índice de muestra")  # Etiqueta del eje X
plt.ylabel("Precio (miles de dólares)")  # Etiqueta del eje Y
plt.title("Comparación de valores reales y predicciones")  # Título del gráfico
plt.legend()  # Mostrar la leyenda
plt.show()

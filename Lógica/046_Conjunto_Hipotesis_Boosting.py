# ----------------------------------------------------------------------
# Ejemplo de Boosting con AdaBoostClassifier (usando sklearn)
# ----------------------------------------------------------------------

# Importar las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns

# ----------------------------
# Datos de entrenamiento
# Cada fila representa un individuo con dos características: [edad, ingreso]
X = [
    [25, 2000],  # Edad: 25 años, Ingreso: 2000
    [30, 2500],  # Edad: 30 años, Ingreso: 2500
    [35, 3000],  # Edad: 35 años, Ingreso: 3000
    [40, 4000],  # Edad: 40 años, Ingreso: 4000
    [45, 5000],  # Edad: 45 años, Ingreso: 5000
    [50, 5500],  # Edad: 50 años, Ingreso: 5500
    [55, 6000],  # Edad: 55 años, Ingreso: 6000
    [60, 7000]   # Edad: 60 años, Ingreso: 7000
]

# Etiquetas asociadas a los datos: 0 = no compra, 1 = compra
# Estas etiquetas indican si una persona realiza una compra (1) o no (0)
y = [0, 0, 0, 1, 1, 1, 1, 1]

# ----------------------------
# Visualizar los datos
# Crear un gráfico de dispersión para observar la distribución de los datos
plt.scatter(
    [x[0] for x in X],  # Extraer la edad (primer elemento de cada fila)
    [x[1] for x in X],  # Extraer el ingreso (segundo elemento de cada fila)
    c=y,                # Colorear los puntos según la etiqueta (0 o 1)
    cmap='coolwarm',    # Usar un mapa de colores para diferenciar las etiquetas
    s=100               # Tamaño de los puntos
)
plt.title("Distribución de los datos")  # Título del gráfico
plt.xlabel("Edad")                      # Etiqueta del eje X
plt.ylabel("Ingreso")                   # Etiqueta del eje Y
plt.colorbar(label="Etiqueta (0 = No compra, 1 = Compra)")  # Leyenda del color
plt.show()

# ----------------------------
# Dividir los datos en conjuntos de entrenamiento y prueba
# El conjunto de entrenamiento se usa para entrenar el modelo
# El conjunto de prueba se usa para evaluar el modelo
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42  # 25% de los datos se reservan para prueba
)

# ----------------------------
# Crear el modelo de Boosting
# AdaBoostClassifier combina varios clasificadores débiles (árboles de decisión simples)
modelo = AdaBoostClassifier(
    base_estimator=DecisionTreeClassifier(max_depth=1),  # Clasificadores débiles (árboles con profundidad 1)
    n_estimators=10,     # Número de clasificadores débiles a combinar
    learning_rate=1.0,   # Peso de cada clasificador en el modelo final
    algorithm='SAMME.R', # Algoritmo de boosting (SAMME.R es más eficiente)
    random_state=42      # Semilla para reproducibilidad
)

# Entrenar el modelo con los datos de entrenamiento
modelo.fit(X_train, y_train)

# ----------------------------
# Hacer predicciones con el modelo entrenado
y_pred = modelo.predict(X_test)

# Mostrar los resultados de las predicciones
print("\nResultados del modelo Boosting:")
for entrada, pred, real in zip(X_test, y_pred, y_test):
    print(f"Entrada: {entrada}, Predicción: {pred}, Real: {real}")

# ----------------------------
# Evaluar el modelo
# Calcular la precisión del modelo (porcentaje de predicciones correctas)
exactitud = accuracy_score(y_test, y_pred)
print(f"\nPrecisión del modelo: {round(exactitud * 100, 2)}%")

# Crear una matriz de confusión para analizar los errores del modelo
matriz_confusion = confusion_matrix(y_test, y_pred)
sns.heatmap(
    matriz_confusion, 
    annot=True,         # Mostrar los valores en las celdas
    fmt="d",            # Formato de los valores (números enteros)
    cmap="Blues",       # Colores del mapa
    xticklabels=["No compra", "Compra"],  # Etiquetas de las columnas
    yticklabels=["No compra", "Compra"]   # Etiquetas de las filas
)
plt.title("Matriz de Confusión")  # Título del gráfico
plt.xlabel("Predicción")          # Etiqueta del eje X
plt.ylabel("Real")                # Etiqueta del eje Y
plt.show()

# Generar un reporte de clasificación con métricas detalladas
print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred, target_names=["No compra", "Compra"]))

# ----------------------------
# Visualizar la importancia de los clasificadores débiles
# Cada clasificador débil tiene un peso que indica su contribución al modelo final
importancias = modelo.estimator_weights_
plt.bar(range(len(importancias)), importancias)  # Crear un gráfico de barras
plt.title("Importancia de los clasificadores débiles")  # Título del gráfico
plt.xlabel("Clasificador débil")                      # Etiqueta del eje X
plt.ylabel("Peso")                                    # Etiqueta del eje Y
plt.show()

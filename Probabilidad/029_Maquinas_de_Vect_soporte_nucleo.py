from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 1. Generar datos con forma de círculos (no linealmente separables)
# `make_circles` genera un conjunto de datos en forma de círculos concéntricos.
X, y = make_circles(n_samples=300, factor=0.5, noise=0.05, random_state=42)

# Visualizar los datos iniciales
# Se grafican los puntos generados para observar su distribución.
plt.figure(figsize=(6, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolors='k')
plt.title("Datos iniciales (círculos)")
plt.xlabel("X1")
plt.ylabel("X2")
plt.grid(True)
plt.show()

# 2. Dividir en datos de entrenamiento y prueba
# Se dividen los datos en un 70% para entrenamiento y un 30% para prueba.
X_entreno, X_prueba, y_entreno, y_prueba = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Crear un modelo SVM con un kernel RBF
# Se define un modelo SVM con un núcleo RBF (Radial Basis Function).
# El parámetro `C` controla la regularización y `gamma` define la influencia de un solo punto de entrenamiento.
modelo_svm = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)

# 4. Entrenar el modelo
# Se entrena el modelo SVM con los datos de entrenamiento.
modelo_svm.fit(X_entreno, y_entreno)

# 5. Predecir las etiquetas de prueba
# Se realizan predicciones sobre los datos de prueba.
y_pred = modelo_svm.predict(X_prueba)

# 6. Visualizar la frontera de decisión
# Esta función grafica la frontera de decisión del modelo en el espacio de características.
def graficar_frontera(modelo, X, y, titulo="Frontera de decisión"):
    # Definir los límites del gráfico
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    
    # Crear una malla de puntos para evaluar el modelo
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 500),
                         np.linspace(y_min, y_max, 500))
    
    # Predecir las etiquetas para cada punto de la malla
    Z = modelo.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    # Graficar la frontera de decisión y los puntos de datos
    plt.contourf(xx, yy, Z, cmap='coolwarm', alpha=0.3)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolors='k')
    plt.title(titulo)
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.grid(True)
    plt.show()

# Graficar la frontera de decisión del modelo inicial
graficar_frontera(modelo_svm, X, y, "Clasificación con SVM (núcleo RBF)")

# 7. Evaluar el modelo
# Calcular la precisión del modelo en los datos de prueba.
print("Precisión del modelo SVM:", accuracy_score(y_prueba, y_pred))

# Generar un reporte de clasificación con métricas como precisión, recall y F1-score.
print("\nReporte de clasificación:\n", classification_report(y_prueba, y_pred))

# Matriz de confusión
# Calcular y graficar la matriz de confusión para analizar los errores de clasificación.
conf_matrix = confusion_matrix(y_prueba, y_pred)
plt.figure(figsize=(6, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=["Clase 0", "Clase 1"], yticklabels=["Clase 0", "Clase 1"])
plt.title("Matriz de Confusión")
plt.xlabel("Predicción")
plt.ylabel("Real")
plt.show()

# 8. Ajuste de hiperparámetros con GridSearchCV
# Definir una cuadrícula de valores para los hiperparámetros `C` y `gamma`.
param_grid = {'C': [0.1, 1, 10], 'gamma': ['scale', 0.1, 1, 10]}

# Usar GridSearchCV para encontrar la mejor combinación de hiperparámetros.
# Se utiliza validación cruzada con 5 particiones (`cv=5`) y la métrica de precisión (`scoring='accuracy'`).
grid_search = GridSearchCV(SVC(kernel='rbf'), param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_entreno, y_entreno)

# Mostrar los mejores hiperparámetros encontrados y la mejor precisión obtenida durante la validación cruzada.
print("Mejores hiperparámetros:", grid_search.best_params_)
print("Mejor precisión en validación cruzada:", grid_search.best_score_)

# Entrenar y evaluar el mejor modelo
# Usar el mejor modelo encontrado por GridSearchCV para realizar predicciones.
mejor_modelo = grid_search.best_estimator_
y_pred_mejor = mejor_modelo.predict(X_prueba)

# Mostrar la precisión del mejor modelo en los datos de prueba.
print("Precisión del mejor modelo SVM:", accuracy_score(y_prueba, y_pred_mejor))

# Graficar la frontera de decisión del mejor modelo.
graficar_frontera(mejor_modelo, X, y, "Frontera de decisión (Mejor modelo)")

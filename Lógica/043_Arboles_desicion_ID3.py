# -------------------------------------------------------------
# Árbol de Decisión con ID3 (usando scikit-learn)
# -------------------------------------------------------------

# Importamos las librerías necesarias
from sklearn.tree import DecisionTreeClassifier  # Para crear el modelo de árbol de decisión
from sklearn import tree  # Para exportar y visualizar el árbol
from sklearn.model_selection import train_test_split  # Para dividir los datos en entrenamiento y prueba
import matplotlib.pyplot as plt  # Para graficar el árbol de decisión

# ----------------------------
# Datos de entrenamiento
# Cada fila representa una instancia con atributos codificados manualmente.
# Convertimos categorías a números para simplificar el procesamiento.

# Atributos (codificados manualmente):
# clima:    soleado=0, nublado=1, lluvioso=2
# temp:     alta=0, media=1, baja=2
# humedad:  alta=0, normal=1
# viento:   no=0, sí=1

# Matriz de características (X): cada fila es una instancia con sus atributos
X = [
    [0, 0, 0, 0],  # soleado, alta, alta, no
    [0, 0, 0, 1],  # soleado, alta, alta, sí
    [1, 0, 0, 0],  # nublado, alta, alta, no
    [2, 2, 1, 0],  # lluvioso, baja, normal, no
    [2, 1, 1, 1],  # lluvioso, media, normal, sí
    [2, 1, 1, 0],  # lluvioso, media, normal, no
    [1, 1, 1, 1],  # nublado, media, normal, sí
    [0, 2, 0, 0],  # soleado, baja, alta, no
    [0, 1, 1, 0],  # soleado, media, normal, no
    [1, 2, 1, 1],  # nublado, baja, normal, sí
]

# Etiquetas (objetivo) (y): indica si se debe jugar (1) o no jugar (0)
y = [0, 0, 1, 1, 1, 1, 1, 0, 0, 1]

# ----------------------------
# Dividir datos en entrenamiento y prueba
# Usamos train_test_split para dividir los datos en dos conjuntos:
# - 70% para entrenamiento
# - 30% para prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ----------------------------
# Crear el modelo de árbol de decisión
# Usamos el criterio 'entropy' para aplicar el algoritmo ID3
modelo = DecisionTreeClassifier(criterion="entropy", random_state=42)

# Entrenamos el modelo con los datos de entrenamiento
modelo.fit(X_train, y_train)

# ----------------------------
# Probar una predicción
# Creamos una nueva instancia para predecir si se debe jugar o no
# Ejemplo: soleado (0), media (1), alta (0), no (0)
nueva_instancia = [[0, 1, 0, 0]]

# Realizamos la predicción con el modelo entrenado
prediccion = modelo.predict(nueva_instancia)

# Mostramos el resultado de la predicción
print("\n¿Debería jugar hoy?")
print("Resultado:", "Sí" if prediccion[0] == 1 else "No")

# ----------------------------
# Evaluar el modelo
# Calculamos la precisión del modelo en los datos de prueba
accuracy = modelo.score(X_test, y_test)

# Mostramos la precisión del modelo
print("\nPrecisión del modelo en datos de prueba:", accuracy)

# ----------------------------
# Visualización del árbol
# Exportamos el árbol en formato de texto para entender su estructura
print("\nÁrbol de Decisión ID3:")
tree_texto = tree.export_text(modelo, feature_names=["clima", "temperatura", "humedad", "viento"])
print(tree_texto)

# Visualización gráfica del árbol
# Creamos una figura para graficar el árbol de decisión
plt.figure(figsize=(12, 8))

# Graficamos el árbol con nombres de características y clases
tree.plot_tree(
    modelo,
    feature_names=["clima", "temperatura", "humedad", "viento"],  # Nombres de los atributos
    class_names=["No Jugar", "Jugar"],  # Nombres de las clases
    filled=True  # Colorear los nodos según la clase
)

# Añadimos un título al gráfico
plt.title("Árbol de Decisión (ID3)")

# Mostramos el gráfico
plt.show()

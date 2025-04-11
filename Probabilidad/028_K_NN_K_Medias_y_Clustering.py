import numpy as np
from sklearn.datasets import make_classification, make_blobs
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.cluster import KMeans, AgglomerativeClustering
import matplotlib.pyplot as plt

# Función para ejemplo de k-NN
def ejemplo_knn():
    """
    Ejemplo de clasificación con k-NN.
    """
    # Generamos datos de clasificación con 2 características y 2 clases
    X, y = make_classification(n_samples=100, n_features=2, n_classes=2, n_redundant=0, random_state=42)
    
    # Dividimos los datos en conjuntos de entrenamiento (70%) y prueba (30%)
    X_entreno, X_prueba, y_entreno, y_prueba = train_test_split(X, y, test_size=0.3, random_state=42)

    # Creamos un modelo k-NN con k=3 (3 vecinos más cercanos)
    modelo_knn = KNeighborsClassifier(n_neighbors=3)
    
    # Entrenamos el modelo con los datos de entrenamiento
    modelo_knn.fit(X_entreno, y_entreno)

    # Realizamos predicciones sobre los datos de prueba
    y_pred = modelo_knn.predict(X_prueba)
    
    # Mostramos un reporte de clasificación con métricas como precisión, recall y F1-score
    print("Reporte de clasificación para k-NN:")
    print(classification_report(y_prueba, y_pred))
    
    # Mostramos la matriz de confusión para evaluar el rendimiento del modelo
    print("Matriz de confusión:\n", confusion_matrix(y_prueba, y_pred))

    # Visualizamos los datos de prueba y las predicciones
    plt.scatter(X_prueba[:, 0], X_prueba[:, 1], c=y_pred, cmap='coolwarm', label='Predicción')
    plt.title("Clasificación k-NN (k=3)")
    plt.xlabel("Característica 1")
    plt.ylabel("Característica 2")
    plt.legend()
    plt.grid(True)
    plt.show()

# Función para ejemplo de k-Medias
def ejemplo_kmeans():
    """
    Ejemplo de agrupamiento con k-Medias.
    """
    # Generamos datos para clustering con 3 centros (clústeres)
    X, _ = make_blobs(n_samples=150, centers=3, cluster_std=1.0, random_state=42)

    # Creamos un modelo k-Medias con 3 clústeres
    modelo_kmeans = KMeans(n_clusters=3, random_state=42)
    
    # Ajustamos el modelo a los datos
    modelo_kmeans.fit(X)
    
    # Obtenemos las etiquetas de los clústeres asignadas a cada punto
    etiquetas = modelo_kmeans.labels_

    # Mostramos las coordenadas de los centros de los clústeres
    print("Centros de clúster:", modelo_kmeans.cluster_centers_)

    # Visualizamos los puntos agrupados y los centros de los clústeres
    plt.scatter(X[:, 0], X[:, 1], c=etiquetas, cmap='viridis', marker='o')
    plt.scatter(modelo_kmeans.cluster_centers_[:, 0], modelo_kmeans.cluster_centers_[:, 1], s=200, c='red', marker='X', label='Centros')
    plt.title("Agrupamiento k-Medias")
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.legend()
    plt.grid(True)
    plt.show()

# Función para ejemplo de Clustering Jerárquico
def ejemplo_clustering_jerarquico():
    """
    Ejemplo de agrupamiento con Clustering Jerárquico Aglomerativo.
    """
    # Generamos datos para clustering con 3 centros
    X, _ = make_blobs(n_samples=100, centers=3, cluster_std=0.8, random_state=42)

    # Creamos un modelo de clustering jerárquico con 3 clústeres
    modelo_aglomerativo = AgglomerativeClustering(n_clusters=3)
    
    # Ajustamos el modelo y obtenemos las etiquetas de los clústeres
    etiquetas = modelo_aglomerativo.fit_predict(X)

    # Visualizamos los puntos agrupados
    plt.scatter(X[:, 0], X[:, 1], c=etiquetas, cmap='rainbow', marker='o')
    plt.title("Clustering Jerárquico Aglomerativo")
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.grid(True)
    plt.show()

# Llamamos a las funciones principales
if __name__ == "__main__":
    print("Ejemplo de k-NN:")
    ejemplo_knn()  # Ejecuta el ejemplo de k-NN
    print("\nEjemplo de k-Medias:")
    ejemplo_kmeans()  # Ejecuta el ejemplo de k-Medias
    print("\nEjemplo de Clustering Jerárquico:")
    ejemplo_clustering_jerarquico()  # Ejecuta el ejemplo de Clustering Jerárquico

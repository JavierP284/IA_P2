from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def cargar_datos():
    """
    Carga los datos de entrenamiento y sus etiquetas.
    """
    correos = [
        "gana dinero ahora",         # spam
        "oferta limitada gratis",    # spam
        "dinero urgente gana",       # spam
        "reunión con el equipo",     # no spam
        "programa el informe",       # no spam
        "revisión del proyecto"      # no spam
    ]
    etiquetas = ["spam", "spam", "spam", "no spam", "no spam", "no spam"]
    return correos, etiquetas

def entrenar_modelo(correos, etiquetas):
    """
    Entrena un modelo Naive Bayes con los datos proporcionados.
    """
    vectorizador = CountVectorizer()
    X = vectorizador.fit_transform(correos)
    modelo = MultinomialNB()
    modelo.fit(X, etiquetas)
    return modelo, vectorizador

def evaluar_modelo(modelo, vectorizador, correos_prueba, etiquetas_reales):
    """
    Evalúa el modelo con datos de prueba y muestra métricas.
    """
    X_prueba = vectorizador.transform(correos_prueba)
    predicciones = modelo.predict(X_prueba)
    
    print("\nReporte de clasificación:\n", classification_report(etiquetas_reales, predicciones))
    print("Precisión del modelo:", accuracy_score(etiquetas_reales, predicciones))
    
    # Matriz de confusión
    matriz_confusion = confusion_matrix(etiquetas_reales, predicciones, labels=modelo.classes_)
    sns.heatmap(matriz_confusion, annot=True, fmt='d', cmap='Blues', xticklabels=modelo.classes_, yticklabels=modelo.classes_)
    plt.title("Matriz de Confusión")
    plt.xlabel("Predicción")
    plt.ylabel("Etiqueta Real")
    plt.show()

def predecir_nuevo_correo(modelo, vectorizador, nuevo_correo):
    """
    Predice la clasificación de un nuevo correo.
    """
    X_nuevo = vectorizador.transform(nuevo_correo)
    prediccion = modelo.predict(X_nuevo)
    probs = modelo.predict_proba(X_nuevo)
    
    print("\nNuevo correo:", nuevo_correo[0])
    print("Clasificación:", prediccion[0])
    print("Probabilidades:", dict(zip(modelo.classes_, probs[0])))

# -------------------------------
# Ejecución principal
# -------------------------------
if __name__ == "__main__":
    # 1. Cargar datos
    correos, etiquetas = cargar_datos()
    
    # 2. Entrenar modelo
    modelo, vectorizador = entrenar_modelo(correos, etiquetas)
    
    # 3. Evaluar modelo
    correos_prueba = [
        "dinero urgente gratis",  # spam
        "reunión del equipo",     # no spam
        "gana una oferta limitada ahora",  # spam
        "programa la revisión"    # no spam
    ]
    etiquetas_reales = ["spam", "no spam", "spam", "no spam"]
    evaluar_modelo(modelo, vectorizador, correos_prueba, etiquetas_reales)
    
    # 4. Probar con un nuevo correo
    nuevo_correo = ["gana dinero gratis ahora"]
    predecir_nuevo_correo(modelo, vectorizador, nuevo_correo)

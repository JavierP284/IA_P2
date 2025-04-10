from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

# -------------------------------
# 1. Datos de entrenamiento (muy simples)
# -------------------------------
correos = [
    "gana dinero ahora",         # spam
    "oferta limitada gratis",    # spam
    "dinero urgente gana",       # spam
    "reunión con el equipo",     # no spam
    "programa el informe",       # no spam
    "revisión del proyecto"      # no spam
]

etiquetas = ["spam", "spam", "spam", "no spam", "no spam", "no spam"]

# -------------------------------
# 2. Convertimos texto a características (bag of words)
# -------------------------------
vectorizador = CountVectorizer()
X = vectorizador.fit_transform(correos)  # Matriz de ocurrencias

# Visualizamos las características generadas
print("Palabras clave:", vectorizador.get_feature_names_out())
print("Matriz de ocurrencias:\n", X.toarray())

# -------------------------------
# 3. Entrenamos el modelo Naive Bayes
# -------------------------------
modelo = MultinomialNB()
modelo.fit(X, etiquetas)

# -------------------------------
# 4. Validamos el modelo con datos de prueba
# -------------------------------
correos_prueba = [
    "dinero urgente gratis",  # spam
    "reunión del equipo",     # no spam
    "gana una oferta limitada ahora",  # spam
    "programa la revisión"    # no spam
]
etiquetas_reales = ["spam", "no spam", "spam", "no spam"]

X_prueba = vectorizador.transform(correos_prueba)
predicciones = modelo.predict(X_prueba)

# Métricas de evaluación
print("\nReporte de clasificación:\n", classification_report(etiquetas_reales, predicciones))
print("Precisión del modelo:", accuracy_score(etiquetas_reales, predicciones))

# -------------------------------
# 5. Probamos con un nuevo correo
# -------------------------------
nuevo_correo = ["gana dinero gratis ahora"]
X_nuevo = vectorizador.transform(nuevo_correo)

# Predicción y probabilidades
prediccion = modelo.predict(X_nuevo)
probs = modelo.predict_proba(X_nuevo)

print("\nNuevo correo:", nuevo_correo[0])
print("Clasificación:", prediccion[0])
print("Probabilidades:", dict(zip(modelo.classes_, probs[0])))

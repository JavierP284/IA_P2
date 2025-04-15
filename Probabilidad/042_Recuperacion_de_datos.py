from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ----- Paso 1: Base de datos de documentos (simulación) -----
# Lista de documentos que simulan una base de datos de texto.
# Cada elemento de la lista representa un documento.
documentos = [
    "El gato duerme en el sofá",
    "El perro ladra fuerte",
    "El gato y el perro juegan juntos",
    "Me gusta programar en Python",
    "Los animales son divertidos"
]

# ----- Paso 2: Consulta del usuario -----
# Consulta que el usuario realiza para buscar documentos relevantes.
consulta = "Python y perro"

# ----- Paso 3: Convertir los textos a vectores TF-IDF -----
# Creamos un vectorizador TF-IDF que convierte texto en vectores numéricos.
# TF-IDF (Term Frequency - Inverse Document Frequency) mide la importancia
# de las palabras en un documento en relación con el corpus completo.
vectorizador = TfidfVectorizer()

# Unimos los documentos y la consulta en un solo corpus para procesarlos juntos.
corpus_completo = documentos + [consulta]

# Generamos la matriz TF-IDF a partir del corpus completo.
# Cada fila de la matriz representa un documento o la consulta en forma de vector.
tfidf_matriz = vectorizador.fit_transform(corpus_completo)

# ----- Paso 4: Calculamos la similitud entre la consulta y cada documento -----
# Usamos la similitud coseno para medir qué tan similares son los vectores.
# La última fila de la matriz TF-IDF corresponde a la consulta,
# mientras que las filas anteriores corresponden a los documentos.
similitudes = cosine_similarity(tfidf_matriz[-1], tfidf_matriz[:-1])

# ----- Paso 5: Mostramos los resultados ordenados por relevancia -----
# Imprimimos un encabezado para los resultados.
print("Resultados ordenados por similitud con la consulta:\n")

# Enumeramos las similitudes para asociarlas con los índices de los documentos.
# Cada elemento de 'resultados' es una tupla (índice, similitud).
resultados = list(enumerate(similitudes[0]))

# Ordenamos los resultados en orden descendente según la similitud.
resultados.sort(key=lambda x: x[1], reverse=True)

# Iteramos sobre los resultados ordenados para mostrar la información.
for idx, score in resultados:
    # Mostramos el índice del documento (ajustado a base 1) y su similitud.
    print(f"Documento #{idx + 1} - Similitud: {score:.2f}")
    # Mostramos el contenido del documento correspondiente.
    print(f"Contenido: {documentos[idx]}\n")

import random
from collections import defaultdict

# -------- Función: Preprocesar el corpus --------
def preprocesar_corpus(corpus):
    """
    Convierte el texto en minúsculas y lo separa en palabras.
    """
    return corpus.lower().split()

# -------- Función: Crear modelo de bigramas --------
def crear_modelo_bigramas(palabras):
    """
    Crea un modelo de bigramas basado en conteos y lo convierte a probabilidades.
    """
    bigramas = defaultdict(lambda: defaultdict(int))
    for i in range(len(palabras) - 1):
        anterior = palabras[i]
        siguiente = palabras[i + 1]
        bigramas[anterior][siguiente] += 1

    modelo_prob = {}
    for palabra in bigramas:
        total = float(sum(bigramas[palabra].values()))
        modelo_prob[palabra] = {
            siguiente: conteo / total
            for siguiente, conteo in bigramas[palabra].items()
        }
    return modelo_prob

# -------- Función: Generar frase --------
def generar_frase(modelo, palabra_inicial, longitud=5):
    """
    Genera una frase basada en el modelo de bigramas.
    """
    if palabra_inicial not in modelo:
        return f"La palabra '{palabra_inicial}' no está en el modelo."

    frase = [palabra_inicial]
    palabra_actual = palabra_inicial

    for _ in range(longitud - 1):
        siguientes = modelo.get(palabra_actual)
        if not siguientes:
            break  # Si no hay siguiente palabra, detener
        palabras_posibles = list(siguientes.keys())
        probabilidades = list(siguientes.values())
        palabra_siguiente = random.choices(palabras_posibles, probabilidades)[0]
        frase.append(palabra_siguiente)
        palabra_actual = palabra_siguiente

    return ' '.join(frase)

# -------- Función: Mostrar modelo --------
def mostrar_modelo(modelo):
    """
    Muestra las probabilidades del modelo de bigramas.
    """
    print("Modelo de Probabilidades (bigrama):")
    for palabra, transiciones in modelo.items():
        print(f"{palabra} -> {transiciones}")

# -------- Main --------
if __name__ == "__main__":
    # Corpus de ejemplo
    corpus = """
    el perro come croquetas
    el gato come pescado
    el perro ladra
    el gato maulla
    """

    # Preprocesar el corpus
    palabras = preprocesar_corpus(corpus)

    # Crear modelo de bigramas
    modelo_prob = crear_modelo_bigramas(palabras)

    # Mostrar el modelo
    mostrar_modelo(modelo_prob)

    # Generar frases de ejemplo
    print("\nFrase generada desde 'el':")
    print(generar_frase(modelo_prob, 'el'))

    print("\nFrase generada desde 'gato':")
    print(generar_frase(modelo_prob, 'gato'))

    print("\nFrase generada desde 'perro':")
    print(generar_frase(modelo_prob, 'perro'))

    print("\nFrase generada desde 'pescado':")
    print(generar_frase(modelo_prob, 'pescado'))

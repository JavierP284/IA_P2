import numpy as np
from collections import defaultdict

# ----- Paso 1: Corpus de entrenamiento (frases paralelas) -----
# Español (origen)
espanol = [
    ["casa"],
    ["la", "casa"],
    ["una", "casa"],
    ["la", "ventana"],
]

# Inglés (destino)
ingles = [
    ["house"],
    ["the", "house"],
    ["a", "house"],
    ["the", "window"],
]

# Validación: Asegurarse de que las frases en español e inglés tengan el mismo número de elementos
if len(espanol) != len(ingles):
    raise ValueError("El número de frases en español e inglés debe ser igual.")

# ----- Paso 2: Inicializar todas las probabilidades de traducción -----
def inicializar_probabilidades(espanol, ingles):
    """Inicializa las probabilidades de traducción uniformemente."""
    vocab_esp = set(palabra for frase in espanol for palabra in frase)
    vocab_ing = set(palabra for frase in ingles for palabra in frase)
    probabilidades = defaultdict(lambda: defaultdict(float))
    for f in vocab_esp:
        for e in vocab_ing:
            probabilidades[e][f] = 1.0 / len(vocab_ing)
    return probabilidades, vocab_esp, vocab_ing

probabilidades, vocab_esp, vocab_ing = inicializar_probabilidades(espanol, ingles)

# ----- Paso 3: Entrenamiento usando EM (Expectation-Maximization) -----
def entrenar_modelo(espanol, ingles, probabilidades, vocab_esp, vocab_ing, iteraciones=10):
    """Entrena el modelo usando el algoritmo de Expectation-Maximization."""
    for iteracion in range(iteraciones):
        conteo = defaultdict(lambda: defaultdict(float))
        total_f = defaultdict(float)

        # Expectation step
        for esp, eng in zip(espanol, ingles):
            for e in eng:
                Z = sum(probabilidades[e][f] for f in esp)
                for f in esp:
                    c = probabilidades[e][f] / Z
                    conteo[e][f] += c
                    total_f[f] += c

        # Maximization step
        for f in vocab_esp:
            for e in vocab_ing:
                if total_f[f] > 0:
                    probabilidades[e][f] = conteo[e][f] / total_f[f]

entrenar_modelo(espanol, ingles, probabilidades, vocab_esp, vocab_ing)

# ----- Paso 4: Traducción palabra por palabra usando las probabilidades aprendidas -----
def traducir(frase_esp, probabilidades):
    """Traduce una frase en español a inglés usando las probabilidades aprendidas."""
    frase_ing = []
    for f in frase_esp:
        if f not in probabilidades[next(iter(probabilidades))]:
            frase_ing.append("<UNK>")  # Manejo de palabras desconocidas
        else:
            palabra_ingles = max(probabilidades, key=lambda e: probabilidades[e][f])
            frase_ing.append(palabra_ingles)
    return frase_ing

# ----- Paso 5: Mostrar probabilidades aprendidas -----
def mostrar_probabilidades(probabilidades, vocab_esp, vocab_ing):
    """Muestra las probabilidades de traducción aprendidas."""
    print("Probabilidades de traducción (P(e|f)):")
    for f in vocab_esp:
        for e in vocab_ing:
            print(f"P({e}|{f}) = {probabilidades[e][f]:.4f}")

mostrar_probabilidades(probabilidades, vocab_esp, vocab_ing)

# ----- Prueba de traducción -----
frase_test = ["una", "ventana"]
traduccion = traducir(frase_test, probabilidades)

print("\nFrase en español:", frase_test)
print("Traducción generada:", traduccion)

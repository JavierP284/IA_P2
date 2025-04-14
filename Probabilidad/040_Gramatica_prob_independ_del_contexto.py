import random

# -------- Definimos una Gramática Probabilística --------
# La gramática está representada como un diccionario.
# Cada clave es un símbolo no terminal (como "S", "NP", "VP").
# Cada valor es una lista de tuplas, donde:
#   - El primer elemento de la tupla es una producción (lista de símbolos).
#   - El segundo elemento es la probabilidad asociada a esa producción.
gramatica = {
    "S": [
        (["NP", "VP"], 1.0)  # S → NP VP con probabilidad 1
    ],
    "NP": [
        (["Det", "N"], 0.6),      # NP → Det N con probabilidad 0.6
        (["Nombre"], 0.4)         # NP → Nombre con probabilidad 0.4
    ],
    "VP": [
        (["V", "NP"], 0.5),       # VP → V NP con probabilidad 0.5
        (["V"], 0.5)              # VP → V con probabilidad 0.5
    ],
    "Det": [
        (["el"], 0.5),            # Det → "el" con probabilidad 0.5
        (["la"], 0.5)             # Det → "la" con probabilidad 0.5
    ],
    "N": [
        (["perro"], 0.5),         # N → "perro" con probabilidad 0.5
        (["gato"], 0.5)           # N → "gato" con probabilidad 0.5
    ],
    "V": [
        (["come"], 0.5),          # V → "come" con probabilidad 0.5
        (["duerme"], 0.5)         # V → "duerme" con probabilidad 0.5
    ],
    "Nombre": [
        (["Juan"], 0.5),          # Nombre → "Juan" con probabilidad 0.5
        (["Ana"], 0.5)            # Nombre → "Ana" con probabilidad 0.5
    ]
}

# -------- Validación de Gramática --------
# Esta función verifica que las probabilidades de cada conjunto de producciones sumen 1.
# Si no es así, lanza un error indicando el símbolo problemático.
def validar_gramatica(gramatica):
    for simbolo, producciones in gramatica.items():
        suma_probabilidades = sum(prob for _, prob in producciones)
        # Permitimos una pequeña tolerancia para errores de redondeo
        if not (0.99 <= suma_probabilidades <= 1.01):
            raise ValueError(f"Las probabilidades de {simbolo} no suman 1.0: {suma_probabilidades}")

# -------- Función para elegir una producción basada en probabilidad --------
# Esta función selecciona una producción de forma aleatoria, respetando las probabilidades definidas.
def elegir_produccion(producciones):
    reglas, probs = zip(*producciones)  # Separamos las producciones y sus probabilidades
    return random.choices(reglas, probs)[0]  # Elegimos una producción según las probabilidades

# -------- Función para generar una oración --------
# Esta función genera una oración a partir de un símbolo inicial (por defecto "S").
# Si el símbolo es terminal (no está en la gramática), lo devuelve directamente.
# Si es no terminal, elige una producción y la expande recursivamente.
def generar_oracion(simbolo="S", mostrar_proceso=False):
    if simbolo not in gramatica:
        return [simbolo]  # Si es un símbolo terminal, devolverlo como una lista
    produccion = elegir_produccion(gramatica[simbolo])  # Elegir una producción
    if mostrar_proceso:
        print(f"{simbolo} → {' '.join(produccion)}")  # Mostrar la regla seleccionada
    resultado = []
    for simbolo_nuevo in produccion:
        # Expandir recursivamente cada símbolo de la producción
        resultado += generar_oracion(simbolo_nuevo, mostrar_proceso)
    return resultado

# -------- Generar y mostrar oraciones --------
if __name__ == "__main__":
    print("Validando gramática...")
    try:
        validar_gramatica(gramatica)
        print("Gramática válida.\n")
    except ValueError as e:
        print(e)
        exit(1)

    print("Oraciones generadas usando Gramática Probabilística:\n")
    for i in range(5):  # Generar 5 oraciones
        print(f"Oración {i + 1}:")
        oracion = generar_oracion(mostrar_proceso=True)  # Mostrar el proceso de generación
        oracion[0] = oracion[0].capitalize()  # Capitalizar la primera palabra
        print("Resultado final: " + " ".join(oracion) + ".\n")  # Mostrar la oración final

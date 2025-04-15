import random

# ---------- Gramática Probabilística Lexicalizada ----------
# La gramática está representada como un diccionario.
# Cada clave es un símbolo no terminal (como "S", "NP", "VP").
# Cada valor es una lista de reglas de producción.
# Cada regla de producción tiene:
# - Una lista de símbolos hijos (pueden ser terminales o no terminales).
# - Una probabilidad asociada a la regla.
# - Un índice (head_index) que indica cuál hijo es el "head" principal.

gramatica = {
    "S": [
        (["NP", "VP"], 1.0, 1)  # La única regla para "S" produce "NP VP", y el head es "VP".
    ],
    "NP": [
        (["Det", "N"], 0.7, 1),  # "NP" puede ser "Det N" con probabilidad 0.7, y el head es "N".
        (["Nombre"], 0.3, 0)     # "NP" también puede ser un "Nombre" con probabilidad 0.3.
    ],
    "VP": [
        (["V", "NP"], 0.6, 0),   # "VP" puede ser "V NP" con probabilidad 0.6, y el head es "V".
        (["V"], 0.4, 0)          # "VP" también puede ser solo "V" con probabilidad 0.4.
    ],
    "Det": [
        (["el"], 0.5, 0),        # "Det" puede ser "el" con probabilidad 0.5.
        (["la"], 0.5, 0)         # "Det" también puede ser "la" con probabilidad 0.5.
    ],
    "N": [
        (["perro"], 0.5, 0),     # "N" puede ser "perro" con probabilidad 0.5.
        (["gato"], 0.5, 0)       # "N" también puede ser "gato" con probabilidad 0.5.
    ],
    "V": [
        (["ve"], 0.5, 0),        # "V" puede ser "ve" con probabilidad 0.5.
        (["sigue"], 0.5, 0)      # "V" también puede ser "sigue" con probabilidad 0.5.
    ],
    "Nombre": [
        (["Juan"], 0.5, 0),      # "Nombre" puede ser "Juan" con probabilidad 0.5.
        (["Ana"], 0.5, 0)        # "Nombre" también puede ser "Ana" con probabilidad 0.5.
    ]
}

# ---------- Función para elegir una producción basada en probabilidad ----------
def elegir_regla(reglas):
    """
    Selecciona una regla de producción basada en las probabilidades asociadas.
    - reglas: Lista de reglas de producción para un símbolo no terminal.
    Retorna una regla seleccionada aleatoriamente según las probabilidades.
    """
    probs = [r[1] for r in reglas]  # Extraemos las probabilidades de las reglas.
    return random.choices(reglas, probs)[0]  # Seleccionamos una regla usando las probabilidades.

# ---------- Generador de oración con seguimiento de head-words ----------
def generar_oracion(simbolo):
    """
    Genera una oración a partir de un símbolo inicial.
    - simbolo: El símbolo inicial (puede ser terminal o no terminal).
    Retorna:
    - Una lista de palabras que forman la oración generada.
    - El head principal de la oración.
    """
    if simbolo not in gramatica:
        # Caso base: Si el símbolo no está en la gramática, es un terminal.
        return [simbolo], simbolo  # Retornamos el terminal como la oración y el head.

    # Seleccionamos una regla de producción para el símbolo.
    producciones = gramatica[simbolo]
    hijos, _, head_index = elegir_regla(producciones)
    
    resultado = []  # Lista para almacenar las palabras generadas.
    heads = []      # Lista para almacenar los heads de los hijos.
    for hijo in hijos:
        palabras, head = generar_oracion(hijo)  # Generamos recursivamente para cada hijo.
        resultado += palabras  # Agregamos las palabras generadas al resultado.
        heads.append(head)     # Agregamos el head del hijo a la lista de heads.

    # Determinamos el head final basado en el índice head_index.
    head_final = heads[head_index]
    return resultado, head_final  # Retornamos la oración generada y el head principal.

# ---------- Validación de la gramática ----------
def validar_gramatica(gramatica):
    """
    Valida que las probabilidades de cada conjunto de reglas sumen 1.
    - gramatica: Diccionario que representa la gramática.
    Lanza una excepción si las probabilidades no suman 1 para algún símbolo.
    """
    for simbolo, reglas in gramatica.items():
        suma_probs = sum(r[1] for r in reglas)  # Sumamos las probabilidades de las reglas.
        if not (0.99 <= suma_probs <= 1.01):  # Permitimos un margen pequeño de error.
            raise ValueError(f"Las probabilidades para {simbolo} no suman 1: {suma_probs}")

# ---------- Generar oraciones ----------
if __name__ == "__main__":
    # Validamos la gramática antes de generar oraciones.
    validar_gramatica(gramatica)

    # Generamos 5 oraciones y mostramos sus head words.
    for i in range(5):
        oracion, head = generar_oracion("S")  # Generamos una oración a partir del símbolo inicial "S".
        print("Oración:", " ".join(oracion), "| Head Word:", head)  # Mostramos la oración y su head.

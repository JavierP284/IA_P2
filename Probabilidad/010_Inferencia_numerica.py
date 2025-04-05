from itertools import product

# Definición de las variables y sus posibles valores
variables = {
    "Nublado": [True, False],
    "Rain": [True, False],
    "Sprinkler": [True, False],
    "Pasto mojado": [True, False]
}

# Probabilidades condicionales y marginales de la red bayesiana
def P(var, value, evidence):
    """
    Calcula la probabilidad de una variable dado su valor y la evidencia.
    """
    if var == "Nublado":
        # Probabilidad marginal: P(Nublado)
        return 0.5 if value else 0.5

    elif var == "Rain":
        # Probabilidad condicional: P(Rain | Nublado)
        if value:
            return 0.8 if evidence["Nublado"] else 0.2
        else:
            return 0.2 if evidence["Nublado"] else 0.8

    elif var == "Sprinkler":
        # Probabilidad condicional: P(Sprinkler | Nublado)
        if value:
            return 0.1 if evidence["Nublado"] else 0.5
        else:
            return 0.9 if evidence["Nublado"] else 0.5

    elif var == "Pasto mojado":
        # Probabilidad condicional: P(Pasto mojado | Sprinkler, Rain)
        sprinkler = evidence["Sprinkler"]
        rain = evidence["Rain"]
        if sprinkler and rain:
            return 0.99 if value else 0.01
        elif sprinkler and not rain:
            return 0.90 if value else 0.10
        elif not sprinkler and rain:
            return 0.90 if value else 0.10
        else:
            return 0.0 if value else 1.0

# Algoritmo de inferencia por enumeración
def enumeration_ask(query_var, evidence):
    """
    Calcula la distribución de probabilidad de una variable de consulta
    dado un conjunto de evidencia.
    """
    probabilities = {}  # Diccionario para guardar las probabilidades

    for value in variables[query_var]:
        # Extendemos la evidencia con el valor asumido de la variable de consulta
        extended_evidence = evidence.copy()
        extended_evidence[query_var] = value

        # Llamamos a la función recursiva para calcular la probabilidad
        probabilities[value] = enumerate_all(list(variables.keys()), extended_evidence)

    # Normalización para que las probabilidades sumen 1
    total = sum(probabilities.values())
    for val in probabilities:
        probabilities[val] /= total

    return probabilities

def enumerate_all(vars_list, evidence):
    """
    Calcula la suma de probabilidades de todas las combinaciones posibles
    de las variables restantes.
    """
    if not vars_list:
        return 1.0  # Caso base: ya no hay variables por procesar

    first = vars_list[0]
    rest = vars_list[1:]

    if first in evidence:
        # Si la variable ya tiene un valor en la evidencia, usamos directamente su probabilidad
        prob = P(first, evidence[first], evidence)
        return prob * enumerate_all(rest, evidence)
    else:
        # Si la variable no está en la evidencia, iteramos sobre todos sus valores posibles
        total = 0
        for val in variables[first]:
            new_evidence = evidence.copy()
            new_evidence[first] = val
            prob = P(first, val, new_evidence)
            total += prob * enumerate_all(rest, new_evidence)
        return total

# -------------------------------
# EJEMPLO DE EJECUCIÓN
# -------------------------------

# Consulta: ¿Cuál es la probabilidad de que esté nublado si el pasto está mojado?
query_variable = "Nublado"
evidence = {"Pasto mojado": True}

# Realizamos la consulta
resultado = enumeration_ask(query_variable, evidence)

# Mostramos el resultado de manera más legible
print(f"P({query_variable} | {evidence}):")
for value, prob in resultado.items():
    print(f"  {query_variable} = {value}: {prob:.4f}")

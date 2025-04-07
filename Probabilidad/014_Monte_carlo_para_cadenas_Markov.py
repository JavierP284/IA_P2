import random
from collections import Counter

# Tabla de Probabilidades Condicionales (CPTs)
CPT = {
    "Nublado": {
        (): {True: 0.5, False: 0.5}
    },
    "Aspersor": {
        (True,): {True: 0.1, False: 0.9},
        (False,): {True: 0.5, False: 0.5}
    },
    "Llovizna": {
        (True,): {True: 0.8, False: 0.2},
        (False,): {True: 0.2, False: 0.8}
    },
    "PastoMojado": {
        (True, True): {True: 0.99, False: 0.01},
        (True, False): {True: 0.90, False: 0.10},
        (False, True): {True: 0.90, False: 0.10},
        (False, False): {True: 0.0, False: 1.0}
    }
}

# Relaciones entre nodos (padres)
padres = {
    "Nublado": [],
    "Aspersor": ["Nublado"],
    "Llovizna": ["Nublado"],
    "PastoMojado": ["Aspersor", "Llovizna"]
}

# -------------------------------
# Algoritmo MCMC - Metropolis-Hastings
# -------------------------------
def mcmc(consulta, evidencia, num_muestras=10000, semilla=None):
    """
    Implementa el algoritmo MCMC para calcular la probabilidad de una variable de consulta
    dado un conjunto de evidencia.

    Parámetros:
    - consulta: str, la variable de la que queremos calcular la probabilidad.
    - evidencia: dict, un diccionario con las variables de evidencia y sus valores.
    - num_muestras: int, el número de muestras a generar (por defecto 10,000).
    - semilla: int, semilla para el generador aleatorio (opcional, para reproducibilidad).

    Retorna:
    - dict, un diccionario con las probabilidades normalizadas de la variable de consulta.
    """
    if semilla is not None:
        random.seed(semilla)  # Establecer semilla para reproducibilidad

    # Validar que la consulta y la evidencia sean válidas
    if consulta not in CPT:
        raise ValueError(f"La variable de consulta '{consulta}' no está definida en el modelo.")
    for var in evidencia:
        if var not in CPT:
            raise ValueError(f"La variable de evidencia '{var}' no está definida en el modelo.")

    # Inicializar el estado aleatoriamente respetando la evidencia
    estado = {
        "Nublado": random.choice([True, False]),
        "Aspersor": random.choice([True, False]),
        "Llovizna": random.choice([True, False]),
        "PastoMojado": evidencia.get("PastoMojado", random.choice([True, False]))
    }

    # Asegurarse de que las variables de evidencia tengan los valores correctos
    for var, valor in evidencia.items():
        estado[var] = valor

    conteo = Counter()  # Contador para las ocurrencias de la variable de consulta

    # Generar muestras
    for _ in range(num_muestras):
        for variable in estado:
            if variable in evidencia:
                continue  # No cambiamos las variables de evidencia

            # Proponer un nuevo valor para la variable (inversión del valor actual)
            nuevo_estado = estado.copy()
            nuevo_estado[variable] = not estado[variable]

            # Función para calcular la probabilidad de un estado
            def prob_estado(s):
                prob = 1.0
                for var in CPT:
                    padres_var = tuple(s[p] for p in padres[var])  # Obtener valores de los padres
                    prob *= CPT[var][padres_var][s[var]]  # Multiplicar las probabilidades
                return prob

            # Calcular las probabilidades del estado actual y del propuesto
            p_actual = prob_estado(estado)
            p_nuevo = prob_estado(nuevo_estado)

            # Aceptar el nuevo estado con probabilidad min(1, p_nuevo / p_actual)
            if random.random() < min(1, p_nuevo / p_actual):
                estado = nuevo_estado

        # Contar la ocurrencia del valor actual de la variable de consulta
        conteo[estado[consulta]] += 1

    # Normalizar los resultados para obtener probabilidades
    total = sum(conteo.values())
    return {k: v / total for k, v in conteo.items()}


# Ejemplo de uso
if __name__ == "__main__":
    print("MCMC - P(Llovizna | PastoMojado=True):")
    resultado = mcmc("Llovizna", {"PastoMojado": True}, num_muestras=10000, semilla=42)
    for valor, probabilidad in resultado.items():
        print(f"  P(Llovizna={valor}) = {probabilidad:.4f}")

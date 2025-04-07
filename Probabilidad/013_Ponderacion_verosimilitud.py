import random
from collections import Counter

# Tabla de Probabilidades Condicionales (CPTs)
# Representa las probabilidades condicionales de cada nodo en la red bayesiana.
CPT = {
    "Nublado": {
        (): {True: 0.5, False: 0.5}  # Probabilidad de que esté nublado (sin padres).
    },
    "Aspersor": {
        (True,): {True: 0.1, False: 0.9},  # Probabilidad de que el aspersor esté activado si está nublado.
        (False,): {True: 0.5, False: 0.5}  # Probabilidad de que el aspersor esté activado si no está nublado.
    },
    "Llovizna": {
        (True,): {True: 0.8, False: 0.2},  # Probabilidad de llovizna si está nublado.
        (False,): {True: 0.2, False: 0.8}  # Probabilidad de llovizna si no está nublado.
    },
    "PastoMojado": {
        # Probabilidad de que el pasto esté mojado dependiendo del estado del aspersor y la llovizna.
        (True, True): {True: 0.99, False: 0.01},
        (True, False): {True: 0.90, False: 0.10},
        (False, True): {True: 0.90, False: 0.10},
        (False, False): {True: 0.0, False: 1.0}
    }
}

# Relaciones entre nodos (padres)
# Define qué nodos son padres de otros en la red bayesiana.
padres = {
    "Nublado": [],  # "Nublado" no tiene padres.
    "Aspersor": ["Nublado"],  # "Aspersor" depende de "Nublado".
    "Llovizna": ["Nublado"],  # "Llovizna" depende de "Nublado".
    "PastoMojado": ["Aspersor", "Llovizna"]  # "PastoMojado" depende de "Aspersor" y "Llovizna".
}

def ponderacion_verosimilitud(consulta, evidencia, num_muestras=10000):
    """
    Algoritmo de ponderación por verosimilitud para redes bayesianas.

    Args:
        consulta (str): Variable de consulta.
        evidencia (dict): Variables de evidencia con sus valores (True/False).
        num_muestras (int): Número de muestras a generar.

    Returns:
        dict: Distribución de probabilidad de la variable de consulta.
    """
    # Validación de entrada
    if consulta not in CPT:
        raise ValueError(f"La variable de consulta '{consulta}' no está en la red.")
    for var in evidencia:
        if var not in CPT:
            raise ValueError(f"La variable de evidencia '{var}' no está en la red.")
        if evidencia[var] not in [True, False]:
            raise ValueError(f"El valor de evidencia para '{var}' debe ser True o False.")

    # Inicializamos contadores para las muestras y los pesos
    conteo = Counter()  # Contador para los valores de la variable de consulta.
    pesos = Counter()   # Contador para los pesos totales.

    # Generamos muestras
    for _ in range(num_muestras):
        muestra = {}  # Diccionario para almacenar la muestra generada.
        peso = 1.0    # Peso inicial de la muestra.

        # Iteramos sobre las variables en el orden topológico de la red.
        for variable in ["Nublado", "Aspersor", "Llovizna", "PastoMojado"]:
            # Obtenemos los valores de los padres de la variable actual.
            padres_var = tuple(muestra[p] for p in padres[variable])
            # Obtenemos las probabilidades condicionales de la variable actual.
            probs = CPT[variable][padres_var]

            if variable in evidencia:
                # Si la variable es evidencia, no se muestrea, solo se ajusta el peso.
                muestra[variable] = evidencia[variable]
                peso *= probs[evidencia[variable]]  # Actualizamos el peso según la probabilidad.
            else:
                # Si no es evidencia, se genera un valor aleatorio basado en las probabilidades.
                muestra[variable] = random.choices([True, False], weights=[probs[True], probs[False]])[0]

        # Actualizamos el conteo ponderado de la variable de consulta.
        conteo[muestra[consulta]] += peso
        pesos["total"] += peso  # Actualizamos el peso total.

    # Normalizamos los conteos para obtener una distribución de probabilidad.
    return {k: v / pesos["total"] for k, v in conteo.items()}

# Ejemplo de uso
if __name__ == "__main__":
    # Fijamos una semilla para reproducibilidad de los resultados.
    random.seed(42)
    print("Ponderación de Verosimilitud - P(Llovizna | PastoMojado=True):")
    # Llamamos al algoritmo con la consulta "Llovizna" y la evidencia "PastoMojado=True".
    resultado = ponderacion_verosimilitud("Llovizna", {"PastoMojado": True})
    # Mostramos los resultados de forma legible.
    for valor, prob in resultado.items():
        print(f"{valor}: {prob:.4f}")

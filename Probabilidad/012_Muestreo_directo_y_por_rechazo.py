import random
from collections import Counter

# Tabla de probabilidades condicionales (CPTs)
# Representa las probabilidades condicionales de cada variable en el modelo.
CPT = {
    "Nublado": {
        (): {True: 0.5, False: 0.5}  # Probabilidad de que esté nublado (sin padres).
    },
    "Aspersor": {
        (True,): {True: 0.1, False: 0.9},  # Probabilidad de que el aspersor esté activado dado que está nublado.
        (False,): {True: 0.5, False: 0.5}  # Probabilidad de que el aspersor esté activado dado que no está nublado.
    },
    "Llovizna": {
        (True,): {True: 0.8, False: 0.2},  # Probabilidad de llovizna dado que está nublado.
        (False,): {True: 0.2, False: 0.8}  # Probabilidad de llovizna dado que no está nublado.
    },
    "PastoMojado": {
        (True, True): {True: 0.99, False: 0.01},  # Probabilidad de pasto mojado dado que el aspersor y la llovizna están activados.
        (True, False): {True: 0.90, False: 0.10},  # Probabilidad de pasto mojado dado que solo el aspersor está activado.
        (False, True): {True: 0.90, False: 0.10},  # Probabilidad de pasto mojado dado que solo la llovizna está activada.
        (False, False): {True: 0.0, False: 1.0}    # Probabilidad de pasto mojado dado que ni el aspersor ni la llovizna están activados.
    }
}

# Dependencias (padres)
# Define las relaciones entre las variables del modelo.
padres = {
    "Nublado": [],  # "Nublado" no tiene padres.
    "Aspersor": ["Nublado"],  # "Aspersor" depende de "Nublado".
    "Llovizna": ["Nublado"],  # "Llovizna" depende de "Nublado".
    "PastoMojado": ["Aspersor", "Llovizna"]  # "PastoMojado" depende de "Aspersor" y "Llovizna".
}

# Función auxiliar para muestrear una variable dada la evidencia
def muestrear_variable(variable, evidencia):
    """
    Muestrea una variable aleatoria dada la evidencia actual.
    - variable: Nombre de la variable a muestrear.
    - evidencia: Diccionario con los valores actuales de las variables observadas.
    """
    # Obtiene los valores de los padres de la variable en la evidencia.
    key = tuple(evidencia[p] for p in padres[variable])
    # Obtiene las probabilidades condicionales de la variable dado los valores de sus padres.
    probs = CPT[variable][key]
    # Realiza un muestreo aleatorio basado en las probabilidades.
    return random.choices([True, False], weights=[probs[True], probs[False]])[0]

# Muestreo Directo (Prior Sampling)
def muestreo_directo(consulta, evidencia, num_muestras=10000):
    """
    Realiza muestreo directo para estimar P(consulta | evidencia).
    - consulta: Variable de interés.
    - evidencia: Diccionario con las variables observadas y sus valores.
    - num_muestras: Número de muestras a generar.
    """
    cuenta = Counter()  # Contador para registrar las ocurrencias de la variable de consulta.

    for _ in range(num_muestras):
        muestra = {}  # Diccionario para almacenar los valores generados en la muestra.
        for var in ["Nublado", "Aspersor", "Llovizna", "PastoMojado"]:
            # Muestrea cada variable en orden, respetando las dependencias.
            muestra[var] = muestrear_variable(var, muestra)

        # Verifica si la muestra concuerda con la evidencia.
        if all(muestra[k] == v for k, v in evidencia.items()):
            # Incrementa el contador para el valor de la consulta en esta muestra.
            cuenta[muestra[consulta]] += 1

    total = sum(cuenta.values())  # Total de muestras válidas.
    if total == 0:
        return "Sin muestras válidas"  # Si no hay muestras que cumplan con la evidencia.
    # Calcula las probabilidades normalizadas.
    return {k: v / total for k, v in cuenta.items()}

# Muestreo por Rechazo (Rejection Sampling)
def muestreo_por_rechazo(consulta, evidencia, num_muestras=10000):
    """
    Realiza muestreo por rechazo para estimar P(consulta | evidencia).
    - consulta: Variable de interés.
    - evidencia: Diccionario con las variables observadas y sus valores.
    - num_muestras: Número de muestras a generar.
    """
    cuenta = Counter()  # Contador para registrar las ocurrencias de la variable de consulta.
    aceptadas = 0  # Contador de muestras aceptadas (que cumplen con la evidencia).

    for _ in range(num_muestras):
        muestra = {}  # Diccionario para almacenar los valores generados en la muestra.
        for var in ["Nublado", "Aspersor", "Llovizna", "PastoMojado"]:
            # Muestrea cada variable en orden, respetando las dependencias.
            muestra[var] = muestrear_variable(var, muestra)

        # Verifica si la muestra cumple con toda la evidencia.
        if all(muestra.get(k) == v for k, v in evidencia.items()):
            # Incrementa el contador para el valor de la consulta en esta muestra.
            cuenta[muestra[consulta]] += 1
            aceptadas += 1  # Incrementa el contador de muestras aceptadas.

    if aceptadas == 0:
        return "Sin muestras aceptadas"  # Si no hay muestras que cumplan con la evidencia.
    
    # Calcula las probabilidades normalizadas y devuelve estadísticas adicionales.
    return {
        "Probabilidades": {k: v / aceptadas for k, v in cuenta.items()},
        "Aceptadas": aceptadas,
        "PorcentajeAceptadas": aceptadas / num_muestras * 100
    }

# Función principal para ejecutar ejemplos
def main():
    """
    Ejecuta ejemplos de muestreo directo y por rechazo.
    """
    # Configuración del ejemplo: consulta, evidencia y número de muestras.
    consulta = "Llovizna"  # Variable de interés.
    evidencia = {"PastoMojado": True}  # Evidencia observada.
    num_muestras = 10000  # Número de muestras a generar.

    # Ejemplo de muestreo directo.
    print("Muestreo Directo - P(Llovizna | PastoMojado=True):")
    resultado_directo = muestreo_directo(consulta, evidencia, num_muestras)
    print(resultado_directo)

    # Ejemplo de muestreo por rechazo.
    print("\nMuestreo por Rechazo - P(Llovizna | PastoMojado=True):")
    resultado_rechazo = muestreo_por_rechazo(consulta, evidencia, num_muestras)
    print(resultado_rechazo)

# Ejecutar la función principal
if __name__ == "__main__":
    main()

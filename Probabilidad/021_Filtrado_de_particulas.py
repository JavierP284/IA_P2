import numpy as np
import random
from collections import Counter
import matplotlib.pyplot as plt

# -------------------------------
# 1. Parámetros del modelo
# -------------------------------

# Estados ocultos del modelo (clima)
estados = ["Soleado", "Lluvioso"]

# Observaciones posibles (si alguien lleva paraguas o no)
observaciones = ["Paraguas", "NoParaguas"]

# Matriz de transición: Probabilidad de cambiar de un estado a otro
P_transicion = {
    "Soleado": {"Soleado": 0.7, "Lluvioso": 0.3},
    "Lluvioso": {"Soleado": 0.4, "Lluvioso": 0.6}
}

# Matriz de emisión: Probabilidad de observar algo dado un estado
P_emision = {
    "Soleado": {"Paraguas": 0.1, "NoParaguas": 0.9},
    "Lluvioso": {"Paraguas": 0.8, "NoParaguas": 0.2}
}

# -------------------------------
# 2. Función de validación
# -------------------------------

def validar_entradas(observaciones_dadas):
    """Valida que las observaciones sean válidas."""
    for obs in observaciones_dadas:
        if obs not in observaciones:
            raise ValueError(f"Observación inválida: {obs}. Las observaciones válidas son: {observaciones}")

# -------------------------------
# 3. Función de inicialización de partículas
# -------------------------------

def inicializar_particulas(num_particulas, estados, distribucion_inicial=None):
    """Inicializa las partículas con una distribución uniforme o personalizada."""
    if distribucion_inicial is None:
        # Distribución uniforme por defecto
        return [random.choice(estados) for _ in range(num_particulas)]
    else:
        # Distribución personalizada
        return random.choices(estados, weights=[distribucion_inicial[e] for e in estados], k=num_particulas)

# -------------------------------
# 4. Función de filtrado de partículas
# -------------------------------

def filtrado_particulas(observaciones_dadas, num_particulas=1000):
    """Aplica el algoritmo de filtrado de partículas para estimar estados ocultos."""
    validar_entradas(observaciones_dadas)
    
    # Inicializamos partículas aleatoriamente
    particulas = inicializar_particulas(num_particulas, estados)

    estimaciones = []

    for t, obs in enumerate(observaciones_dadas):
        # 1. PREDICCIÓN: transicionamos cada partícula al siguiente estado
        nuevas_particulas = []
        for p in particulas:
            trans_probs = P_transicion[p]
            nueva = random.choices(estados, weights=[trans_probs[e] for e in estados])[0]
            nuevas_particulas.append(nueva)

        # 2. ACTUALIZACIÓN: asignamos pesos según la observación
        pesos = []
        for p in nuevas_particulas:
            peso = P_emision[p][obs]
            pesos.append(peso)

        # Manejo de pesos nulos
        if sum(pesos) == 0:
            print(f"Advertencia: Todos los pesos son cero en el tiempo {t+1}. Reajustando a distribución uniforme.")
            pesos = [1] * len(nuevas_particulas)

        # 3. RE-MUESTREO: elegimos nuevas partículas según los pesos
        particulas = random.choices(
            nuevas_particulas, weights=pesos, k=num_particulas
        )

        # 4. Estimación: frecuencia relativa de los estados
        cuenta = Counter(particulas)
        total = sum(cuenta.values())
        estimacion = {estado: cuenta[estado] / total for estado in estados}
        estimaciones.append(estimacion)

    return estimaciones

# -------------------------------
# 5. Función de visualización
# -------------------------------

def graficar_estimaciones(estimaciones):
    """Grafica la evolución de las probabilidades estimadas."""
    tiempos = range(1, len(estimaciones) + 1)
    soleado = [est["Soleado"] for est in estimaciones]
    lluvioso = [est["Lluvioso"] for est in estimaciones]

    plt.plot(tiempos, soleado, label="P(Soleado)", marker="o")
    plt.plot(tiempos, lluvioso, label="P(Lluvioso)", marker="o")
    plt.xlabel("Tiempo")
    plt.ylabel("Probabilidad")
    plt.title("Evolución de las probabilidades estimadas")
    plt.legend()
    plt.grid()
    plt.show()

# -------------------------------
# 6. Ejecución del algoritmo
# -------------------------------

# Observaciones simuladas
observaciones_dadas = ["Paraguas", "Paraguas", "NoParaguas", "Paraguas", "NoParaguas"]

# Aplicar filtrado de partículas
estimaciones = filtrado_particulas(observaciones_dadas, num_particulas=1000)

# Mostrar resultados
print("Filtrado de Partículas - Estimación del clima oculto:")
for t, est in enumerate(estimaciones):
    print(f"Tiempo {t+1}: P(Soleado) = {est['Soleado']:.3f}, P(Lluvioso) = {est['Lluvioso']:.3f}")

# Graficar resultados
graficar_estimaciones(estimaciones)

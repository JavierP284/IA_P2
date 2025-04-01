import numpy as np

# Estados posibles del clima
estados = ["Soleado", "Lluvioso"]

# Observaciones posibles (lo que podemos medir)
observaciones = ["Suelo Mojado", "Suelo Seco"]

# Probabilidad de transición P(Clima_t | Clima_t-1)
transiciones = {
    "Soleado": {"Soleado": 0.8, "Lluvioso": 0.2},
    "Lluvioso": {"Soleado": 0.4, "Lluvioso": 0.6}
}

# Probabilidad de observación P(Observación | Clima)
obs_modelo = {
    "Soleado": {"Suelo Mojado": 0.1, "Suelo Seco": 0.9},
    "Lluvioso": {"Suelo Mojado": 0.8, "Suelo Seco": 0.2}
}

# Probabilidad inicial (día 0)
creencias = {"Soleado": 0.5, "Lluvioso": 0.5}

def actualizar_creencias(creencias, observacion):
    nueva_creencia = {s: 0.0 for s in estados}
    
    # Paso 1: Predicción (Aplicar la transición)
    for s in estados:
        suma = sum(transiciones[s_anterior][s] * creencias[s_anterior] for s_anterior in estados)
        nueva_creencia[s] = suma  # P(Clima_t) = ∑ P(Clima_t | Clima_t-1) * P(Clima_t-1)

    # Paso 2: Corrección con la observación
    for s in estados:
        nueva_creencia[s] *= obs_modelo[s][observacion]  # P(Clima_t | Obs_t) ∝ P(Obs_t | Clima_t) * P(Clima_t)

    # Paso 3: Normalización
    total = sum(nueva_creencia.values())
    if total > 0:
        for s in nueva_creencia:
            nueva_creencia[s] /= total  # Normalizamos para que las probabilidades sumen 1

    return nueva_creencia

# Simulación de 3 días con observaciones
observaciones_recibidas = ["Suelo Mojado", "Suelo Seco", "Suelo Mojado"]

print("\nDía 0: Estado inicial de creencias:")
for estado, probabilidad in creencias.items():
    print(f"{estado}: {probabilidad:.2f}")

for i in range(len(observaciones_recibidas)):
    observacion = observaciones_recibidas[i]
    
    print(f"\nDía {i+1}:")
    print(f"- Observación recibida: {observacion}")
    
    creencias = actualizar_creencias(creencias, observacion)
    
    print("- Nueva distribución de creencias:")
    for estado, probabilidad in creencias.items():
        print(f"  {estado}: {probabilidad:.2f}")

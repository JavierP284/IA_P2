import numpy as np

# Definimos los estados posibles
estados = ["Sala 1", "Sala 2", "Sala 3"]

# Definimos las acciones posibles
acciones = ["Mover Izquierda", "Mover Derecha", "Quedarse"]

# Definimos las observaciones posibles
observaciones = ["Cerca de la puerta", "En el centro"]

# Probabilidad de transición P(s' | s, a)
transiciones = {
    "Sala 1": {"Mover Derecha": {"Sala 2": 1.0}, "Mover Izquierda": {"Sala 1": 1.0}, "Quedarse": {"Sala 1": 1.0}},
    "Sala 2": {"Mover Izquierda": {"Sala 1": 0.8, "Sala 2": 0.2}, 
               "Mover Derecha": {"Sala 3": 0.8, "Sala 2": 0.2}, 
               "Quedarse": {"Sala 2": 1.0}},
    "Sala 3": {"Mover Izquierda": {"Sala 2": 1.0}, "Mover Derecha": {"Sala 3": 1.0}, "Quedarse": {"Sala 3": 1.0}}
}

# Probabilidad de observación P(o | s)
obs_modelo = {
    "Sala 1": {"Cerca de la puerta": 0.9, "En el centro": 0.1},
    "Sala 2": {"Cerca de la puerta": 0.5, "En el centro": 0.5},
    "Sala 3": {"Cerca de la puerta": 0.2, "En el centro": 0.8}
}

# Inicializar la creencia (probabilidad de estar en cada estado)
creencias = {"Sala 1": 1.0, "Sala 2": 0.0, "Sala 3": 0.0}  # Comenzamos con certeza en la Sala 1

def actualizar_creencias(creencias, accion, observacion):
    if accion not in acciones:
        raise ValueError(f"Acción no válida: {accion}")
    if observacion not in observaciones:
        raise ValueError(f"Observación no válida: {observacion}")
    
    nueva_creencia = {s: 0.0 for s in estados}
    
    # Calcular la nueva creencia usando la regla de Bayes
    for s in estados:
        prob_obs_dado_estado = obs_modelo[s].get(observacion, 0)  # P(o | s)
        suma = 0
        for s_anterior in estados:
            if accion in transiciones[s_anterior]:  # Verifica si la acción existe
                prob_transicion = transiciones[s_anterior][accion].get(s, 0)  # P(s' | s, a)
                suma += prob_transicion * creencias[s_anterior]  # Sumar contribuciones desde cada estado
        
        nueva_creencia[s] = prob_obs_dado_estado * suma  # P(s' | o, a) ∝ P(o | s') * ∑ P(s' | s, a) * b(s)
    
    # Normalizar la distribución de creencias
    total = sum(nueva_creencia.values())
    if total > 0:
        for s in nueva_creencia:
            nueva_creencia[s] /= total  # Normalización
    
    return nueva_creencia

# Simulación del POMDP
acciones_tomadas = ["Mover Derecha", "Mover Derecha", "Mover Izquierda"]
observaciones_recibidas = ["Cerca de la puerta", "En el centro", "Cerca de la puerta"]

print("\nEstado inicial de creencias:")
for estado, probabilidad in creencias.items():
    print(f"{estado}: {probabilidad:.2f}")

for i in range(len(acciones_tomadas)):
    accion = acciones_tomadas[i]
    observacion = observaciones_recibidas[i]
    
    print(f"\nPaso {i+1}:")
    print(f"- Acción tomada: {accion}")
    print(f"- Observación recibida: {observacion}")
    
    try:
        creencias = actualizar_creencias(creencias, accion, observacion)
    except ValueError as e:
        print(f"Error: {e}")
        break
    
    print("- Nueva distribución de creencias:")
    for estado, probabilidad in creencias.items():
        print(f"  {estado}: {probabilidad:.2f}")

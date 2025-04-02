import numpy as np

# Probabilidades a priori (antes de observar los síntomas)
p_gripe = 0.1   # 10% de probabilidad de tener gripe
p_alergia = 0.3  # 30% de probabilidad de tener alergia
p_sano = 0.6     # 60% de probabilidad de estar sano

# Probabilidades de presentar fiebre dado cada caso
p_fiebre_dado_gripe = 0.8  # 80% de los que tienen gripe tienen fiebre
p_fiebre_dado_alergia = 0.2  # 20% de los que tienen alergia tienen fiebre
p_fiebre_dado_sano = 0.1  # 10% de los sanos tienen fiebre

# Probabilidad total de fiebre (usando la regla de la probabilidad total)
p_fiebre = (p_gripe * p_fiebre_dado_gripe) + \
           (p_alergia * p_fiebre_dado_alergia) + \
           (p_sano * p_fiebre_dado_sano)

def calcular_probabilidad_condicionada(p_estado, p_fiebre_dado_estado, p_fiebre):
    return (p_estado * p_fiebre_dado_estado) / p_fiebre

# Aplicamos el Teorema de Bayes para obtener las probabilidades condicionadas
p_gripe_dado_fiebre = calcular_probabilidad_condicionada(p_gripe, p_fiebre_dado_gripe, p_fiebre)
p_alergia_dado_fiebre = calcular_probabilidad_condicionada(p_alergia, p_fiebre_dado_alergia, p_fiebre)
p_sano_dado_fiebre = calcular_probabilidad_condicionada(p_sano, p_fiebre_dado_sano, p_fiebre)

# Normalización: los valores ya están normalizados porque suman 1
normalizacion = p_gripe_dado_fiebre + p_alergia_dado_fiebre + p_sano_dado_fiebre

# Mostramos los resultados
print(f"Probabilidad de tener gripe dado que hay fiebre: {p_gripe_dado_fiebre:.4f}")
print(f"Probabilidad de tener alergia dado que hay fiebre: {p_alergia_dado_fiebre:.4f}")
print(f"Probabilidad de estar sano dado que hay fiebre: {p_sano_dado_fiebre:.4f}")
print(f"Verificación de normalización: {normalizacion:.4f} (debe ser aproximadamente 1)")

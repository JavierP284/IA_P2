import numpy as np

# Definir probabilidades iniciales en un diccionario
probabilidades = {
    "P_Gripe": 0.1,  # Probabilidad base de tener gripe (10%)
    "P_Fiebre_Gripe": 0.8,  # Probabilidad de fiebre si hay gripe (80%)
    "P_Tos_Gripe": 0.7,  # Probabilidad de tos si hay gripe (70%)
    "P_Fiebre_NoGripe": 0.2,  # Probabilidad de fiebre sin gripe (20%)
    "P_Tos_NoGripe": 0.3,  # Probabilidad de tos sin gripe (30%)
}

def calcular_probabilidad_sintomas(tiene_fiebre, tiene_tos, con_gripe, probabilidades):
    """
    Calcula P(Síntomas | Gripe) o P(Síntomas | No Gripe) según el caso.
    """
    P_Fiebre = probabilidades["P_Fiebre_Gripe"] if con_gripe else probabilidades["P_Fiebre_NoGripe"]
    P_Tos = probabilidades["P_Tos_Gripe"] if con_gripe else probabilidades["P_Tos_NoGripe"]
    
    P_Sintomas = (P_Fiebre if tiene_fiebre else 1 - P_Fiebre) * \
                 (P_Tos if tiene_tos else 1 - P_Tos)
    return P_Sintomas

def calcular_probabilidad_gripe(tiene_fiebre, tiene_tos, probabilidades):
    """
    Calcula la probabilidad de que una persona tenga gripe dado que presenta síntomas
    usando el Teorema de Bayes.
    """
    P_Gripe = probabilidades["P_Gripe"]
    P_NoGripe = 1 - P_Gripe

    # P(Síntomas | Gripe) y P(Síntomas | No Gripe)
    P_Sintomas_Gripe = calcular_probabilidad_sintomas(tiene_fiebre, tiene_tos, True, probabilidades)
    P_Sintomas_NoGripe = calcular_probabilidad_sintomas(tiene_fiebre, tiene_tos, False, probabilidades)

    # P(Síntomas) = P(Síntomas | Gripe) * P(Gripe) + P(Síntomas | No Gripe) * P(No Gripe)
    P_Sintomas = P_Sintomas_Gripe * P_Gripe + P_Sintomas_NoGripe * P_NoGripe

    # Aplicamos el Teorema de Bayes
    P_Gripe_Dado_Sintomas = (P_Sintomas_Gripe * P_Gripe) / P_Sintomas

    return P_Gripe_Dado_Sintomas

# Simulaciones de diferentes escenarios
casos = [
    (True, True),  # Tiene fiebre y tos
    (True, False),  # Tiene fiebre, pero no tos
    (False, True),  # No tiene fiebre, pero tiene tos
    (False, False)  # No tiene fiebre ni tos
]

print("Resultados de probabilidad de gripe según síntomas:")
for fiebre, tos in casos:
    probabilidad = calcular_probabilidad_gripe(fiebre, tos, probabilidades)
    print(f"Fiebre: {fiebre}, Tos: {tos} → Probabilidad de gripe: {probabilidad:.2%}")

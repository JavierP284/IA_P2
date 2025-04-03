# Importamos la librería numpy para cálculos numéricos
import numpy as np

# Función que aplica la Regla de Bayes
def regla_de_bayes(P_B_dado_A, P_A, P_B):
    """
    Calcula la probabilidad P(A|B) usando la Regla de Bayes:
    
    P(A|B) = (P(B|A) * P(A)) / P(B)
    
    Parámetros:
    - P_B_dado_A: Probabilidad de B dado A (P(B|A))
    - P_A: Probabilidad de A (P(A))
    - P_B: Probabilidad de B (P(B))
    
    Retorna:
    - P(A|B): Probabilidad de A dado B
    """
    if not (0 <= P_B_dado_A <= 1 and 0 <= P_A <= 1 and 0 <= P_B <= 1):
        raise ValueError("Todas las probabilidades deben estar en el rango [0, 1].")
    if P_B == 0:
        raise ZeroDivisionError("P(B) no puede ser 0 para aplicar la Regla de Bayes.")
    
    return (P_B_dado_A * P_A) / P_B

# Función para calcular P(B) usando la ley de la probabilidad total
def calcular_probabilidad_total(P_B_dado_A, P_A, P_B_dado_no_A):
    """
    Calcula la probabilidad total P(B) usando la ley de la probabilidad total:
    
    P(B) = P(B|A) * P(A) + P(B|¬A) * P(¬A)
    
    Parámetros:
    - P_B_dado_A: Probabilidad de B dado A (P(B|A))
    - P_A: Probabilidad de A (P(A))
    - P_B_dado_no_A: Probabilidad de B dado no A (P(B|¬A))
    
    Retorna:
    - P(B): Probabilidad total de B
    """
    if not (0 <= P_B_dado_no_A <= 1 and 0 <= P_A <= 1):
        raise ValueError("Todas las probabilidades deben estar en el rango [0, 1].")
    
    P_no_A = 1 - P_A  # Probabilidad de que NO ocurra A
    return (P_B_dado_A * P_A) + (P_B_dado_no_A * P_no_A)

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos probabilidades dadas
    P_A = 0.02  # Probabilidad de que una persona tenga una enfermedad (P(A))
    P_B_dado_A = 0.95  # Probabilidad de que la prueba sea positiva si tiene la enfermedad (P(B|A))
    P_B_dado_no_A = 0.10  # Probabilidad de que la prueba sea positiva si NO tiene la enfermedad (falso positivo)

    # Calculamos P(B)
    P_B = calcular_probabilidad_total(P_B_dado_A, P_A, P_B_dado_no_A)

    # Aplicamos la Regla de Bayes para calcular P(A|B)
    P_A_dado_B = regla_de_bayes(P_B_dado_A, P_A, P_B)

    # Mostramos los resultados
    print(f"P(A) = {P_A:.4f}  -> Probabilidad de tener la enfermedad")
    print(f"P(B|A) = {P_B_dado_A:.4f}  -> Probabilidad de que la prueba sea positiva si se tiene la enfermedad")
    print(f"P(B) = {P_B:.4f}  -> Probabilidad total de que la prueba sea positiva")
    print(f"P(A|B) = {P_A_dado_B:.4f}  -> Probabilidad de tener la enfermedad dado que la prueba salió positiva")

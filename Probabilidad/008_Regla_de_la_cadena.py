# Ejemplo mejorado de uso de la Regla de la Cadena
# Calculamos la probabilidad conjunta P(A, B, C) usando la regla de la cadena.

def calcular_probabilidad_conjunta(P_A, P_B_given_A, P_C_given_A_B):
    """
    Calcula la probabilidad conjunta P(A, B, C) usando la regla de la cadena.
    
    Fórmula: P(A, B, C) = P(A) * P(B|A) * P(C|A,B)
    """
    # Validar que las probabilidades estén en el rango [0, 1]
    if not (0 <= P_A <= 1 and 0 <= P_B_given_A <= 1 and 0 <= P_C_given_A_B <= 1):
        raise ValueError("Todas las probabilidades deben estar en el rango [0, 1].")
    
    # Aplicar la regla de la cadena
    # Paso 1: Multiplicar P(A) por P(B|A)
    P_A_B = P_A * P_B_given_A  # Probabilidad conjunta de A y B
    
    # Paso 2: Multiplicar el resultado anterior por P(C|A,B)
    P_A_B_C = P_A_B * P_C_given_A_B  # Probabilidad conjunta de A, B y C
    
    # Mostrar pasos intermedios
    print(f"P(A) = {P_A}")  # Probabilidad de A
    print(f"P(B|A) = {P_B_given_A}")  # Probabilidad condicional de B dado A
    print(f"P(A, B) = P(A) * P(B|A) = {P_A_B}")  # Probabilidad conjunta de A y B
    print(f"P(C|A,B) = {P_C_given_A_B}")  # Probabilidad condicional de C dado A y B
    print(f"P(A, B, C) = P(A, B) * P(C|A,B) = {P_A_B_C}")  # Probabilidad conjunta final
    
    return P_A_B_C

# Ejemplo de uso
if __name__ == "__main__":
    # Probabilidades dadas
    P_A = 0.6                   # P(A)
    P_B_given_A = 0.7           # P(B | A)
    P_C_given_A_B = 0.9         # P(C | A, B)
    
    # Calcular la probabilidad conjunta
    try:
        P_A_B_C = calcular_probabilidad_conjunta(P_A, P_B_given_A, P_C_given_A_B)
        print("Probabilidad conjunta P(A, B, C):", round(P_A_B_C, 4))
    except ValueError as e:
        print("Error:", e)

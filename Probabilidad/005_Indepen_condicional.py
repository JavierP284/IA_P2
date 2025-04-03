import numpy as np

def probabilidad_conjunta(P_A, P_B_dado_A):
    """
    Calcula la probabilidad conjunta de dos eventos P(A, B).
    
    Args:
        P_A (float): Probabilidad de que ocurra el evento A.
        P_B_dado_A (float): Probabilidad de que ocurra B dado que A ha ocurrido.
    
    Returns:
        float: Probabilidad conjunta P(A, B).
    """
    return P_A * P_B_dado_A

def es_independiente(P_B_dado_A, P_B, tolerancia=0.01):
    """
    Verifica si dos eventos son aproximadamente independientes.
    
    Args:
        P_B_dado_A (float): Probabilidad de B dado A.
        P_B (float): Probabilidad de B.
        tolerancia (float): Margen de error permitido para considerar independencia.
    
    Returns:
        bool: True si son independientes, False en caso contrario.
    """
    return abs(P_B_dado_A - P_B) < tolerancia

def main():
    # Solicitar probabilidades al usuario
    try:
        P_A = float(input("Ingrese la probabilidad de A (P(A)): "))
        P_B = float(input("Ingrese la probabilidad de B (P(B)): "))
        P_B_dado_A = float(input("Ingrese la probabilidad de B dado A (P(B|A)): "))
        tolerancia = float(input("Ingrese la tolerancia para verificar independencia (default 0.01): ") or 0.01)
        
        # Validar que las probabilidades estén en el rango [0, 1]
        if not (0 <= P_A <= 1 and 0 <= P_B <= 1 and 0 <= P_B_dado_A <= 1):
            raise ValueError("Las probabilidades deben estar en el rango [0, 1].")
        
        # Calcular probabilidad conjunta
        P_A_B = probabilidad_conjunta(P_A, P_B_dado_A)
        
        # Verificar independencia
        independiente = es_independiente(P_B_dado_A, P_B, tolerancia)
        
        # Mostrar resultados
        print("\nResultados:")
        print(f"P(A) = {P_A}")
        print(f"P(B) = {P_B}")
        print(f"P(B|A) = {P_B_dado_A}")
        print(f"P(A, B) = {P_A_B}")
        
        if independiente:
            print("Las variables A y B son aproximadamente independientes.")
        else:
            print("Las variables A y B NO son independientes.")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

"""
Ejemplo de Sintaxis y Semántica: Cuantificadores (Universal y Existencial)

Este programa evalúa predicados sobre un conjunto de números utilizando
los cuantificadores universal (∀) y existencial (∃).
"""

# Conjunto de números para trabajar
conjunto = [2, 4, 6, 8, 10]

# Predicado: x es par
def es_par(x):
    """Devuelve True si x es un número par."""
    return x % 2 == 0

# Predicado: x es mayor que 5
def mayor_que_5(x):
    """Devuelve True si x es mayor que 5."""
    return x > 5

# Evaluación del cuantificador universal ∀x P(x)
def cuantificador_universal(S, P):
    """
    Evalúa si todos los elementos de S cumplen el predicado P.
    
    Args:
        S (list): Conjunto de elementos.
        P (function): Predicado a evaluar.
    
    Returns:
        bool: True si todos los elementos cumplen P, False en caso contrario.
    """
    for x in S:
        if not P(x):
            return False  # Encontramos un contraejemplo
    return True  # Todos cumplen

# Evaluación del cuantificador existencial ∃x P(x)
def cuantificador_existencial(S, P):
    """
    Evalúa si al menos un elemento de S cumple el predicado P.
    
    Args:
        S (list): Conjunto de elementos.
        P (function): Predicado a evaluar.
    
    Returns:
        bool: True si al menos un elemento cumple P, False en caso contrario.
    """
    for x in S:
        if P(x):
            return True  # Encontramos al menos uno que cumple
    return False  # Ninguno cumple

# Pruebas de los cuantificadores
if __name__ == "__main__":
    print("Conjunto:", conjunto)

    # ∀x ∈ conjunto, x es par
    print("∀x es par:", cuantificador_universal(conjunto, es_par))  # Esperado: True

    # ∀x ∈ conjunto, x > 5
    print("∀x > 5:", cuantificador_universal(conjunto, mayor_que_5))  # Esperado: False

    # ∃x ∈ conjunto, x > 5
    print("∃x > 5:", cuantificador_existencial(conjunto, mayor_que_5))  # Esperado: True

    # ∃x ∈ conjunto, x < 0
    print("∃x < 0:", cuantificador_existencial(conjunto, lambda x: x < 0))  # Esperado: False

    # Nuevos ejemplos
    # Predicado: x es divisible por 3
    print("∃x divisible por 3:", cuantificador_existencial(conjunto, lambda x: x % 3 == 0))  # Esperado: True

    # Predicado: x es mayor que 0
    print("∀x > 0:", cuantificador_universal(conjunto, lambda x: x > 0))  # Esperado: True

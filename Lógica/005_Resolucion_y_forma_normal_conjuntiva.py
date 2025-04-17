from sympy import symbols
from sympy.logic.boolalg import to_cnf
from sympy.logic.inference import satisfiable

def declarar_simbolos():
    """
    Declara los símbolos proposicionales utilizados en el algoritmo.
    En este caso, se declaran tres símbolos: P, Q y R.
    """
    return symbols('P Q R')

def definir_premisas_y_conclusion(P, Q, R):
    """
    Define las premisas y la conclusión utilizando equivalencias lógicas.
    Las premisas y la conclusión se expresan en términos de lógica proposicional:
    - Premisa 1: P → Q, que es equivalente a ¬P ∨ Q
    - Premisa 2: Q → R, que es equivalente a ¬Q ∨ R
    - Conclusión: P → R, que es equivalente a ¬P ∨ R
    Retorna las premisas y la conclusión en forma simbólica.
    """
    premisa1 = ~P | Q   # P → Q es equivalente a ¬P ∨ Q
    premisa2 = ~Q | R   # Q → R es equivalente a ¬Q ∨ R
    conclusion = ~P | R  # P → R es equivalente a ¬P ∨ R
    return premisa1, premisa2, conclusion

def imprimir_fnc(premisa1, premisa2, conclusion):
    """
    Convierte las premisas y la conclusión a Forma Normal Conjuntiva (FNC).
    La FNC es una forma estándar utilizada en lógica proposicional para facilitar
    la resolución lógica. Además, imprime las premisas y la conclusión en FNC.
    """
    print("Forma Normal Conjuntiva (FNC):")
    # Convertir cada premisa y la conclusión a FNC
    cnf_p1 = to_cnf(premisa1, simplify=True)
    cnf_p2 = to_cnf(premisa2, simplify=True)
    cnf_conclusion = to_cnf(conclusion, simplify=True)
    # Imprimir los resultados
    print(f"Premisa 1 (P → Q): {cnf_p1}")
    print(f"Premisa 2 (Q → R): {cnf_p2}")
    print(f"Conclusión (P → R): {cnf_conclusion}")
    return cnf_p1, cnf_p2, cnf_conclusion

def aplicar_resolucion(cnf_p1, cnf_p2, conclusion):
    """
    Aplica el algoritmo de resolución lógica para determinar si la conclusión
    se deduce lógicamente de las premisas.
    Pasos:
    1. Se niega la conclusión (¬(P → R)).
    2. Se combina la negación de la conclusión con las premisas en FNC.
    3. Se verifica si el conjunto total es satisfacible.
    Retorna:
    - Un modelo si el conjunto es satisfacible (la conclusión no se deduce).
    - None si el conjunto no es satisfacible (la conclusión se deduce).
    """
    # Negar la conclusión y convertirla a FNC
    neg_conclusion = to_cnf(~conclusion, simplify=True)
    print(f"\nNegación de la conclusión (¬(P → R)): {neg_conclusion}")
    
    # Combinar las premisas y la negación de la conclusión
    conjunto_total = cnf_p1 & cnf_p2 & neg_conclusion
    # Verificar si el conjunto es satisfacible
    modelo = satisfiable(conjunto_total)
    return modelo

def interpretar_resultado(modelo):
    """
    Interpreta y muestra el resultado del algoritmo de resolución lógica.
    Si el modelo es None, significa que la conclusión se deduce lógicamente
    de las premisas. De lo contrario, se muestra un modelo que contradice
    la deducción.
    """
    if not modelo:
        print("La conclusión se deduce lógicamente de las premisas (Resolución exitosa)")
    else:
        print("La conclusión NO se deduce lógicamente de las premisas (Hay al menos un modelo que contradice)")
        print(f"Modelo encontrado: {modelo}")

def main():
    """
    Función principal que ejecuta el algoritmo de resolución lógica paso a paso:
    1. Declarar los símbolos proposicionales.
    2. Definir las premisas y la conclusión.
    3. Convertir las premisas y la conclusión a Forma Normal Conjuntiva (FNC).
    4. Aplicar el algoritmo de resolución lógica.
    5. Interpretar y mostrar el resultado.
    """
    # Paso 1: Declarar símbolos
    P, Q, R = declarar_simbolos()

    # Paso 2: Definir premisas y conclusión
    premisa1, premisa2, conclusion = definir_premisas_y_conclusion(P, Q, R)

    # Paso 3: Convertir a Forma Normal Conjuntiva (FNC)
    cnf_p1, cnf_p2, cnf_conclusion = imprimir_fnc(premisa1, premisa2, conclusion)

    # Paso 4: Aplicar resolución lógica
    print("\nEvaluando resolución lógica...")
    modelo = aplicar_resolucion(cnf_p1, cnf_p2, conclusion)

    # Paso 5: Interpretar el resultado
    interpretar_resultado(modelo)

# Punto de entrada del programa
if __name__ == "__main__":
    main()

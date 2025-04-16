from itertools import product

# Definimos las variables booleanas involucradas
variables = ['A', 'B', 'C']

# Generamos todas las combinaciones posibles de valores True/False para las variables
# itertools.product genera todas las combinaciones posibles
combinaciones = list(product([False, True], repeat=len(variables)))

# Listado de expresiones lógicas comunes para referencia:
# 1. Operadores básicos:
#    - A and B       → AND lógico entre A y B
#    - A or B        → OR lógico entre A y B
#    - not A         → Negación lógica de A
# 2. Expresiones combinadas:
#    - (A and B) or C       → AND entre A y B, luego OR con C
#    - (A or B) and not C   → OR entre A y B, luego AND con la negación de C
#    - A and (B or C)       → AND entre A y el resultado de B OR C
# 3. Expresiones con implicación:
#    - not A or B           → Representa A → B (implicación lógica)
#    - not (A and B) or C   → Representa (A ∧ B) → C
# 4. Expresiones con equivalencia:
#    - (A and B) == C       → Equivalencia lógica entre (A ∧ B) y C
#    - A == (B or C)        → Equivalencia lógica entre A y (B ∨ C)
# 5. Expresiones más complejas:
#    - (A or not B) and (B or C)       → Combinación de OR y AND con negación
#    - (A and B) or (not A and not B)  → Representa una equivalencia lógica (A ↔ B)
#    - (A or B) and not (A and B)      → Representa una disyunción exclusiva (A ⊕ B)

# Solicitamos al usuario que ingrese la expresión lógica a evaluar
# Ejemplo: "(A and B) or not C"
print("Ingrese la expresión lógica a evaluar (use las variables A, B, C):")
expresion = input("Expresión lógica: ")

# Imprimimos el encabezado de la tabla
print(f"\n{'A':^5} {'B':^5} {'C':^5} | {'Resultado':^10}")
print("-" * 30)

# Evaluamos la expresión para cada combinación de valores
for valores in combinaciones:
    # Asignamos los valores a las variables
    contexto = dict(zip(variables, valores))  # {'A': False, 'B': True, 'C': False}

    # Evaluamos la expresión lógica usando eval() con el contexto de variables
    try:
        resultado = eval(expresion, {}, contexto)
    except Exception as e:
        print(f"Error al evaluar la expresión: {e}")
        break

    # Imprimimos la fila de la tabla
    print(f"{contexto['A']!s:^5} {contexto['B']!s:^5} {contexto['C']!s:^5} | {resultado!s:^10}")

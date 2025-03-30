def forward_checking(variables, domains, constraints, assignment):
    """
    Implementación del algoritmo de verificación hacia adelante (forward checking).
    
    Parámetros:
    - variables: Lista de variables del problema.
    - domains: Diccionario que asocia cada variable con su dominio de valores posibles.
    - constraints: Función que verifica si una asignación cumple con las restricciones.
    - assignment: Diccionario que contiene la asignación actual de variables.

    Retorna:
    - Una asignación completa si se encuentra una solución, o None si no hay solución.
    """
    # Si todas las variables están asignadas, devolvemos la asignación actual
    if len(assignment) == len(variables):
        return assignment

    # Seleccionamos una variable no asignada
    unassigned = [v for v in variables if v not in assignment]
    variable = unassigned[0]

    # Iteramos sobre los valores posibles en el dominio de la variable
    for value in domains[variable]:
        # Creamos una copia de la asignación actual
        local_assignment = assignment.copy()
        local_assignment[variable] = value

        # Verificamos si la asignación cumple con las restricciones
        if constraints(local_assignment):
            # Realizamos la verificación hacia adelante
            local_domains = forward_check_domains(variable, value, domains, constraints, local_assignment)

            # Si no hay dominios vacíos, continuamos con la búsqueda recursiva
            if local_domains is not None:
                result = forward_checking(variables, local_domains, constraints, local_assignment)
                if result is not None:
                    return result

    # Si no se encuentra solución, devolvemos None
    return None


def forward_check_domains(variable, value, domains, constraints, assignment):
    """
    Realiza la verificación hacia adelante actualizando los dominios de las variables no asignadas.
    
    Parámetros:
    - variable: La variable que acaba de ser asignada.
    - value: El valor asignado a la variable.
    - domains: Diccionario con los dominios actuales de las variables.
    - constraints: Función que verifica las restricciones.
    - assignment: Diccionario con la asignación actual.

    Retorna:
    - Un nuevo diccionario de dominios si no hay conflictos, o None si algún dominio queda vacío.
    """
    # Creamos una copia de los dominios actuales
    new_domains = {var: list(domains[var]) for var in domains}

    # Iteramos sobre las variables no asignadas
    for var in domains:
        if var not in assignment:
            # Filtramos los valores del dominio que no cumplen con las restricciones
            new_domains[var] = [v for v in new_domains[var] if constraints({**assignment, var: v})]

            # Si algún dominio queda vacío, devolvemos None
            if not new_domains[var]:
                return None

    return new_domains


# Ejemplo de uso: Problema de coloreado de grafos
if __name__ == "__main__":
    # Variables del problema: Nodos del grafo
    variables = ["A", "B", "C", "D", "E"]

    # Dominios de las variables: Colores disponibles
    domains = {
        "A": ["Rojo", "Verde", "Azul"],
        "B": ["Rojo", "Verde", "Azul"],
        "C": ["Rojo", "Verde", "Azul"],
        "D": ["Rojo", "Verde", "Azul"],
        "E": ["Rojo", "Verde", "Azul"]
    }

    # Restricciones: Los nodos adyacentes no pueden tener el mismo color
    neighbors = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D", "E"],
        "D": ["B", "C", "E"],
        "E": ["C", "D"]
    }

    def constraints(assignment):
        """
        Verifica que los nodos adyacentes no tengan el mismo color.
        """
        for variable, value in assignment.items():
            for neighbor in neighbors.get(variable, []):
                if neighbor in assignment and assignment[neighbor] == value:
                    return False
        return True

    # Llamada al algoritmo de verificación hacia adelante
    solution = forward_checking(variables, domains, constraints, {})

    # Imprimimos la solución encontrada
    print("Solución:", solution)
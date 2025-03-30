from collections import deque

def ac3(variables, dominios, restricciones):
    """
    Algoritmo AC-3 para la Propagación de Restricciones en un CSP (Problema de Satisfacción de Restricciones).
    Reduce los dominios eliminando valores inconsistentes entre variables conectadas.
    """
    # Inicializamos la cola con todas las restricciones (arcos)
    cola = deque([(xi, xj) for xi in restricciones for xj in restricciones[xi]])
    
    while cola:
        xi, xj = cola.popleft()  # Extraemos un par de variables con restricciones
        if revisar_arco(xi, xj, dominios):  # Si se modificó el dominio de xi
            if not dominios[xi]:  # Si el dominio queda vacío, no hay solución
                return False
            # Agregamos los vecinos de xi para revisión, excepto xj
            for xk in restricciones[xi]:
                if xk != xj:
                    cola.append((xk, xi))
    return True  # Si terminamos sin vaciar dominios, el problema es consistente


def revisar_arco(xi, xj, dominios):
    """
    Revisa y filtra el dominio de xi eliminando valores inconsistentes respecto a xj.
    Devuelve True si se eliminaron valores.
    """
    dominio_filtrado = []
    for valor_xi in dominios[xi]:
        # xi debe ser diferente de xj para que sea consistente
        if any(valor_xi != valor_xj for valor_xj in dominios[xj]):
            dominio_filtrado.append(valor_xi)
    
    # Si el dominio de xi cambia, actualizamos y devolvemos True
    if len(dominio_filtrado) < len(dominios[xi]):
        dominios[xi] = dominio_filtrado
        return True
    return False


# Definimos el problema de coloreo de mapas con 4 regiones y 3 colores
variables = ['A', 'B', 'C', 'D']
dominios = {
    'A': ['rojo', 'azul'],
    'B': ['rojo'],
    'C': ['rojo', 'azul', 'verde'],
    'D': ['rojo', 'azul', 'verde']
}
restricciones = {
    'A': ['B', 'C'],  # A debe ser diferente de B y C
    'B': ['A', 'C', 'D'],  # B debe ser diferente de A, C y D
    'C': ['A', 'B', 'D'],  # C debe ser diferente de A, B y D
    'D': ['B', 'C']   # D debe ser diferente de B y C
}

# Ejecutamos el código
if ac3(variables, dominios, restricciones):
    print("Dominios reducidos tras AC-3:", dominios)
else:
    print("No hay solución posible después de AC-3.")

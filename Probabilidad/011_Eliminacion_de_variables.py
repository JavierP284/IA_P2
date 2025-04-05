from collections import defaultdict
import itertools

# Dominios de las variables (valores posibles: True o False)
# Cada variable puede tomar uno de estos valores.
dominios = {
    "Nublado": [True, False],
    "Rociador": [True, False],
    "Lluvia": [True, False],
    "PastoMojado": [True, False]
}

# Tablas de Probabilidad Condicional (CPTs) para cada nodo
# Estas tablas definen las probabilidades condicionales de cada variable
# dado el estado de sus padres en la red bayesiana.
CPT = {
    "Nublado": {
        (): {True: 0.5, False: 0.5}  # Probabilidad marginal de "Nublado"
    },
    "Rociador": {
        (True,): {True: 0.1, False: 0.9},  # Probabilidad condicional dado "Nublado=True"
        (False,): {True: 0.5, False: 0.5}  # Probabilidad condicional dado "Nublado=False"
    },
    "Lluvia": {
        (True,): {True: 0.8, False: 0.2},  # Probabilidad condicional dado "Nublado=True"
        (False,): {True: 0.2, False: 0.8}  # Probabilidad condicional dado "Nublado=False"
    },
    "PastoMojado": {
        # Probabilidad condicional dado "Rociador" y "Lluvia"
        (True, True): {True: 0.99, False: 0.01},
        (True, False): {True: 0.90, False: 0.10},
        (False, True): {True: 0.90, False: 0.10},
        (False, False): {True: 0.0, False: 1.0}
    }
}

# Padres de cada nodo en la red
# Esto define la estructura de la red bayesiana.
padres = {
    "Nublado": [],  # "Nublado" no tiene padres
    "Rociador": ["Nublado"],  # "Rociador" depende de "Nublado"
    "Lluvia": ["Nublado"],  # "Lluvia" depende de "Nublado"
    "PastoMojado": ["Rociador", "Lluvia"]  # "PastoMojado" depende de "Rociador" y "Lluvia"
}

def obtener_probabilidad(variable, valor, evidencia):
    """
    Obtiene la probabilidad de una variable dado su valor y la evidencia conocida.
    - variable: Nombre de la variable.
    - valor: Valor de la variable (True o False).
    - evidencia: Diccionario con las variables observadas y sus valores.
    """
    # Obtiene los valores de los padres de la variable según la evidencia.
    par = tuple(evidencia[p] for p in padres[variable])
    # Retorna la probabilidad correspondiente desde la CPT.
    return CPT[variable][par][valor]

def crear_factor(variable, evidencia):
    """
    Crea un factor de probabilidad para una variable dada la evidencia actual.
    - variable: Nombre de la variable.
    - evidencia: Diccionario con las variables observadas y sus valores.
    """
    # Variables involucradas en el factor: la variable actual y sus padres no observados.
    variables_factor = [variable] + [p for p in padres[variable] if p not in evidencia]
    # Genera todas las combinaciones posibles de valores para estas variables.
    combinaciones = list(itertools.product(*[dominios[v] for v in variables_factor]))

    factor = []
    for fila in combinaciones:
        # Crea una copia de la evidencia actual para trabajar con ella.
        evidencia_local = evidencia.copy()
        # Asigna los valores de la combinación actual a las variables.
        for i, v in enumerate(variables_factor):
            evidencia_local[v] = fila[i]

        # Calcula la probabilidad de la variable actual dado la evidencia local.
        prob = obtener_probabilidad(variable, fila[0], evidencia_local)
        # Agrega la asignación y su probabilidad al factor.
        factor.append((dict(zip(variables_factor, fila)), prob))

    return factor

def multiplicar_factores(factores):
    """
    Multiplica todos los factores de una lista.
    - factores: Lista de factores a multiplicar.
    """
    # Inicializa el resultado con el primer factor.
    resultado = factores[0]
    # Multiplica los factores uno por uno.
    for f in factores[1:]:
        resultado = multiplicar_dos_factores(resultado, f)
    return resultado

def multiplicar_dos_factores(f1, f2):
    """
    Multiplica dos factores en uno solo.
    - f1, f2: Factores a multiplicar.
    """
    # Obtiene las variables involucradas en ambos factores.
    vars1 = list(f1[0][0].keys())
    vars2 = list(f2[0][0].keys())
    todas_vars = list(set(vars1 + vars2))  # Unión de las variables.

    nuevo_factor = []
    # Itera sobre todas las combinaciones posibles de valores para las variables.
    for valores in itertools.product(*[dominios[v] for v in todas_vars]):
        asignacion = dict(zip(todas_vars, valores))

        # Busca las probabilidades correspondientes en ambos factores.
        match1 = [p for a, p in f1 if all(asignacion[k] == a[k] for k in a)]
        match2 = [p for a, p in f2 if all(asignacion[k] == a[k] for k in a)]

        # Si ambas asignaciones existen, multiplica las probabilidades.
        if match1 and match2:
            nuevo_factor.append((asignacion, match1[0] * match2[0]))

    return nuevo_factor

def eliminar_variable(factor, variable):
    """
    Elimina una variable sumando sobre todos sus valores posibles.
    - factor: Factor del que se eliminará la variable.
    - variable: Variable a eliminar.
    """
    nuevo_factor = defaultdict(float)
    # Itera sobre cada asignación en el factor.
    for asignacion, prob in factor:
        # Crea una clave sin la variable a eliminar.
        clave = tuple((k, v) for k, v in asignacion.items() if k != variable)
        # Suma las probabilidades para las asignaciones equivalentes.
        nuevo_factor[clave] += prob

    # Convierte el resultado en una lista de asignaciones y probabilidades.
    resultado = []
    for k, v in nuevo_factor.items():
        resultado.append((dict(k), v))

    return resultado

def normalizar(factor, variable_consulta):
    """
    Normaliza el resultado para que la suma sea 1 (probabilidad total).
    - factor: Factor a normalizar.
    - variable_consulta: Variable de consulta.
    """
    # Calcula la suma total de las probabilidades.
    total = sum(prob for _, prob in factor)
    resultado = {}
    # Divide cada probabilidad entre el total para normalizar.
    for asignacion, prob in factor:
        resultado[asignacion[variable_consulta]] = prob / total
    return resultado

def eliminacion_de_variables(variable_consulta, evidencia):
    """
    Algoritmo principal de Eliminación de Variables.
    - variable_consulta: Variable sobre la que se quiere inferir.
    - evidencia: Diccionario con las variables observadas y sus valores.
    """
    # Identifica las variables ocultas (no consulta ni evidencia).
    variables_ocultas = [v for v in dominios if v != variable_consulta and v not in evidencia]

    # Crea factores iniciales para cada nodo en la red.
    factores = [crear_factor(variable, evidencia) for variable in dominios]

    # Elimina cada variable oculta una por una.
    for variable in variables_ocultas:
        # Factores que contienen la variable a eliminar.
        factores_con_variable = [f for f in factores if any(variable in a for a, _ in f)]
        # Factores que no contienen la variable.
        otros_factores = [f for f in factores if f not in factores_con_variable]

        # Multiplica los factores que contienen la variable.
        producto = multiplicar_factores(factores_con_variable)
        # Elimina la variable del producto.
        suma = eliminar_variable(producto, variable)

        # Actualiza la lista de factores.
        factores = otros_factores + [suma]

    # Multiplica los factores finales y normaliza.
    factor_final = multiplicar_factores(factores)
    return normalizar(factor_final, variable_consulta)

# --------------------------
# EJEMPLO DE CONSULTA
# --------------------------
if __name__ == "__main__":
    # Consulta: P(Lluvia | PastoMojado=True)
    resultado = eliminacion_de_variables("Lluvia", {"PastoMojado": True})
    print("P(Lluvia | PastoMojado=True):")
    for valor, prob in resultado.items():
        print(f"  {valor}: {prob:.4f}")

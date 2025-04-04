from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definir la estructura de la red bayesiana
# En este caso, "Lluvia" y "Riego" son causas que afectan al estado de "Césped Mojado".
modelo = DiscreteBayesianNetwork([("Lluvia", "Césped Mojado"), ("Riego", "Césped Mojado")])

# Definir las distribuciones de probabilidad para cada nodo
# Nodo "Lluvia": Probabilidad de que llueva o no llueva
cpd_lluvia = TabularCPD(
    variable="Lluvia",  # Nombre del nodo
    variable_card=2,  # Número de estados posibles (Sí, No)
    values=[[0.2], [0.8]],  # Probabilidades: 20% de que llueva, 80% de que no llueva
    state_names={"Lluvia": ["Sí", "No"]}  # Nombres de los estados
)

# Nodo "Riego": Probabilidad de que se riegue el césped o no
cpd_riego = TabularCPD(
    variable="Riego",  # Nombre del nodo
    variable_card=2,  # Número de estados posibles (Sí, No)
    values=[[0.5], [0.5]],  # Probabilidades: 50% de que se riegue, 50% de que no
    state_names={"Riego": ["Sí", "No"]}  # Nombres de los estados
)

# Nodo "Césped Mojado": Probabilidad condicional de que el césped esté mojado
# dado los estados de "Lluvia" y "Riego".
cpd_cesped_mojado = TabularCPD(
    variable="Césped Mojado",  # Nombre del nodo
    variable_card=2,  # Número de estados posibles (Sí, No)
    values=[
        [0.99, 0.8, 0.9, 0.0],  # Probabilidad de que el césped esté mojado (Sí)
        [0.01, 0.2, 0.1, 1.0],  # Probabilidad de que el césped no esté mojado (No)
    ],
    evidence=["Lluvia", "Riego"],  # Nodos padres que afectan a este nodo
    evidence_card=[2, 2],  # Número de estados posibles para cada nodo padre
    state_names={
        "Césped Mojado": ["Sí", "No"],
        "Lluvia": ["Sí", "No"],
        "Riego": ["Sí", "No"],
    },
)

# Añadir las distribuciones de probabilidad condicional (CPDs) al modelo
modelo.add_cpds(cpd_lluvia, cpd_riego, cpd_cesped_mojado)

# Validar el modelo para asegurarse de que las CPDs son consistentes
if not modelo.check_model():
    raise ValueError("El modelo no es válido. Verifica las CPDs.")

# Realizar inferencia en la red bayesiana
# Usamos VariableElimination para calcular probabilidades condicionales
inferencia = VariableElimination(modelo)

# Calcular la probabilidad de que haya llovido dado que el césped está mojado
resultado = inferencia.query(
    variables=["Lluvia"],  # Variable de interés
    evidence={"Césped Mojado": "Sí"}  # Evidencia observada
)

# Mostrar los resultados de la inferencia
print("Probabilidad de que haya llovido dado que el césped está mojado:")
print(resultado)

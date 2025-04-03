from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definir la estructura de la red bayesiana
modelo = BayesianNetwork([("Lluvia", "Césped Mojado"), ("Riego", "Césped Mojado")])

# Definir las distribuciones de probabilidad para cada nodo
cpd_lluvia = TabularCPD(variable="Lluvia", variable_card=2, values=[[0.2], [0.8]], state_names={"Lluvia": ["Sí", "No"]})
cpd_riego = TabularCPD(variable="Riego", variable_card=2, values=[[0.5], [0.5]], state_names={"Riego": ["Sí", "No"]})

# Definir la distribución condicional de "Césped Mojado" dado "Lluvia" y "Riego"
cpd_cesped_mojado = TabularCPD(
    variable="Césped Mojado",
    variable_card=2,
    values=[
        [0.99, 0.8, 0.9, 0.0],  # Probabilidad de "Sí"
        [0.01, 0.2, 0.1, 1.0],  # Probabilidad de "No"
    ],
    evidence=["Lluvia", "Riego"],
    evidence_card=[2, 2],
    state_names={
        "Césped Mojado": ["Sí", "No"],
        "Lluvia": ["Sí", "No"],
        "Riego": ["Sí", "No"],
    },
)

# Añadir las CPDs al modelo
modelo.add_cpds(cpd_lluvia, cpd_riego, cpd_cesped_mojado)

# Validar el modelo
if not modelo.check_model():
    raise ValueError("El modelo no es válido. Verifica las CPDs.")

# Inferencia: calcular la probabilidad de que haya llovido si el césped está mojado
inferencia = VariableElimination(modelo)
resultado = inferencia.query(variables=["Lluvia"], evidence={"Césped Mojado": "Sí"})

# Mostrar resultados
print("Probabilidad de que haya llovido dado que el césped está mojado:")
print(resultado)

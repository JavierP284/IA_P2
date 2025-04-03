# Importamos las librerías necesarias
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

def crear_modelo():
    """Crea y devuelve un modelo bayesiano con sus CPDs asociadas."""
    # Creamos la estructura de la Red Bayesiana
    modelo = BayesianModel([("Lluvia", "Tráfico"), ("Lluvia", "Retraso"), ("Tráfico", "Retraso")])

    # Definimos las Tablas de Probabilidad Condicionada (CPDs)
    cpd_lluvia = TabularCPD(variable="Lluvia", variable_card=2, values=[[0.7], [0.3]])  # P(Lluvia)
    cpd_trafico = TabularCPD(variable="Tráfico", variable_card=2,
                             values=[[0.8, 0.3], [0.2, 0.7]],  # P(Tráfico | Lluvia)
                             evidence=["Lluvia"], evidence_card=[2])
    cpd_retraso = TabularCPD(variable="Retraso", variable_card=2,
                             values=[[0.9, 0.6, 0.5, 0.1], [0.1, 0.4, 0.5, 0.9]],  # P(Retraso | Lluvia, Tráfico)
                             evidence=["Lluvia", "Tráfico"], evidence_card=[2, 2])

    # Asociamos las CPDs al modelo
    modelo.add_cpds(cpd_lluvia, cpd_trafico, cpd_retraso)

    # Verificamos si la red está bien definida
    if modelo.check_model():
        print("El modelo es válido.")
    else:
        raise ValueError("El modelo no es válido. Verifica las CPDs.")

    return modelo

def realizar_inferencia(modelo, evidencia):
    """Realiza inferencia sobre el modelo dado una evidencia."""
    inferencia = VariableElimination(modelo)
    resultado = inferencia.query(variables=["Retraso"], evidence=evidencia)
    return resultado

if __name__ == "__main__":
    try:
        # Crear el modelo bayesiano
        modelo = crear_modelo()

        # Realizar inferencia con evidencia
        evidencia = {"Tráfico": 1}  # 1 significa que hay tráfico
        resultado = realizar_inferencia(modelo, evidencia)

        # Mostrar resultados
        print("Probabilidad de retraso dada la evidencia:")
        print(resultado)
    except Exception as e:
        print(f"Error: {e}")

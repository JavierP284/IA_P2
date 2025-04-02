import numpy as np

# Definimos la probabilidad a priori de que un paciente tenga una enfermedad
p_enfermedad = 0.01  # 1% de los pacientes tienen la enfermedad

# Probabilidad de que la prueba dé positiva si el paciente tiene la enfermedad (sensibilidad)
p_positivo_dado_enfermedad = 0.95  

# Probabilidad de que la prueba dé positiva si el paciente NO tiene la enfermedad (falso positivo)
p_positivo_dado_no_enfermedad = 0.05  

# Probabilidad total de obtener un resultado positivo en la prueba (regla de la probabilidad total)
p_positivo = (p_enfermedad * p_positivo_dado_enfermedad) + \
             ((1 - p_enfermedad) * p_positivo_dado_no_enfermedad)

# Aplicamos el Teorema de Bayes para actualizar la probabilidad
p_enfermedad_dado_positivo = (p_enfermedad * p_positivo_dado_enfermedad) / p_positivo

# Mostramos los resultados
print(f"Probabilidad a priori de enfermedad: {p_enfermedad:.4f}")
print(f"Probabilidad de dar positivo en la prueba: {p_positivo:.4f}")
print(f"Probabilidad de tener la enfermedad dado un resultado positivo: {p_enfermedad_dado_positivo:.4f}")

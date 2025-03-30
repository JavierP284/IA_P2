import numpy as np

# Definir una función de utilidad basada en riesgo y rentabilidad esperada
def funcion_utilidad(rentabilidad, riesgo, aversion_riesgo=2):
    """
    Calcula la utilidad de una inversión en función de su rentabilidad y riesgo.

    Parámetros:
    - rentabilidad: beneficio esperado de la inversión (en porcentaje).
    - riesgo: incertidumbre o volatilidad de la inversión (valor entre 0 y 1).
    - aversion_riesgo: factor que mide qué tan adverso al riesgo es el inversor (mayor = más aversión).

    Retorna:
    - Un valor de utilidad (mayor valor = mejor inversión).
    """
    utilidad = rentabilidad - (aversion_riesgo * riesgo * 100)  # Penaliza el riesgo
    return utilidad

# Lista de opciones de inversión con rentabilidad (%) y riesgo (escala 0-1)
opciones_inversion = [
    {"nombre": "Bonos del Gobierno", "rentabilidad": 5, "riesgo": 0.1},
    {"nombre": "Acciones Tecnológicas", "rentabilidad": 12, "riesgo": 0.6},
    {"nombre": "Bienes Raíces", "rentabilidad": 8, "riesgo": 0.3},
    {"nombre": "Criptomonedas", "rentabilidad": 20, "riesgo": 0.9}
]

# Factor de aversión al riesgo del inversor (ajustable)
aversion_riesgo = 2

# Evaluar la utilidad de cada inversión
for inversion in opciones_inversion:
    inversion["utilidad"] = funcion_utilidad(inversion["rentabilidad"], inversion["riesgo"], aversion_riesgo)

# Seleccionar la mejor inversión basada en la mayor utilidad
mejor_inversion = max(opciones_inversion, key=lambda x: x["utilidad"])

# Mostrar resultados
print("Opciones de inversión y sus utilidades:")
for inversion in opciones_inversion:
    print(f"{inversion['nombre']}: Rentabilidad = {inversion['rentabilidad']}%, Riesgo = {inversion['riesgo']}, Utilidad = {inversion['utilidad']}")

print("\nMejor inversión recomendada:", mejor_inversion["nombre"])

# Probabilidades de la demanda en el mercado
probabilidades = {
    "Alta demanda": 0.7,  # 70% de probabilidad
    "Baja demanda": 0.3   # 30% de probabilidad
}

# Utilidades sin hacer estudio de mercado
utilidades_sin_info = {
    "Lanzar": {
        "Alta demanda": 100000,  # Ganancia si hay alta demanda
        "Baja demanda": -50000   # Pérdida si hay baja demanda
    },
    "No lanzar": {
        "Alta demanda": 0,
        "Baja demanda": 0  # No hay ganancia ni pérdida
    }
}

# Calcular la utilidad esperada sin información
def utilidad_esperada_sin_info():
    utilidad_total = 0
    for estado, prob in probabilidades.items():
        utilidad_total += prob * utilidades_sin_info["Lanzar"][estado]
    return utilidad_total

# Probabilidades del estudio de mercado (su precisión)
precision_estudio = {
    "Alta demanda predicha": {"Alta demanda": 0.9, "Baja demanda": 0.1},
    "Baja demanda predicha": {"Alta demanda": 0.2, "Baja demanda": 0.8}
}

# Validar que las probabilidades del estudio sumen 1
for prediccion, probabilidades_reales in precision_estudio.items():
    if not abs(sum(probabilidades_reales.values()) - 1) < 1e-6:
        raise ValueError(f"Las probabilidades para '{prediccion}' no suman 1.")

# Costo del estudio de mercado
costo_estudio = 5000  

# Calcular la utilidad esperada con información del estudio de mercado
def utilidad_esperada_con_info():
    utilidad_con_info = 0
    for resultado, probabilidades_reales in precision_estudio.items():
        # Probabilidad de que el estudio prediga este resultado
        prob_predicho = sum(probabilidades[estado] * prob for estado, prob in probabilidades_reales.items())

        if "Alta demanda" in resultado:
            # Si el estudio predice alta demanda, se lanza el producto
            utilidad = sum(probabilidades_reales[estado] * utilidades_sin_info["Lanzar"][estado] for estado in probabilidades_reales)
        else:
            # Si el estudio predice baja demanda, no se lanza el producto
            utilidad = 0  

        # Acumular la utilidad ponderada por la probabilidad del resultado predicho
        utilidad_con_info += prob_predicho * utilidad

    # Restar el costo del estudio
    return utilidad_con_info - costo_estudio

# Calcular el Valor de la Información (VOI)
voi = utilidad_esperada_con_info() - utilidad_esperada_sin_info()

# Mostrar los resultados
print(f"Utilidad esperada SIN información: ${utilidad_esperada_sin_info():,.2f}")
print(f"Utilidad esperada CON información: ${utilidad_esperada_con_info():,.2f}")
print(f"Valor de la Información (VOI): ${voi:,.2f}")

# Decisión final
if voi > 0:
    print("\nSe recomienda hacer el estudio de mercado.")
else:
    print("\nNo vale la pena pagar por el estudio.")

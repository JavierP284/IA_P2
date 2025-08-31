# ===============================================================
# Calculadora de costo de impresión 3D con IA (regresión lineal)
# ===============================================================
# Este programa estima el costo de impresión 3D en pesos mexicanos (MXN)
# considerando el tipo de filamento, el tiempo de impresión, la cantidad
# de material usado y el margen de ganancia deseado. Utiliza un modelo
# de regresión lineal entrenado con ejemplos históricos para predecir
# el costo base según el tipo de filamento y el tiempo de impresión.
# Luego suma el costo del material y aplica el margen de ganancia.
# ===============================================================

import numpy as np
from sklearn.linear_model import LinearRegression

# Datos de entrenamiento para el modelo de IA.
# Cada fila representa un ejemplo: [tipo_filamento, tiempo_horas]
# tipo_filamento: 0 = PLA, 1 = PETG
# tiempo_horas: duración estimada de la impresión
X = np.array([
    [0, 2],  # PLA, 2 horas
    [0, 4],  # PLA, 4 horas
    [1, 3],  # PETG, 3 horas
    [1, 5]   # PETG, 5 horas
])
# Costos base en MXN para cada ejemplo anterior
# Estos valores sirven como referencia histórica
y = np.array([50, 100, 120, 180])

# Se crea y entrena el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X, y)

# Diccionario con el precio por kilogramo de cada tipo de filamento
# 0 = PLA (300 MXN/kg), 1 = PETG (400 MXN/kg)
precio_filamento = {0: 300, 1: 400}

# Función que calcula el costo total de la impresión 3D
# tipo_filamento: 0=PLA, 1=PETG
# tiempo: horas de impresión
# gramos_material: cantidad de filamento en gramos
# margen_ganancia: porcentaje de ganancia (ej. 0.2 = 20%)
def calcular_costo(tipo_filamento, tiempo, gramos_material, margen_ganancia=0.2):
    # Validación de entradas para evitar errores
    if tipo_filamento not in precio_filamento:
        raise ValueError("Tipo de filamento no válido. Debe ser 0 (PLA) o 1 (PETG).")
    if tiempo <= 0 or gramos_material <= 0:
        raise ValueError("El tiempo y la cantidad de material deben ser mayores a 0.")
    # Predicción del costo base usando el modelo de IA
    costo_base = modelo.predict(np.array([[tipo_filamento, tiempo]]))[0]
    # Cálculo del costo del filamento usado (precio por gramo)
    costo_filamento_total = (precio_filamento[tipo_filamento] / 1000) * gramos_material
    # Suma del costo base y el material
    costo_total = costo_base + costo_filamento_total
    # Aplicación del margen de ganancia
    precio_final = costo_total * (1 + margen_ganancia)
    # Desglose de los costos para el usuario
    print(f"\n=== Desglose del costo ===")
    print(f"Costo base (IA): ${costo_base:.2f} MXN")
    print(f"Filamento ({gramos_material} g): ${costo_filamento_total:.2f} MXN")
    print(f"Total con margen ({margen_ganancia*100:.0f}%): ${precio_final:.2f} MXN")
    return round(precio_final, 2)

# Interfaz de usuario por consola
# Permite calcular varios costos hasta que el usuario escriba 'q'
print("=== Calculadora de costo de impresión 3D (MXN) ===")
print("Tipos de filamento: 0 = PLA, 1 = PETG")
while True:
    entrada = input("Ingrese el tipo de filamento (0 o 1, o 'q' para salir): ")
    if entrada.lower() == 'q':
        print("Saliendo de la calculadora. ¡Hasta luego!")
        break
    try:
        # Solicita los datos necesarios al usuario
        tipo_filamento = int(entrada)
        tiempo = float(input("Ingrese el tiempo estimado de impresión en horas: "))
        gramos_material = float(input("Ingrese la cantidad de material a usar en gramos: "))
        margen = float(input("Ingrese el margen de ganancia deseado (ej: 0.2 = 20%): "))
        # Calcula y muestra el costo estimado
        costo_estimado = calcular_costo(tipo_filamento, tiempo, gramos_material, margen)
        print(f"\nCosto estimado de impresión: ${costo_estimado} MXN\n")
    except ValueError as e:
        print(f"Error: {e}\nPor favor, ingrese valores válidos.\n")

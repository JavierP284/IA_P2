# -------------------------------------------------------------
# Algoritmo de Explicaciones e Información Relevante
# -------------------------------------------------------------

# Constantes para umbrales
# Estos valores definen los límites para clasificar ingresos y deudas
UMBRAL_INGRESOS_BUENOS = 5000  # Ingresos considerados buenos
UMBRAL_INGRESOS_ALTOS = 7000   # Ingresos considerados altos
UMBRAL_DEUDA_ELEVADA = 8000    # Deuda considerada elevada
UMBRAL_DEUDA_BAJA = 2000       # Deuda considerada baja

# Base de conocimiento: reglas para aprobación
# Cada regla contiene:
# - Una condición (función lambda) que evalúa los datos del cliente
# - Un resultado que indica la decisión tomada
# - Una explicación que describe por qué se tomó esa decisión
reglas = [
    {
        "condicion": lambda x: x["historial"] == "bueno" and x["ingresos"] > UMBRAL_INGRESOS_BUENOS,
        "resultado": "Aprobado",
        "explicacion": "Historial bueno y buenos ingresos"
    },
    {
        "condicion": lambda x: x["historial"] == "regular" and x["ingresos"] > UMBRAL_INGRESOS_ALTOS and x["deuda"] < UMBRAL_DEUDA_BAJA,
        "resultado": "Aprobado con condiciones",
        "explicacion": "Historial regular compensado con alto ingreso y poca deuda"
    },
    {
        "condicion": lambda x: x["deuda"] > UMBRAL_DEUDA_ELEVADA,
        "resultado": "Rechazado",
        "explicacion": "Deuda muy elevada"
    },
    {
        "condicion": lambda x: True,  # Regla por defecto si ninguna otra se cumple
        "resultado": "Requiere evaluación manual",
        "explicacion": "No se cumplen reglas automáticas"
    }
]

# -------------------------------------------------------------
# Función para validar datos del cliente
# -------------------------------------------------------------
# Esta función verifica que los datos del cliente sean válidos:
# - Que contengan los campos requeridos: 'historial', 'ingresos', 'deuda'
# - Que los valores de 'ingresos' y 'deuda' sean numéricos
# - Que el valor de 'historial' sea uno de los permitidos: 'bueno', 'regular', 'malo'
def validar_cliente(cliente):
    campos_requeridos = ["historial", "ingresos", "deuda"]
    for campo in campos_requeridos:
        if campo not in cliente:
            raise ValueError(f"Falta el campo requerido: {campo}")
    if not isinstance(cliente["ingresos"], (int, float)) or not isinstance(cliente["deuda"], (int, float)):
        raise ValueError("Los campos 'ingresos' y 'deuda' deben ser numéricos.")
    if cliente["historial"] not in ["bueno", "regular", "malo"]:
        raise ValueError("El campo 'historial' debe ser 'bueno', 'regular' o 'malo'.")

# -------------------------------------------------------------
# Función principal: evaluar y explicar decisión
# -------------------------------------------------------------
# Esta función evalúa los datos del cliente según las reglas definidas.
# Devuelve un diccionario con:
# - La decisión tomada
# - Una explicación de la decisión
# - Información relevante sobre el cliente
def evaluar_cliente(cliente):
    # Validar los datos del cliente antes de evaluarlo
    validar_cliente(cliente)
    
    # Evaluar las reglas en orden
    for regla in reglas:
        if regla["condicion"](cliente):  # Si la condición de la regla se cumple
            return {
                "decisión": regla["resultado"],  # Resultado de la regla
                "explicación": regla["explicacion"],  # Explicación de la regla
                "información_relevante": {  # Información del cliente usada en la evaluación
                    "historial": cliente["historial"],
                    "ingresos": cliente["ingresos"],
                    "deuda": cliente["deuda"]
                }
            }
    # Si ninguna regla se cumple (caso improbable)
    return {"decisión": "No evaluado"}

# -------------------------------------------------------------
# Prueba con varios clientes
# -------------------------------------------------------------
# Lista de clientes a evaluar. Cada cliente es un diccionario con:
# - 'historial': calidad del historial crediticio ('bueno', 'regular', 'malo')
# - 'ingresos': ingresos mensuales del cliente
# - 'deuda': monto total de la deuda del cliente
clientes = [
    {"historial": "bueno", "ingresos": 6000, "deuda": 1000},  # Caso con buenos ingresos y buen historial
    {"historial": "regular", "ingresos": 7500, "deuda": 1500},  # Caso con ingresos altos y deuda baja
    {"historial": "malo", "ingresos": 4000, "deuda": 9000},  # Caso con historial malo y deuda elevada
    {"historial": "bueno", "ingresos": 4000, "deuda": 3000},  # Caso con ingresos bajos y deuda moderada
    {"historial": "regular", "ingresos": 8000, "deuda": 1000}  # Caso adicional con ingresos altos y deuda baja
]

# Evaluar cada cliente y mostrar los resultados
for c in clientes:
    try:
        # Evaluar al cliente y obtener el resultado
        resultado = evaluar_cliente(c)
        # Imprimir el resultado de la evaluación
        print(f"\nEvaluación del cliente: {c}")
        print(f"[OK] Decisión: {resultado['decisión']}")
        print(f"[INFO] Explicación: {resultado['explicación']}")
        print(f"[DATA] Información relevante: {resultado['información_relevante']}")
    except ValueError as e:
        # Manejar errores en los datos del cliente
        print(f"[ERROR] Error al evaluar cliente {c}: {e}")

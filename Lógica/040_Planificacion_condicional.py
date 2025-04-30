# --------------------------------------------------------
# Planificación Condicional: Buscar llaves en múltiples lugares
# --------------------------------------------------------

# Estado inicial: Representa las ubicaciones posibles de las llaves y si ya se tienen o no.
estado_inicial = {
    "ubicaciones": {
        "mesa": True,        # Las llaves están en la mesa (True indica que están aquí).
        "mochila": False,    # Las llaves no están en la mochila.
        "cajon": False,      # Las llaves no están en el cajón.
        "bolsillo": False    # Las llaves no están en el bolsillo.
    },
    "tiene_llaves": False    # Inicialmente no se tienen las llaves.
}

# --------------------------------------------------------
# Acción genérica para revisar una ubicación
# Esta función simula la acción de buscar las llaves en un lugar específico.
# Recibe el estado actual y el lugar a revisar.
def revisar_ubicacion(estado, lugar):
    print(f"Revisando {lugar}...")  # Mensaje para indicar dónde se está buscando.
    
    # Verifica si las llaves están en el lugar especificado.
    if estado["ubicaciones"].get(lugar, False):  # .get() devuelve False si el lugar no existe.
        estado["tiene_llaves"] = True  # Actualiza el estado indicando que ya se tienen las llaves.
        print(f"¡Encontraste las llaves en {lugar}!")  # Mensaje de éxito.
    else:
        print(f"No están en {lugar}.")  # Mensaje indicando que no están en este lugar.
    
    return estado  # Devuelve el estado actualizado.

# --------------------------------------------------------
# Planificación condicional
# Esta función implementa el plan para buscar las llaves en un orden específico.
def plan_condicional(estado):
    print("\nIniciando plan condicional...")  # Mensaje inicial.
    
    # Define el plan como una lista de lugares a revisar en orden.
    plan = ["mesa", "mochila", "cajon", "bolsillo"]

    # Itera sobre cada lugar en el plan.
    for lugar in plan:
        # Llama a la función para revisar el lugar actual.
        estado = revisar_ubicacion(estado, lugar)
        
        # Si las llaves ya se encontraron, se detiene el plan.
        if estado["tiene_llaves"]:
            break

    # Verificación final: Se evalúa si el objetivo se cumplió.
    if estado["tiene_llaves"]:
        print("\nObjetivo alcanzado: tienes las llaves.")  # Mensaje de éxito.
    else:
        print("\nNo se encontró ninguna solución.")  # Mensaje de fallo si no se encontraron las llaves.

# --------------------------------------------------------
# Ejecutar el plan
# Se llama a la función de planificación condicional con una copia del estado inicial.
plan_condicional(estado_inicial.copy())

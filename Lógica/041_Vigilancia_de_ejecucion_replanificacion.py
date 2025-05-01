# -------------------------------------------------------
# Vigilancia de Ejecución y Replanificación: Entrega de paquete
# -------------------------------------------------------
# Este programa simula un sistema de vigilancia de ejecución y replanificación
# para un robot que debe entregar un paquete. Si el plan inicial falla, el robot
# genera un nuevo plan basado en el estado actual del mundo.

# Estado inicial del mundo
estado = {
    "ubicacion_robot": "pasillo",  # Ubicación inicial del robot
    "paquete_disponible": True,   # Indica si el paquete está disponible para ser tomado
    "paquete_entregado": False    # Indica si el paquete ha sido entregado
}

# Plan inicial (lista de acciones que el robot debe ejecutar)
plan_original = ["ir_al_almacen", "tomar_paquete", "llevar_a_oficina"]

# -------------------------------------------------------
# Definición de acciones del plan
# Cada acción modifica el estado del mundo y devuelve True si tuvo éxito o False si falló.

def ir_al_almacen(estado):
    # Acción: Mover el robot al almacén
    print("El robot va al almacén.")
    estado["ubicacion_robot"] = "almacen"  # Actualiza la ubicación del robot
    return True  # Esta acción siempre tiene éxito

def tomar_paquete(estado):
    # Acción: Tomar el paquete del almacén
    print("El robot intenta tomar el paquete.")
    if estado["ubicacion_robot"] == "almacen" and estado["paquete_disponible"]:
        # Si el robot está en el almacén y el paquete está disponible, lo toma
        estado["paquete_disponible"] = False  # El paquete ya no está disponible
        print("Paquete tomado.")
        return True
    else:
        # Si no se cumplen las condiciones, la acción falla
        print("¡Error! No se pudo tomar el paquete.")
        return False

def llevar_a_oficina(estado):
    # Acción: Llevar el paquete a la oficina
    print("El robot lleva el paquete a la oficina.")
    if estado["ubicacion_robot"] == "almacen":
        # Si el robot está en el almacén, puede llevar el paquete a la oficina
        estado["ubicacion_robot"] = "oficina"  # Actualiza la ubicación del robot
        estado["paquete_entregado"] = True    # Marca el paquete como entregado
        print("Paquete entregado.")
        return True
    else:
        # Si no está en el almacén, la acción falla
        print("No está en el lugar correcto para entregar.")
        return False

# Mapa de acciones disponibles
# Este diccionario asocia los nombres de las acciones con las funciones correspondientes
acciones = {
    "ir_al_almacen": ir_al_almacen,
    "tomar_paquete": tomar_paquete,
    "llevar_a_oficina": llevar_a_oficina
}

# -------------------------------------------------------
# Función para registrar el estado actual
def log_estado(estado):
    # Imprime el estado actual del mundo
    print(f"Estado actual: {estado}")

# -------------------------------------------------------
# Vigilancia de Ejecución
def ejecutar_plan(plan, estado):
    # Ejecuta un plan de acciones paso a paso
    print("\nIniciando ejecución del plan...")
    for paso in plan:
        accion = acciones.get(paso)  # Obtiene la acción correspondiente al paso
        if accion:
            # Ejecuta la acción y registra el estado
            exito = accion(estado)
            log_estado(estado)
            if not exito:
                # Si una acción falla, se requiere replanificación
                print("\nFallo detectado: replanificando...\n")
                return False
        else:
            # Si la acción no está definida, se aborta el plan
            print(f"Acción desconocida: {paso}. Abortando plan.")
            return False
    return True  # El plan se ejecutó con éxito

# -------------------------------------------------------
# Replanificador mejorado
def replanificar(estado):
    # Genera un nuevo plan basado en el estado actual del mundo
    print("Replanificando basado en nuevo estado...")
    nuevo_plan = []
    if estado["ubicacion_robot"] != "almacen":
        # Si el robot no está en el almacén, debe ir al almacén
        nuevo_plan.append("ir_al_almacen")
    if estado["paquete_disponible"]:
        # Si el paquete está disponible, debe tomarlo
        nuevo_plan.append("tomar_paquete")
    if not estado["paquete_entregado"]:
        # Si el paquete no ha sido entregado, debe llevarlo a la oficina
        nuevo_plan.append("llevar_a_oficina")
    return nuevo_plan

# -------------------------------------------------------
# Simulación de escenarios
def simular_escenario(estado_inicial, plan):
    # Simula la ejecución de un plan en un escenario dado
    estado = estado_inicial.copy()  # Copia el estado inicial para no modificarlo
    resultado = ejecutar_plan(plan, estado)  # Ejecuta el plan
    if not resultado:
        # Si el plan falla, genera un nuevo plan y lo ejecuta
        nuevo_plan = replanificar(estado)
        print("Nuevo plan:", nuevo_plan)
        ejecutar_plan(nuevo_plan, estado)
    verificar_entrega(estado)  # Verifica si el paquete fue entregado

def verificar_entrega(estado):
    # Verifica si el paquete fue entregado exitosamente
    if estado["paquete_entregado"]:
        print("\nEl paquete fue entregado exitosamente.")
    else:
        print("\nEl paquete no fue entregado.")

# -------------------------------------------------------
# Escenarios de prueba
# Escenario 1: El paquete no está disponible
print("🔹 Escenario 1: El paquete NO está disponible")
estado_escenario_1 = {
    "ubicacion_robot": "pasillo",
    "paquete_disponible": False,
    "paquete_entregado": False
}
simular_escenario(estado_escenario_1, plan_original)

# Escenario 2: El robot no está en el almacén
print("\n🔹 Escenario 2: El robot no está en el almacén")
estado_escenario_2 = {
    "ubicacion_robot": "oficina",
    "paquete_disponible": True,
    "paquete_entregado": False
}
simular_escenario(estado_escenario_2, plan_original)

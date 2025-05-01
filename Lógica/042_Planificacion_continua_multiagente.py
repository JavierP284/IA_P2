# -----------------------------------------------------------------
# Planificación Continua y Multiagente: Robots en una bodega
# -----------------------------------------------------------------

import random  # Para simular eventos aleatorios
import time    # Para simular tiempo real en la ejecución

# -----------------------------------------------------------------
# Inicialización del estado del mundo
def inicializar_estado(paquetes, robots):
    """
    Inicializa el estado del mundo con paquetes y robots.

    Args:
        paquetes (dict): Diccionario con paquetes y sus ubicaciones iniciales.
        robots (dict): Diccionario con robots y sus ubicaciones iniciales.

    Returns:
        dict: Estado inicial del mundo.
    """
    return {
        "paquetes": paquetes,  # Ubicación inicial de los paquetes
        "robots": robots,      # Ubicación inicial de los robots
        "ocupado": set()       # Conjunto de zonas ocupadas (vacío al inicio)
    }

# Estado inicial del sistema
estado = inicializar_estado(
    paquetes={"P1": "zonaA", "P2": "zonaB"},  # Paquetes y sus ubicaciones iniciales
    robots={"R1": "inicio", "R2": "inicio"}  # Robots y sus ubicaciones iniciales
)

# Objetivo: cada robot debe recoger un paquete específico
objetivos = {"R1": "P1", "R2": "P2"}

# -----------------------------------------------------------------
# Función para mostrar el estado actual del mundo
def mostrar_estado():
    """
    Muestra el estado actual del sistema, incluyendo:
    - Ubicación de los paquetes
    - Ubicación de los robots
    - Zonas ocupadas
    """
    print("\nEstado actual:")
    print(f"Paquetes: {estado['paquetes']}")  # Paquetes y sus ubicaciones
    print(f"Robots: {estado['robots']}")      # Robots y sus ubicaciones
    print(f"Zonas ocupadas: {estado['ocupado']}\n")  # Zonas actualmente ocupadas

# -----------------------------------------------------------------
# Función para registrar eventos
def log_evento(mensaje):
    """
    Registra un evento en la consola y en un archivo de texto.

    Args:
        mensaje (str): Mensaje del evento.
    """
    print(mensaje)  # Muestra el mensaje en la consola
    with open("registro_eventos.txt", "a") as archivo:
        archivo.write(mensaje + "\n")  # Guarda el mensaje en un archivo de texto

# -----------------------------------------------------------------
# Función para que un robot intente recoger un paquete
def recoger_paquete(robot, paquete):
    """
    Intenta que un robot recoja un paquete de una zona específica.

    Args:
        robot (str): Nombre del robot.
        paquete (str): Nombre del paquete.

    Returns:
        bool: True si el robot logra recoger el paquete, False en caso contrario.
    """
    # Obtener la ubicación del paquete y del robot
    zona = estado["paquetes"].get(paquete)  # Zona donde está el paquete
    ubicacion_robot = estado["robots"][robot]  # Ubicación actual del robot

    log_evento(f"\n{robot} quiere ir a recoger {paquete} en {zona}...")

    # Verificar si el paquete sigue disponible
    if paquete not in estado["paquetes"]:
        log_evento(f"{paquete} ya no está disponible.")  # El paquete ya no está en el sistema
        return False

    # Verificar si la zona está ocupada
    if zona in estado["ocupado"]:
        log_evento(f"{robot} espera: {zona} está ocupada.")  # El robot debe esperar
        return False

    # Mover al robot a la zona del paquete
    estado["ocupado"].discard(ubicacion_robot)  # Liberar la zona anterior del robot
    estado["robots"][robot] = zona              # Actualizar la ubicación del robot
    estado["ocupado"].add(zona)                 # Marcar la nueva zona como ocupada
    log_evento(f"{robot} se mueve a {zona}.")

    # Simular un evento inesperado: el paquete desaparece con cierta probabilidad
    if random.random() < 0.2:  # 20% de probabilidad de que el paquete desaparezca
        log_evento(f"Evento inesperado: {paquete} desapareció.")
        estado["paquetes"].pop(paquete)  # Eliminar el paquete del estado
        return False

    # El robot recoge el paquete
    log_evento(f"{robot} recogió el paquete {paquete}.")
    estado["paquetes"].pop(paquete)  # Eliminar el paquete del estado
    estado["ocupado"].discard(zona)  # Liberar la zona donde estaba el paquete
    return True

# -----------------------------------------------------------------
# Simulador de planificación continua para todos los robots
def plan_multiagente():
    """
    Ejecuta la planificación continua para que los robots cumplan sus objetivos.
    - Cada robot intenta recoger su paquete asignado.
    - Se simulan eventos inesperados y se actualiza el estado dinámicamente.
    """
    pasos = 0          # Contador de pasos de simulación
    max_pasos = 10     # Máximo número de pasos permitidos

    while pasos < max_pasos and objetivos:  # Continuar mientras haya objetivos pendientes
        mostrar_estado()  # Mostrar el estado actual del sistema
        for robot, paquete in list(objetivos.items()):  # Iterar sobre los objetivos
            exito = recoger_paquete(robot, paquete)  # Intentar recoger el paquete
            if exito:
                log_evento(f"{robot} completó su tarea.")  # Registrar éxito
                objetivos.pop(robot)  # Eliminar el objetivo cumplido
            time.sleep(1)  # Simular tiempo real con una pausa
        pasos += 1  # Incrementar el contador de pasos

    # Verificar si se cumplieron todos los objetivos
    if not objetivos:
        log_evento("\nTodos los robots cumplieron sus tareas.")  # Éxito total
    else:
        log_evento("\nNo se pudieron cumplir todos los objetivos.")  # Algunos objetivos fallaron

# -----------------------------------------------------------------
# Ejecutar simulación
if __name__ == "__main__":
    print("Iniciando planificación continua multiagente...\n")
    plan_multiagente()

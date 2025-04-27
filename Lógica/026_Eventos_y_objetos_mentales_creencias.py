# ----------------------------------------------
# Ejemplo de Creencias en un Agente con Eventos
# ----------------------------------------------

class Agente:
    """
    Clase que representa un agente con un modelo de creencias.
    """
    def __init__(self, nombre):
        # Inicializa el agente con un nombre y un diccionario vacío de creencias
        self.nombre = nombre
        self.creencias = {}  # Diccionario para almacenar creencias actuales

    def agregar_creencia(self, hecho, valor):
        """
        Agrega una nueva creencia al agente.
        :param hecho: La creencia o hecho (clave del diccionario).
        :param valor: El valor asociado a la creencia (puede ser True/False u otro valor).
        """
        self.creencias[hecho] = valor
        print(f"{self.nombre} ahora cree que '{hecho}' es {valor}.")

    def actualizar_creencia(self, hecho, nuevo_valor):
        """
        Actualiza una creencia existente o agrega una nueva si no existe.
        :param hecho: La creencia o hecho a actualizar.
        :param nuevo_valor: El nuevo valor de la creencia.
        """
        if hecho in self.creencias:
            # Si la creencia ya existe, se actualiza su valor
            print(f"{self.nombre} actualiza su creencia: '{hecho}' era {self.creencias[hecho]}, ahora es {nuevo_valor}.")
        else:
            # Si la creencia no existe, se agrega como nueva
            print(f"{self.nombre} aprende una nueva creencia: '{hecho}' es {nuevo_valor}.")
        self.creencias[hecho] = nuevo_valor

    def eliminar_creencia(self, hecho):
        """
        Elimina una creencia del agente.
        :param hecho: La creencia o hecho a eliminar.
        """
        if hecho in self.creencias:
            # Si la creencia existe, se elimina
            print(f"{self.nombre} olvida la creencia: '{hecho}'.")
            del self.creencias[hecho]
        else:
            # Si la creencia no existe, se informa al usuario
            print(f"{self.nombre} no tiene la creencia: '{hecho}' para olvidar.")

    def mostrar_creencias(self):
        """
        Muestra todas las creencias actuales del agente.
        """
        print(f"\nCreencias actuales de {self.nombre}:")
        if not self.creencias:
            # Si no hay creencias, se indica que el agente no tiene ninguna
            print(" - No tiene creencias.")
        else:
            # Se muestran todas las creencias y sus valores
            for hecho, valor in self.creencias.items():
                print(f" - {hecho}: {valor}")


class Evento:
    """
    Clase que representa un evento que puede afectar las creencias de un agente.
    """
    def __init__(self, descripcion, impacto):
        """
        Inicializa un evento con una descripción y su impacto en las creencias.
        :param descripcion: Descripción del evento.
        :param impacto: Diccionario con los cambios en las creencias (clave: hecho, valor: nuevo valor).
        """
        self.descripcion = descripcion
        self.impacto = impacto

    def aplicar_evento(self, agente):
        """
        Aplica el impacto del evento a las creencias del agente.
        :param agente: El agente cuyas creencias serán afectadas.
        """
        print(f"\nEvento: {self.descripcion}")
        # Itera sobre los cambios en las creencias y los aplica al agente
        for hecho, nuevo_valor in self.impacto.items():
            agente.actualizar_creencia(hecho, nuevo_valor)


# ----------------------------------------------
# Simulación de eventos y creencias
# ----------------------------------------------

# Crear un agente llamado "Robo"
robo = Agente("Robo")

# Estado inicial: Robo cree que el clima es soleado
robo.agregar_creencia("clima_soleado", True)

# Crear un evento: Comienza a llover
evento_lluvia = Evento(
    descripcion="Comienza a llover",  # Descripción del evento
    impacto={"clima_soleado": False, "lluvia": True}  # Cambios en las creencias
)

# Aplicar el evento al agente
evento_lluvia.aplicar_evento(robo)

# Mostrar el estado de las creencias después del evento
robo.mostrar_creencias()

# Crear otro evento: Sale el sol nuevamente
evento_sol = Evento(
    descripcion="Sale el sol nuevamente",  # Descripción del evento
    impacto={"clima_soleado": True, "lluvia": False}  # Cambios en las creencias
)

# Aplicar el evento al agente
evento_sol.aplicar_evento(robo)

# Mostrar el estado de las creencias después del segundo evento
robo.mostrar_creencias()

# Eliminar una creencia
robo.eliminar_creencia("lluvia")  # Robo olvida la creencia sobre la lluvia
robo.mostrar_creencias()  # Mostrar las creencias finales del agente

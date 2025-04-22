# ----------------------------
# Agente Lógico Simple Mejorado
# ----------------------------

class AgenteLogico:
    """
    Clase que representa un agente lógico simple basado en reglas.
    Este agente evalúa una base de conocimientos para decidir si puede salir
    de acuerdo con ciertas condiciones.
    """
    def __init__(self, base_conocimientos):
        """
        Inicializa el agente con una base de conocimientos.
        :param base_conocimientos: Diccionario con los hechos del entorno.
        """
        self.base_conocimientos = base_conocimientos  # Almacena los hechos conocidos sobre el entorno

    def puede_salir(self):
        """
        Evalúa las reglas para determinar si el agente puede salir.
        :return: True si puede salir, False en caso contrario.
        """
        # Alias para simplificar el acceso a la base de conocimientos
        bc = self.base_conocimientos

        # Regla 1: Si está soleado y tiene llaves, puede salir sin paraguas
        if bc.get("soleado", False) and bc.get("tiene_llaves", False):
            print("Puede salir sin paraguas: hace sol y tiene llaves.")
            return True

        # Regla 2: Si no está soleado, pero tiene paraguas y llaves, puede salir
        if not bc.get("soleado", False) and bc.get("tiene_paraguas", False) and bc.get("tiene_llaves", False):
            print("Puede salir con paraguas: no hace sol, pero está preparado.")
            return True

        # Si no cumple ninguna regla, no puede salir
        print("No puede salir: condiciones no adecuadas.")
        return False

    def actualizar_conocimiento(self, clave, valor):
        """
        Actualiza un hecho en la base de conocimientos.
        :param clave: Clave del hecho a actualizar.
        :param valor: Nuevo valor del hecho.
        """
        # Actualiza el valor de la clave en la base de conocimientos
        self.base_conocimientos[clave] = valor
        # Muestra la base de conocimientos actualizada
        print(f"Base de conocimientos actualizada: {self.base_conocimientos}")


# Ejemplo de uso
if __name__ == "__main__":
    # Base de conocimientos inicial
    # Representa el estado inicial del entorno
    base_conocimientos = {
        "soleado": True,          # Indica si está soleado
        "tiene_llaves": True,     # Indica si el agente tiene llaves
        "tiene_paraguas": False   # Indica si el agente tiene un paraguas
    }

    # Crear el agente con la base de conocimientos inicial
    agente = AgenteLogico(base_conocimientos)

    # Evaluar si el agente puede salir con las condiciones iniciales
    agente.puede_salir()

    # Actualizar la base de conocimientos para simular un cambio en el entorno
    agente.actualizar_conocimiento("soleado", False)  # Ahora no está soleado
    agente.actualizar_conocimiento("tiene_paraguas", True)  # Ahora tiene un paraguas

    # Evaluar nuevamente si el agente puede salir con las nuevas condiciones
    agente.puede_salir()

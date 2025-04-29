from enum import Enum

# Enumeración para representar los posibles estados de vuelo de un animal
class EstadoVuelo(Enum):
    PUEDE_VOLAR = "puede_volar"  # El animal puede volar
    NO_PUEDE_VOLAR = "no_puede_volar"  # El animal no puede volar

# Clase que implementa el razonamiento por defecto y no monotónico
class RazonamientoPorDefecto:
    def __init__(self, hechos):
        """
        Inicializa el razonador con una base de hechos.
        
        Args:
            hechos (dict): Diccionario que contiene información sobre los animales,
                          como cuáles son pájaros y cuáles son pingüinos.
        """
        self.hechos = hechos  # Base de hechos inicial
        self.creencias = {}  # Diccionario para almacenar las creencias derivadas

    def regla_por_defecto_volar(self, animal):
        """
        Aplica la regla por defecto para determinar si un animal puede volar.
        
        Args:
            animal (str): Nombre del animal a evaluar.
        """
        # Si el animal es un pájaro y no es un pingüino, puede volar por defecto
        if animal in self.hechos["pajaro"] and animal not in self.hechos.get("pinguino", []):
            self.creencias[animal] = EstadoVuelo.PUEDE_VOLAR.value
            print(f"Por defecto, {animal} puede volar.")
        # Si el animal es un pingüino, no puede volar
        elif animal in self.hechos.get("pinguino", []):
            self.creencias[animal] = EstadoVuelo.NO_PUEDE_VOLAR.value
            print(f"{animal} es un pingüino, no puede volar.")
        # Si no hay reglas aplicables, no se hace ninguna inferencia
        else:
            print(f"No hay reglas aplicables para {animal}.")

    def aplicar_razonamiento(self):
        """
        Aplica las reglas de razonamiento por defecto a todos los animales
        presentes en la base de hechos.
        """
        for animal in self.hechos["animal"]:
            self.regla_por_defecto_volar(animal)

    def mostrar_creencias(self):
        """
        Muestra las creencias actuales derivadas del razonamiento.
        """
        print("\nCreencias actuales:")
        for animal, estado in self.creencias.items():
            print(f" - {animal}: {estado}")

def main():
    """
    Función principal que ejecuta el razonamiento por defecto con una base de hechos inicial.
    """
    # Base de hechos inicial
    hechos = {
        "animal": ["tweety", "pingu"],  # Lista de todos los animales
        "pajaro": ["tweety", "pingu"],  # Lista de animales que son pájaros
        "pinguino": ["pingu"]  # Lista de animales que son pingüinos
    }

    # Crear una instancia del razonador con la base de hechos
    razonador = RazonamientoPorDefecto(hechos)
    print("Aplicando razonamiento por defecto...")
    
    # Aplicar las reglas de razonamiento por defecto
    razonador.aplicar_razonamiento()
    
    # Mostrar las creencias derivadas
    razonador.mostrar_creencias()

    # Actualizar las creencias con nueva información
    print("\nNueva información: Tweety está herido y no puede volar.")
    razonador.creencias["tweety"] = EstadoVuelo.NO_PUEDE_VOLAR.value  # Actualización manual
    razonador.mostrar_creencias()

# Punto de entrada del programa
if __name__ == "__main__":
    main()

import numpy as np

class AprendizajeRefuerzoPasivo:
    def __init__(self, estados, politica, gamma=0.9):
        """
        Inicializa el agente de Aprendizaje por Refuerzo Pasivo.
        
        estados: Lista de estados posibles.
        politica: Diccionario {estado: acción} que define la política fija.
        gamma: Factor de descuento para valorar recompensas futuras.
        """
        if not (0 <= gamma <= 1):
            raise ValueError("El factor de descuento gamma debe estar en el rango [0, 1].")
        
        self.estados = estados
        self.politica = politica
        self.gamma = gamma

        # Inicializar valores de estado arbitrarios
        self.valores_estado = {s: 0.0 for s in estados}
        self.visitas_estado = {s: 0 for s in estados}

    def actualizar_valores(self, episodios):
        """
        Ajusta los valores de los estados según las experiencias observadas.
        
        episodios: Lista de trayectorias [(estado, recompensa, próximo_estado), ...]
        """
        for episodio in episodios:
            recompensa_total = 0
            for t in reversed(range(len(episodio))):  # Recorre el episodio en orden inverso
                estado, recompensa, _ = episodio[t]
                
                # Validar que el estado esté en la lista de estados
                if estado not in self.estados:
                    raise ValueError(f"Estado desconocido: {estado}")
                
                recompensa_total = recompensa + self.gamma * recompensa_total  # Descuento futuro

                # Actualizar promedio del valor del estado
                self.visitas_estado[estado] += 1
                self.valores_estado[estado] += (recompensa_total - self.valores_estado[estado]) / self.visitas_estado[estado]

    def mostrar_valores(self):
        """ Muestra los valores estimados de cada estado """
        for estado, valor in self.valores_estado.items():
            print(f"Estado {estado}: Valor estimado {valor:.2f}")

# Definimos un conjunto de estados y una política fija
estados = ["A", "B", "C", "D"]
politica_fija = {"A": "Derecha", "B": "Derecha", "C": "Abajo", "D": "Fin"}

# Inicializamos el agente con la política dada
agente = AprendizajeRefuerzoPasivo(estados, politica_fija)

# Simulamos episodios de experiencia con recompensas
episodios = [
    [("A", 0, "B"), ("B", 0, "C"), ("C", 1, "D")],  # Episodio 1
    [("A", 0, "B"), ("B", 0, "C"), ("C", 1, "D")],  # Episodio 2 (repetido)
    [("A", 0, "B"), ("B", -1, "D")],  # Episodio 3 (recompensa negativa)
]

# Actualizamos los valores de los estados basados en los episodios
agente.actualizar_valores(episodios)

# Mostramos los valores finales aprendidos
agente.mostrar_valores()

import numpy as np
import random

class AprendizajeRefuerzoActivo:
    def __init__(self, estados, acciones, alpha=0.1, gamma=0.9, epsilon=0.1):
        """
        Inicializa el agente de Aprendizaje por Refuerzo Activo usando Q-Learning.
        
        estados: Lista de estados posibles.
        acciones: Lista de acciones disponibles.
        alpha: Tasa de aprendizaje (qué tan rápido se actualiza Q).
        gamma: Factor de descuento para valorar recompensas futuras.
        epsilon: Probabilidad de exploración (para evitar quedar atrapado en malas soluciones).
        """
        self.estados = estados
        self.acciones = acciones
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

        # Inicializar tabla Q con valores en 0
        self.q_table = {s: {a: 0.0 for a in acciones} for s in estados}

    def elegir_accion(self, estado):
        """
        Selecciona una acción basada en la política ε-greedy:
        - Con probabilidad epsilon, elige una acción aleatoria (exploración).
        - De lo contrario, elige la acción con el mayor valor Q (explotación).
        """
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(self.acciones)  # Explorar
        else:
            return max(self.q_table[estado], key=self.q_table[estado].get)  # Explotar

    def actualizar_q(self, estado, accion, recompensa, siguiente_estado):
        """
        Actualiza la tabla Q utilizando la ecuación de Q-Learning:
        Q(s, a) = Q(s, a) + α [recompensa + γ max(Q(s', a')) - Q(s, a)]
        """
        mejor_q_siguiente = max(self.q_table[siguiente_estado].values())  # Mejor Q(s', a')
        self.q_table[estado][accion] += self.alpha * (recompensa + self.gamma * mejor_q_siguiente - self.q_table[estado][accion])

    def entrenar(self, episodios):
        """
        Simula interacciones con el entorno para aprender una política óptima.
        
        episodios: Lista de trayectorias [(estado, acción, recompensa, próximo_estado), ...]
        """
        for episodio in episodios:
            for estado, accion, recompensa, siguiente_estado in episodio:
                self.actualizar_q(estado, accion, recompensa, siguiente_estado)

    def mostrar_politica(self):
        """ Muestra la mejor acción por estado después del aprendizaje """
        print("\nPolítica aprendida:")
        for estado in self.estados:
            mejor_accion = max(self.q_table[estado], key=self.q_table[estado].get)
            print(f"Estado {estado}: Mejor acción -> {mejor_accion}")

# Definir un conjunto de estados y acciones
estados = ["A", "B", "C", "D"]
acciones = ["Izquierda", "Derecha", "Arriba", "Abajo"]

# Crear agente de Q-Learning
agente = AprendizajeRefuerzoActivo(estados, acciones)

# Simulación de episodios de experiencia
episodios = [
    [("A", "Derecha", 0, "B"), ("B", "Derecha", 0, "C"), ("C", "Abajo", 1, "D")],  # Episodio 1
    [("A", "Derecha", 0, "B"), ("B", "Izquierda", -1, "A")],  # Episodio 2 (acción negativa)
    [("C", "Abajo", 1, "D")],  # Episodio 3 (recompensa alta)
]

# Entrenar al agente con los episodios simulados
agente.entrenar(episodios)

# Mostrar la política aprendida
agente.mostrar_politica()

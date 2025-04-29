# ----------------------------------------
# Ejemplo de Marco: Situación en un restaurante
# ----------------------------------------

class MarcoRestaurante:
    def __init__(self, cliente, mesa):
        """
        Inicializa un marco para un cliente en un restaurante.
        Parámetros:
        - cliente: Nombre del cliente.
        - mesa: Número de la mesa asignada al cliente.
        """
        self.cliente = cliente  # Nombre del cliente
        self.mesa = mesa  # Número de la mesa
        self.lugar = "Restaurante Genérico"  # Nombre del restaurante
        self.mesero = None  # Nombre del mesero asignado (inicialmente ninguno)
        self.pedido = []  # Lista de platillos pedidos por el cliente
        self.cuenta_pagada = False  # Indica si la cuenta ha sido pagada

    def asignar_mesero(self, nombre_mesero):
        """
        Asigna un mesero al cliente.
        Parámetros:
        - nombre_mesero: Nombre del mesero que atenderá al cliente.
        """
        if self.cuenta_pagada:
            # No se puede asignar un mesero si la cuenta ya fue pagada
            print("No se puede asignar un mesero después de pagar la cuenta.")
            return
        self.mesero = nombre_mesero  # Asigna el mesero al cliente
        print(f"El mesero asignado a {self.cliente} es {self.mesero}.")

    def ordenar(self, platillo):
        """
        Permite al cliente ordenar un platillo.
        Parámetros:
        - platillo: Nombre del platillo que el cliente desea ordenar.
        """
        if self.cuenta_pagada:
            # No se puede hacer un pedido si la cuenta ya fue pagada
            print("No se puede hacer un pedido después de pagar la cuenta.")
            return
        self.pedido.append(platillo)  # Agrega el platillo a la lista de pedidos
        print(f"{self.cliente} ordena '{platillo}'.")

    def pagar(self):
        """
        Permite al cliente pagar la cuenta.
        """
        if not self.pedido:
            # No se puede pagar si no se ha hecho ningún pedido
            print("No se puede pagar la cuenta sin haber hecho un pedido.")
            return
        if not self.mesero:
            # No se puede pagar si no hay un mesero asignado
            print("No se puede pagar la cuenta sin un mesero asignado.")
            return
        self.cuenta_pagada = True  # Marca la cuenta como pagada
        print(f"{self.cliente} ha pagado la cuenta. Pedido: {', '.join(self.pedido)}.")

    def mostrar_estado(self):
        """
        Muestra el estado actual del marco, incluyendo información del cliente,
        la mesa, el mesero, los pedidos y si la cuenta ha sido pagada.
        """
        print("\nEstado actual del marco:")
        print(f"Cliente: {self.cliente}")  # Nombre del cliente
        print(f"Mesa: {self.mesa}")  # Número de la mesa
        print(f"Lugar: {self.lugar}")  # Nombre del restaurante
        print(f"Mesero: {self.mesero if self.mesero else 'No asignado'}")  # Mesero asignado o "No asignado"
        print(f"Pedido: {', '.join(self.pedido) if self.pedido else 'Sin pedido'}")  # Lista de pedidos o "Sin pedido"
        print(f"Cuenta pagada: {'Sí' if self.cuenta_pagada else 'No'}")  # Estado de la cuenta

# ----------------------------------------
# Uso del marco en una situación específica
# ----------------------------------------

# Crear un marco con un cliente llamado "Laura" en la mesa 5
# Esto simula la llegada de un cliente al restaurante
evento = MarcoRestaurante("Laura", 5)

# Simular acciones en el restaurante
evento.asignar_mesero("Carlos")  # Asignar un mesero llamado "Carlos" al cliente
evento.ordenar("Pizza Margarita")  # El cliente ordena una Pizza Margarita
evento.ordenar("Ensalada César")  # El cliente ordena una Ensalada César
evento.mostrar_estado()  # Mostrar el estado actual del marco
evento.pagar()  # El cliente paga la cuenta
evento.mostrar_estado()  # Mostrar el estado actual después de pagar

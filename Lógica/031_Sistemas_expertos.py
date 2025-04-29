# --------------------------------------------
# Sistema Experto de Diagnóstico de Computadoras
# --------------------------------------------

class SistemaExperto:
    def __init__(self):
        """
        Inicializa el sistema experto con una base de hechos y una base de reglas.
        """
        # Base de hechos: Representa los síntomas que el usuario debe responder.
        self.hechos = {
            "enciende": None,  # Indica si la computadora enciende.
            "hay_sonido": None,  # Indica si hay sonido al encender.
            "hay_video": None  # Indica si hay video al encender.
        }

        # Base de reglas: Contiene las condiciones y el diagnóstico asociado.
        self.reglas = [
            {
                # Si la computadora no enciende y no hay sonido, el problema es la fuente de poder.
                "condiciones": {"enciende": False, "hay_sonido": False},
                "diagnostico": "Falla en la fuente de poder"
            },
            {
                # Si la computadora enciende pero no hay video, el problema es la tarjeta gráfica.
                "condiciones": {"enciende": True, "hay_video": False},
                "diagnostico": "Falla en la tarjeta gráfica"
            },
            {
                # Si la computadora enciende y hay video, el sistema funciona correctamente.
                "condiciones": {"enciende": True, "hay_video": True},
                "diagnostico": "El sistema parece estar funcionando correctamente"
            }
        ]

    def preguntar_usuario(self):
        """
        Solicita al usuario información sobre los síntomas de la computadora.
        Actualiza la base de hechos con las respuestas del usuario.
        """
        print("Diagnóstico de computadora: Responde con 'si' o 'no'")
        for hecho in self.hechos.keys():
            while True:
                # Pregunta al usuario sobre cada hecho (síntoma).
                respuesta = input(f"¿{hecho.replace('_', ' ')}? (si/no): ").strip().lower()
                if respuesta in ["si", "no"]:
                    # Convierte la respuesta en un valor booleano y lo guarda en la base de hechos.
                    self.hechos[hecho] = (respuesta == "si")
                    break
                else:
                    # Si la respuesta no es válida, solicita al usuario que intente de nuevo.
                    print("Por favor, responde con 'si' o 'no'.")

    def motor_inferencia(self):
        """
        Evalúa las reglas para determinar un diagnóstico basado en los hechos proporcionados.
        Retorna el diagnóstico correspondiente o un mensaje indicando que no se pudo diagnosticar.
        """
        for regla in self.reglas:
            # Verifica si todas las condiciones de una regla se cumplen con los hechos actuales.
            if all(self.hechos.get(cond) == val for cond, val in regla["condiciones"].items()):
                # Si se cumple, retorna el diagnóstico asociado a la regla.
                return regla["diagnostico"]
        # Si ninguna regla se cumple, retorna un mensaje indicando que no se pudo diagnosticar.
        return "No se pudo diagnosticar el problema."

    def ejecutar(self):
        """
        Ejecuta el sistema experto:
        1. Solicita información al usuario.
        2. Evalúa las reglas para determinar un diagnóstico.
        3. Muestra el diagnóstico al usuario.
        """
        self.preguntar_usuario()  # Solicita los síntomas al usuario.
        resultado = self.motor_inferencia()  # Determina el diagnóstico basado en las reglas.
        print("\nDiagnóstico:")  # Muestra el diagnóstico al usuario.
        print(f" - {resultado}")


# --------------------------------------------
# Ejecución del sistema experto
if __name__ == "__main__":
    # Crea una instancia del sistema experto y lo ejecuta.
    sistema = SistemaExperto()
    sistema.ejecutar()

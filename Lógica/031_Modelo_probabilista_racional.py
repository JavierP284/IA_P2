# ---------------------------------------------------
# Modelo Probabilista Racional: Decidir salir o quedarse
# ---------------------------------------------------
# Este programa utiliza un modelo probabilista racional para decidir entre dos acciones:
# salir o quedarse en casa, basándose en las probabilidades de lluvia y las utilidades
# asociadas a cada acción.

# ---------------------------------------------------
# Función para obtener las probabilidades y utilidades del usuario
def obtener_datos():
    """
    Solicita al usuario las probabilidades de lluvia y las utilidades asociadas
    a las acciones posibles (salir con lluvia, salir sin lluvia, quedarse en casa).
    """
    print("Ingrese las probabilidades (deben sumar 1):")
    
    # Solicitar la probabilidad de lluvia
    prob_lluvia = float(input("Probabilidad de lluvia (0 a 1): "))
    
    # Calcular la probabilidad complementaria (no lluvia)
    prob_no_lluvia = 1 - prob_lluvia

    print("\nIngrese las utilidades:")
    # Solicitar las utilidades asociadas a cada escenario
    utilidades = {
        "salir_con_lluvia": float(input("Utilidad de salir con lluvia (negativo): ")),
        "salir_sin_lluvia": float(input("Utilidad de salir sin lluvia (positivo): ")),
        "quedarse": float(input("Utilidad de quedarse en casa: "))
    }

    # Retornar las probabilidades y utilidades ingresadas
    return prob_lluvia, prob_no_lluvia, utilidades

# ---------------------------------------------------
# Función: calcular utilidad esperada para cada acción
def calcular_utilidad_esperada(prob_lluvia, prob_no_lluvia, utilidades):
    """
    Calcula la utilidad esperada para cada acción (salir o quedarse),
    considerando las probabilidades de lluvia y las utilidades asociadas.
    """
    # Calcular la utilidad esperada de salir
    utilidad_salir = (prob_lluvia * utilidades["salir_con_lluvia"] +
                      prob_no_lluvia * utilidades["salir_sin_lluvia"])
    
    # La utilidad de quedarse no depende del clima, es fija
    utilidad_quedarse = utilidades["quedarse"]
    
    # Retornar las utilidades esperadas de ambas acciones
    return utilidad_salir, utilidad_quedarse

# ---------------------------------------------------
# Decisión basada en la utilidad máxima
def decidir_accion(prob_lluvia, prob_no_lluvia, utilidades):
    """
    Compara las utilidades esperadas de las acciones (salir o quedarse)
    y determina cuál es la decisión óptima.
    """
    # Calcular las utilidades esperadas
    utilidad_salir, utilidad_quedarse = calcular_utilidad_esperada(prob_lluvia, prob_no_lluvia, utilidades)

    # Mostrar los resultados de las utilidades esperadas
    print("\n--- Resultados ---")
    print(f"Utilidad esperada de salir: {round(utilidad_salir, 2)}")
    print(f"Utilidad esperada de quedarse: {round(utilidad_quedarse, 2)}")

    # Comparar las utilidades y tomar la decisión óptima
    if utilidad_salir > utilidad_quedarse:
        print("\nDecisión óptima: ¡Salir!")
    else:
        print("\nDecisión óptima: Quedarse en casa.")

# ---------------------------------------------------
# Ejecutar el modelo
if __name__ == "__main__":
    """
    Punto de entrada principal del programa. Solicita los datos al usuario,
    calcula las utilidades esperadas y toma una decisión basada en el modelo.
    """
    print("Modelo Probabilista Racional: Decidir salir o quedarse")
    print("---------------------------------------------------")
    
    # Obtener las probabilidades y utilidades del usuario
    prob_lluvia, prob_no_lluvia, utilidades = obtener_datos()
    
    # Tomar la decisión óptima basada en las utilidades esperadas
    decidir_accion(prob_lluvia, prob_no_lluvia, utilidades)

# ----------------------------------------------------------
# Algoritmo de Mejor Hipótesis Actual (tipo Find-S)
# ----------------------------------------------------------

# Conjunto de entrenamiento: [color, tamaño, forma]
# Clase objetivo: 'sí' = es manzana, 'no' = no es manzana
# Cada ejemplo contiene una lista de atributos y una clase objetivo.
ejemplos = [
    (["rojo", "mediano", "redonda"], "sí"),  # Ejemplo positivo
    (["rojo", "mediano", "alargada"], "no"),  # Ejemplo negativo
    (["rojo", "grande", "redonda"], "sí"),  # Ejemplo positivo
    (["verde", "mediano", "redonda"], "no"),  # Ejemplo negativo
    (["rojo", "mediano", "redonda"], "sí")  # Ejemplo positivo
]

# Función para aplicar el algoritmo Find-S
def find_s(ejemplos):
    """
    Implementa el algoritmo Find-S para encontrar la hipótesis más específica
    que cubre todos los ejemplos positivos en el conjunto de entrenamiento.

    Parámetros:
    - ejemplos: Lista de tuplas, donde cada tupla contiene una lista de atributos
      y una clase objetivo ('sí' o 'no').

    Retorna:
    - hipotesis: Lista que representa la hipótesis más específica.
    """
    # Inicializar la hipótesis con los valores más específicos posibles ('Ø')
    hipotesis = ["Ø", "Ø", "Ø"]
    print("Evolución de la hipótesis:\n")
    
    # Iterar sobre cada ejemplo en el conjunto de entrenamiento
    for idx, (atributos, clase) in enumerate(ejemplos):
        print(f"Ejemplo {idx + 1}: {atributos}, Clase: {clase}")
        
        # Solo se actualiza la hipótesis con ejemplos positivos ('sí')
        if clase == "sí":
            for i in range(len(atributos)):
                # Si el atributo actual de la hipótesis es 'Ø', lo reemplazamos
                if hipotesis[i] == "Ø":
                    hipotesis[i] = atributos[i]  # Copiar el valor del atributo
                # Si el atributo actual de la hipótesis es diferente, generalizamos
                elif hipotesis[i] != atributos[i]:
                    hipotesis[i] = "?"  # '?' indica que el atributo no es relevante
        
        # Mostrar la hipótesis actual después de procesar el ejemplo
        print(f"Hipótesis actual: {hipotesis}\n")
    
    # Retornar la hipótesis final después de procesar todos los ejemplos
    return hipotesis

# Ejecutar el algoritmo Find-S con el conjunto de ejemplos
hipotesis_final = find_s(ejemplos)

# ----------------------------------------------------------
# Resultado final
# Mostrar la hipótesis más específica que cubre todos los ejemplos positivos
print("Hipótesis más específica que cubre los positivos:")
print("Resultado:", hipotesis_final)

# ----------------------------------------------------------
# Explicación adicional
# Explicación del significado de la hipótesis final
print("\nExplicación:")
print("La hipótesis final representa la descripción más general que cubre todos los ejemplos positivos.")
print("'?' indica que la característica no es relevante para clasificar como 'sí'.")

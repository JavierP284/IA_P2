# Algoritmo de Encadenamiento Hacia Adelante y Hacia Atrás

# ---------- BASE DE CONOCIMIENTOS ----------
# Hechos iniciales: conjunto de hechos que se consideran verdaderos al inicio.
hechos = {"llueve", "tiene_paraguas"}

# Reglas: cada regla está formada por un conjunto de condiciones (premisas) y una consecuencia.
# Si todas las condiciones de una regla son verdaderas, entonces la consecuencia también lo será.
reglas = [
    ({"llueve", "tiene_paraguas"}, "no_se_moja"),  # Si llueve y tiene paraguas, entonces no se moja.
    ({"no_se_moja"}, "feliz"),                    # Si no se moja, entonces está feliz.
    ({"llueve"}, "suelo_mojado"),                 # Si llueve, entonces el suelo está mojado.
    ({"suelo_mojado", "tiene_zapatos"}, "zapatos_mojados"),  # Si el suelo está mojado y tiene zapatos, los zapatos se mojan.
]

# ---------- ENCANDENAMIENTO HACIA ADELANTE ----------
def encadenamiento_adelante(hechos, reglas):
    """
    Realiza el encadenamiento hacia adelante.
    Agrega nuevas inferencias a los hechos basándose en las reglas.
    
    Parámetros:
    - hechos: conjunto de hechos iniciales.
    - reglas: lista de reglas (condiciones → consecuencia).
    
    Retorna:
    - hechos: conjunto de hechos después de aplicar el encadenamiento hacia adelante.
    """
    nuevos = True  # Variable para controlar si se han inferido nuevos hechos.
    while nuevos:
        nuevos = False  # Suponemos que no habrá nuevos hechos en esta iteración.
        for condiciones, consecuencia in reglas:
            # Verificamos si todas las condiciones de la regla están en los hechos actuales.
            if condiciones.issubset(hechos) and consecuencia not in hechos:
                # Si la regla se cumple y la consecuencia no está en los hechos, la agregamos.
                hechos.add(consecuencia)
                print(f"Nueva inferencia (adelante): {consecuencia}")
                nuevos = True  # Indicamos que se ha inferido un nuevo hecho.
    return hechos

# ---------- ENCANDENAMIENTO HACIA ATRÁS ----------
def encadenamiento_atras(meta, hechos, reglas):
    """
    Realiza el encadenamiento hacia atrás.
    Intenta probar si la meta puede ser alcanzada a partir de los hechos y reglas.
    
    Parámetros:
    - meta: hecho que queremos probar si es alcanzable.
    - hechos: conjunto de hechos iniciales.
    - reglas: lista de reglas (condiciones → consecuencia).
    
    Retorna:
    - True si la meta puede ser alcanzada, False en caso contrario.
    """
    # Caso base: si la meta ya está en los hechos, no necesitamos probar nada más.
    if meta in hechos:
        print(f"Meta '{meta}' encontrada directamente en los hechos.")
        return True
    
    # Recorremos las reglas para buscar una cuya consecuencia sea la meta.
    for condiciones, consecuencia in reglas:
        if consecuencia == meta:
            print(f"Tratando de probar '{meta}' usando regla: {condiciones} → {consecuencia}")
            # Intentamos probar todas las condiciones de la regla recursivamente.
            if all(encadenamiento_atras(cond, hechos, reglas) for cond in condiciones):
                # Si todas las condiciones se cumplen, agregamos la meta a los hechos.
                hechos.add(meta)
                print(f"Meta '{meta}' alcanzada por encadenamiento hacia atrás.")
                return True
    
    # Si no encontramos una forma de probar la meta, devolvemos False.
    print(f"No se puede probar la meta '{meta}'.")
    return False

# ---------- FUNCIÓN PRINCIPAL ----------
def main():
    """
    Ejecuta ejemplos de encadenamiento hacia adelante y hacia atrás.
    """
    # Copiamos los hechos iniciales para que los dos métodos trabajen de forma independiente.
    hechos_adelante = hechos.copy()
    print("Encadenamiento hacia adelante:")
    # Aplicamos el encadenamiento hacia adelante y mostramos los hechos finales.
    resultado_adelante = encadenamiento_adelante(hechos_adelante, reglas)
    print("Hechos finales:", resultado_adelante)

    print("\nEncadenamiento hacia atrás (meta: 'feliz'):")
    # Copiamos los hechos iniciales para el encadenamiento hacia atrás.
    hechos_atras = hechos.copy()
    # Intentamos probar si la meta 'feliz' puede ser alcanzada.
    resultado_atras = encadenamiento_atras("feliz", hechos_atras, reglas)
    print("¿Meta alcanzada?:", resultado_atras)

# ---------- EJECUCIÓN ----------
if __name__ == "__main__":
    main()

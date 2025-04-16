# Algoritmo de Inferencia Lógica Proposicional utilizando Modus Ponens

def modus_ponens(base_conocimiento, hechos):
    """
    Aplica la regla de Modus Ponens para inferir nuevos hechos a partir de una base de conocimiento.
    
    Args:
        base_conocimiento (list): Lista de reglas en formato 'P => Q'.
        hechos (list): Lista de hechos conocidos.

    Returns:
        list: Nuevos hechos inferidos.
    """
    # Lista para almacenar los nuevos hechos inferidos
    inferencias = []
    print("Aplicando inferencia lógica con Modus Ponens...\n")

    # Iteramos sobre cada regla en la base de conocimiento
    for regla in base_conocimiento:
        # Verificamos si la regla tiene el formato correcto (contiene '=>')
        if '=>' in regla:
            # Dividimos la regla en antecedente (P) y consecuente (Q)
            antecedente, consecuente = regla.split('=>')
            antecedente = antecedente.strip()  # Eliminamos espacios en blanco
            consecuente = consecuente.strip()

            # Verificamos si el antecedente está en los hechos conocidos
            # y si el consecuente aún no ha sido inferido
            if antecedente in hechos and consecuente not in hechos:
                # Inferimos el consecuente y lo añadimos a la lista de inferencias
                print(f"Dado que '{antecedente}' es verdadero, inferimos '{consecuente}'")
                inferencias.append(consecuente)
            else:
                # Si no se puede aplicar la regla, explicamos por qué
                print(f"No se puede aplicar la regla '{regla}' porque '{antecedente}' no está en los hechos o '{consecuente}' ya es conocido.")
    
    # Devolvemos la lista de nuevos hechos inferidos
    return inferencias

def inferencia_iterativa(base_conocimiento, hechos):
    """
    Realiza inferencia iterativa hasta que no se puedan inferir nuevos hechos.
    
    Args:
        base_conocimiento (list): Lista de reglas en formato 'P => Q'.
        hechos (list): Lista de hechos conocidos iniciales.

    Returns:
        list: Lista completa de hechos conocidos después de la inferencia.
    """
    # Creamos una copia de los hechos iniciales para no modificar la lista original
    nuevos_hechos = hechos[:]
    
    # Ciclo infinito que se detendrá cuando no haya nuevos hechos inferidos
    while True:
        # Aplicamos Modus Ponens para inferir nuevos hechos
        inferidos = modus_ponens(base_conocimiento, nuevos_hechos)
        
        # Si no se infiere nada nuevo, salimos del ciclo
        if not inferidos:
            break
        
        # Añadimos los nuevos hechos inferidos a la lista de hechos conocidos
        nuevos_hechos.extend(inferidos)
    
    # Devolvemos la lista completa de hechos conocidos después de la inferencia
    return nuevos_hechos

# Base de conocimiento (reglas lógicas proposicionales)
# Cada regla está en el formato "P => Q", donde P es el antecedente y Q es el consecuente
base_conocimiento = [
    "llueve => está_nublado",       # Si llueve, entonces está nublado
    "está_nublado => hace_frío",    # Si está nublado, entonces hace frío
    "tengo_paraguas => no_me_mojo", # Si tengo paraguas, entonces no me mojo
    "hace_frío => uso_abrigo"       # Si hace frío, entonces uso abrigo
]

# Hechos conocidos iniciales
# Estos son los hechos que sabemos que son verdaderos al inicio
hechos = ["llueve", "tengo_paraguas"]

# Mostramos los hechos iniciales
print("Hechos iniciales:", hechos)

# Aplicamos la inferencia iterativa para obtener todos los hechos posibles
hechos_completos = inferencia_iterativa(base_conocimiento, hechos)

# Mostramos todos los hechos conocidos después de aplicar la inferencia
print("\nHechos conocidos después de la inferencia:")
for hecho in hechos_completos:
    print(f"- {hecho}")

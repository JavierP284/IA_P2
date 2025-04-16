"""
Base de conocimiento para diagnóstico médico.
Este programa compara los síntomas proporcionados por el usuario con una base de conocimiento
y sugiere posibles diagnósticos basados en coincidencias.
"""

# Diccionario que representa la base de conocimientos (reglas)
# Cada regla está asociada a una enfermedad y una lista de síntomas requeridos
base_conocimiento = {
    "Gripe": ["fiebre", "dolor de cabeza", "congestion nasal"],
    "Resfriado": ["estornudos", "congestion nasal", "dolor de garganta"],
    "COVID-19": ["fiebre", "tos seca", "perdida del olfato"],
    "Alergia": ["estornudos", "ojos llorosos", "picazon en la nariz"]
}

def diagnosticar(sintomas, umbral=2):
    """
    Diagnostica posibles enfermedades basadas en los síntomas proporcionados.

    Args:
        sintomas (list): Lista de síntomas reportados por el usuario.
        umbral (int): Número mínimo de coincidencias para considerar un diagnóstico.

    Returns:
        list: Lista de tuplas con posibles diagnósticos y número de coincidencias.
    """
    print("Evaluando síntomas...")
    posibles_diagnosticos = []

    for enfermedad, sintomas_necesarios in base_conocimiento.items():
        # Contamos cuántos síntomas coinciden con la base
        coincidencias = sum(1 for s in sintomas if s in sintomas_necesarios)

        # Si las coincidencias alcanzan el umbral, lo consideramos como posible diagnóstico
        if coincidencias >= umbral:
            posibles_diagnosticos.append((enfermedad, coincidencias, sintomas_necesarios))

    # Ordenamos por número de coincidencias (de mayor a menor)
    posibles_diagnosticos.sort(key=lambda x: x[1], reverse=True)

    return posibles_diagnosticos

def mostrar_diagnosticos(diagnosticos, sintomas_usuario):
    """
    Muestra los diagnósticos posibles al usuario.

    Args:
        diagnosticos (list): Lista de posibles diagnósticos.
        sintomas_usuario (list): Lista de síntomas reportados por el usuario.
    """
    if diagnosticos:
        print("\nDiagnóstico(s) posible(s):")
        for enfermedad, coincidencias, sintomas_necesarios in diagnosticos:
            sintomas_coincidentes = [s for s in sintomas_usuario if s in sintomas_necesarios]
            sintomas_faltantes = [s for s in sintomas_necesarios if s not in sintomas_usuario]
            print(f"- {enfermedad} (coincidencias: {coincidencias})")
            print(f"  Síntomas coincidentes: {', '.join(sintomas_coincidentes)}")
            print(f"  Síntomas faltantes: {', '.join(sintomas_faltantes)}")
    else:
        print("No se encontró un diagnóstico claro con los síntomas proporcionados.")

def mostrar_sintomas_disponibles():
    """
    Muestra al usuario un listado de los síntomas disponibles en la base de conocimiento.
    """
    print("Lista de síntomas disponibles:")
    sintomas_disponibles = set(sintoma for sintomas in base_conocimiento.values() for sintoma in sintomas)
    print(", ".join(sintomas_disponibles))
    print("\nPor favor, ingrese los síntomas de la lista anterior.")

def solicitar_sintomas():
    """
    Solicita al usuario que ingrese sus síntomas uno por uno.

    Returns:
        list: Lista de síntomas ingresados por el usuario.
    """
    print("Ingrese sus síntomas uno por uno. Escriba 'listo' para finalizar.")
    sintomas = []
    while True:
        sintoma = input("Ingrese un síntoma: ").strip().lower()
        if sintoma == "listo":
            break
        elif sintoma:
            sintomas.append(sintoma)
        else:
            print("Por favor, ingrese un síntoma válido.")
    return sintomas

# Mostrar los síntomas disponibles al usuario
mostrar_sintomas_disponibles()

# Solicitar síntomas al usuario
sintomas_usuario = solicitar_sintomas()

# Ejecutamos el diagnóstico
diagnosticos = diagnosticar(sintomas_usuario)

# Mostramos los resultados
mostrar_diagnosticos(diagnosticos, sintomas_usuario)

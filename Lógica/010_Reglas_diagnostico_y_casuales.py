# Sistema de diagnóstico basado en reglas causales

# Datos del paciente: síntomas observados
# Este diccionario contiene los síntomas que presenta el paciente.
paciente = {
    "fiebre": True,             # El paciente tiene fiebre
    "dolor_cabeza": True,       # El paciente tiene dolor de cabeza
    "congestion_nasal": True,   # El paciente tiene congestión nasal
    "dolor_garganta": False,    # El paciente NO tiene dolor de garganta
    "dolor_muscular": True      # El paciente tiene dolor muscular
}

# Validar que el paciente tenga todos los síntomas necesarios
# Esta función verifica que el diccionario del paciente contenga todas las claves requeridas.
def validar_datos_paciente(paciente):
    # Lista de síntomas que deben estar presentes en los datos del paciente
    sintomas_requeridos = ["fiebre", "dolor_cabeza", "congestion_nasal", "dolor_garganta", "dolor_muscular"]
    for sintoma in sintomas_requeridos:
        # Si falta algún síntoma, se lanza una excepción
        if sintoma not in paciente:
            raise ValueError(f"Falta el síntoma '{sintoma}' en los datos del paciente.")

# Reglas de diagnóstico
# Cada regla representa una condición que, si se cumple, sugiere un posible diagnóstico.

def regla_gripe(paciente):
    """
    Regla 1: SI fiebre Y dolor muscular Y dolor de cabeza → ENTONCES puede ser gripe
    """
    if paciente["fiebre"] and paciente["dolor_muscular"] and paciente["dolor_cabeza"]:
        return "Posible diagnóstico: Gripe"  # Diagnóstico basado en los síntomas
    return None  # Si no se cumple la regla, no se devuelve diagnóstico

def regla_resfriado(paciente):
    """
    Regla 2: SI congestión nasal Y dolor de garganta Y NO fiebre → ENTONCES puede ser resfriado
    """
    if paciente["congestion_nasal"] and paciente["dolor_garganta"] and not paciente["fiebre"]:
        return "Posible diagnóstico: Resfriado común"
    return None

def regla_alergia(paciente):
    """
    Regla 3: SI solo hay congestión nasal → ENTONCES puede ser alergia
    """
    if paciente["congestion_nasal"] and not paciente["fiebre"] and not paciente["dolor_cabeza"]:
        return "Posible diagnóstico: Alergia"
    return None

# Función principal de diagnóstico
# Esta función aplica todas las reglas al paciente y determina un diagnóstico.
def diagnostico(paciente):
    # Validar que los datos del paciente sean correctos
    validar_datos_paciente(paciente)
    
    # Lista de reglas a aplicar
    reglas = [regla_gripe, regla_resfriado, regla_alergia]
    
    # Iterar sobre cada regla y aplicarla al paciente
    for regla in reglas:
        resultado = regla(paciente)  # Evaluar la regla
        if resultado:
            # Si la regla devuelve un diagnóstico, se imprime y se detiene el proceso
            print(resultado)
            return
    
    # Si ninguna regla se cumple, se sugiere una revisión médica
    print("Diagnóstico incierto. Se recomienda revisión médica.")

# Ejecutar el diagnóstico
# Este bloque se ejecuta solo si el archivo se ejecuta directamente (no si se importa como módulo).
if __name__ == "__main__":
    print("Iniciando diagnóstico del paciente...")
    diagnostico(paciente)  # Llamar a la función principal de diagnóstico

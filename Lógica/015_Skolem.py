# ----------------------------
# Skolemización y Resolución Simulada
# ----------------------------

# Ejemplo: Fórmula lógica antes de Skolemizar
# ∀x (ama(x, pareja_de(x))) ∧ ∃y (ama(ana, y))
# Tras Skolemización:
# ∀x (ama(x, pareja_de(x))) ∧ ama(ana, f(ana))
# Nota: La Skolemización elimina los cuantificadores existenciales (∃) reemplazándolos
# por funciones de Skolem, que dependen de las variables universales (si las hay).

# Base de datos de relaciones 'ama(x, y)' tras Skolemización
# Supongamos que f(x) = pareja_de(x), donde pareja_de(x) devuelve a quién ama 'x'.
parejas = {
    "ana": "juan",      # Ana ama a Juan
    "carlos": "laura",  # Carlos ama a Laura
    "marcos": "sandra"  # Marcos ama a Sandra
}

# Función Skolem: devuelve a quién ama una persona
# Esta función simula la función de Skolem f(x) que asigna una pareja a cada persona.
def pareja_de(x):
    # Busca en el diccionario 'parejas' el valor asociado a la clave 'x'.
    # Si no encuentra la clave, devuelve "desconocido".
    return parejas.get(x, "desconocido")

# Predicado ama(x, y): verifica si 'x' ama a 'y' usando la función de Skolem
def ama(x, y):
    # Compara si la pareja asignada a 'x' (por pareja_de) es igual a 'y'.
    return pareja_de(x) == y

# Lista de personas para realizar las comprobaciones
personas = ["ana", "carlos", "marcos", "luis"]  # Incluye a 'luis', que no tiene pareja definida.

# Comprobaciones individuales: verificamos para cada persona si ama a su pareja
print("Comprobaciones individuales:")
for p in personas:
    # Obtenemos la pareja de 'p' usando la función de Skolem
    skolem_y = pareja_de(p)
    # Verificamos si 'p' ama a su pareja
    print(f"{p} ama a {skolem_y}? -> {ama(p, skolem_y)}")

# Función para resolver si existe alguna 'y' tal que ama(x, y)
# Esto corresponde a la fórmula lógica ∃y ama(x, y) antes de Skolemizar.
def existe_alguien_que_ama(x):
    # Si la función pareja_de(x) no devuelve "desconocido", significa que 'x' ama a alguien.
    return pareja_de(x) != "desconocido"

# Comprobamos para cada persona si existe alguien a quien ame
print("\nResolviendo ∃y ama(x, y):")
for p in personas:
    print(f"¿Existe alguien que {p} ame? -> {existe_alguien_que_ama(p)}")

# Ejemplo de resolución lógica:
# Queremos demostrar si ∀x ama(x, pareja_de(x)) es verdadero.
# Esto significa que todas las personas en la lista 'personas' aman a su pareja.
def verificar_todos_aman_a_su_pareja():
    # Iteramos sobre cada persona en la lista
    for p in personas:
        # Si alguna persona no ama a su pareja, devolvemos False
        if not ama(p, pareja_de(p)):
            return False
    # Si todas las personas aman a su pareja, devolvemos True
    return True

# Verificamos si todos aman a su pareja
print("\nResolviendo ∀x ama(x, pareja_de(x)):")
print(f"¿Todos aman a su pareja? -> {verificar_todos_aman_a_su_pareja()}")

# Agregamos más relaciones para ilustrar mejor el concepto
parejas.update({
    "luis": "maria",  # Agregamos una nueva relación: Luis ama a María
    "laura": "carlos"  # Relación inversa: Laura ama a Carlos
})

# Mostramos las nuevas relaciones añadidas
print("\nNuevas relaciones añadidas:")
for p, pareja in parejas.items():
    print(f"{p} ama a {pareja}")

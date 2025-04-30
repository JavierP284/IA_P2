# ---------------------------------------------------------
# Ejemplo de SATPLAN: Apagar una luz (con PySAT)
# ---------------------------------------------------------

# Importamos las librerías necesarias de PySAT
from pysat.solvers import Glucose3  # SAT solver que usaremos para resolver el problema
from pysat.formula import CNF  # Clase para manejar fórmulas en forma normal conjuntiva (CNF)

# ---------------------------------------------------------
# Función para interpretar y mostrar el modelo de verdad
# ---------------------------------------------------------
# Esta función toma como entrada el modelo de verdad (una lista de enteros)
# y traduce las variables proposicionales a un formato más entendible.
def interpretar_modelo(modelo):
    print("Modelo de verdad:")
    for var in sorted(modelo, key=abs):  # Ordenamos las variables por su valor absoluto
        if abs(var) == 1:
            print(f"  luz_encendida_t0: {'T' if var > 0 else 'F'}")  # Variable 1 representa luz encendida en t0
        elif abs(var) == 2:
            print(f"  apagar_t0: {'T' if var > 0 else 'F'}")  # Variable 2 representa la acción de apagar en t0
        elif abs(var) == 3:
            print(f"  luz_encendida_t1: {'T' if var > 0 else 'F'}")  # Variable 3 representa luz encendida en t1

# ---------------------------------------------------------
# Paso 1: Crear la fórmula CNF
# ---------------------------------------------------------
# Creamos una instancia de CNF para almacenar las cláusulas de la fórmula
cnf = CNF()

# Estado inicial: la luz está encendida en t0
# Esto se representa con la variable 1 (luz_encendida_t0) siendo verdadera.
cnf.append([1])  # luz_encendida_t0

# Acción "apagar" en t0 solo puede ocurrir si la luz estaba encendida en t0
# Esto se traduce como: ¬apagar_t0 ∨ luz_encendida_t0
# Si intentamos apagar la luz (apagar_t0), la luz debe estar encendida en t0.
cnf.append([-2, 1])  # ¬apagar ∨ luz_encendida_t0

# Efecto de "apagar" en t0: si se apaga la luz en t0, entonces no estará encendida en t1
# Esto se traduce como: ¬apagar_t0 ∨ ¬luz_encendida_t1
# Si apagamos la luz (apagar_t0), la luz no puede estar encendida en t1.
cnf.append([-2, -3])  # ¬apagar ∨ ¬luz_encendida_t1

# Persistencia: si la luz estaba encendida en t0 y no se apaga, sigue encendida en t1
# Esto se traduce como: ¬luz_encendida_t0 ∨ apagar_t0 ∨ luz_encendida_t1
# Si la luz estaba encendida en t0 y no la apagamos, entonces debe seguir encendida en t1.
cnf.append([-1, 2, 3])  # ¬luz_t0 ∨ apagar ∨ luz_t1

# Objetivo: la luz debe estar apagada en t1
# Esto se traduce como: ¬luz_encendida_t1
# Queremos que la luz no esté encendida en t1.
cnf.append([-3])  # ¬luz_encendida_t1

# ---------------------------------------------------------
# Paso 2: Resolver con SAT solver
# ---------------------------------------------------------
# Creamos una instancia del solver Glucose3
solver = Glucose3()

# Añadimos la fórmula CNF al solver
solver.append_formula(cnf)

# Intentamos resolver el problema
print("Resolviendo el problema de planificación...\n")
if solver.solve():  # Si el solver encuentra una solución
    print("¡Plan encontrado!\n")
    interpretar_modelo(solver.get_model())  # Interpretamos y mostramos el modelo de verdad
else:  # Si no hay solución
    print("No hay plan posible para alcanzar el objetivo.")

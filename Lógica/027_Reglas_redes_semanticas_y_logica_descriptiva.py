# -----------------------------------------------
# Redes Semánticas + Reglas + Lógica Descriptiva
# -----------------------------------------------

# Red semántica ampliada
# Representa una jerarquía de conceptos y sus propiedades.
# Cada nodo tiene un conjunto de propiedades que describen sus características.
red_semantica = {
    "animal": {"es_un": None},  # Nodo raíz, no pertenece a ninguna categoría superior.
    "mamifero": {"es_un": "animal"},  # Los mamíferos son animales.
    "ave": {"es_un": "animal", "puede_volar": True},  # Las aves son animales y, por defecto, pueden volar.
    "perro": {"es_un": "mamifero", "es_domestico": True},  # Los perros son mamíferos y domésticos.
    "gato": {"es_un": "mamifero", "es_domestico": True},  # Los gatos son mamíferos y domésticos.
    "aguila": {"es_un": "ave", "puede_volar": True},  # Las águilas son aves y pueden volar.
    "pinguino": {"es_un": "ave", "puede_volar": False},  # Los pingüinos son aves, pero no pueden volar.
    "pez": {"es_un": "animal", "puede_nadar": True},  # Los peces son animales y pueden nadar.
    "delfin": {"es_un": "mamifero", "puede_nadar": True}  # Los delfines son mamíferos y pueden nadar.
}

# -----------------------------------------------
# Motor de Inferencia basado en Reglas
# -----------------------------------------------
# Este motor aplica reglas para inferir nuevas propiedades en los nodos.

# Regla: Si algo es un ave, entonces puede volar (si no se sabe lo contrario).
# Esta regla se aplica solo si la propiedad "puede_volar" no está definida explícitamente.
def regla_aves_pueden_volar(nodo):
    if "es_un" in red_semantica[nodo] and red_semantica[nodo]["es_un"] == "ave":
        if "puede_volar" not in red_semantica[nodo]:  # Solo aplica si no está definido.
            red_semantica[nodo]["puede_volar"] = True
            print(f"Regla aplicada: {nodo} ahora puede volar.")

# Regla: Si algo es doméstico y un animal, entonces puede ser una mascota.
# Esta regla agrega la propiedad "es_mascota" a los nodos que cumplen las condiciones.
def regla_domestico_es_mascota(nodo):
    if ("es_un" in red_semantica[nodo] and 
        red_semantica[nodo]["es_un"] == "animal" and  # Debe ser un animal.
        red_semantica[nodo].get("es_domestico", False)):  # Debe ser doméstico.
        red_semantica[nodo]["es_mascota"] = True
        print(f"Regla aplicada: {nodo} puede ser una mascota.")

# Regla: Si algo es un mamífero, entonces no puede volar (por defecto).
# Esta regla se aplica solo si la propiedad "puede_volar" no está definida explícitamente.
def regla_mamiferos_no_vuelan(nodo):
    if "es_un" in red_semantica[nodo] and red_semantica[nodo]["es_un"] == "mamifero":
        if "puede_volar" not in red_semantica[nodo]:  # Solo aplica si no está definido.
            red_semantica[nodo]["puede_volar"] = False
            print(f"Regla aplicada: {nodo} no puede volar.")

# Función para aplicar todas las reglas de inferencia.
# Recorre todos los nodos de la red semántica y aplica cada regla.
def aplicar_reglas():
    for nodo in red_semantica.keys():  # Itera sobre todos los nodos de la red.
        regla_aves_pueden_volar(nodo)  # Aplica la regla de las aves.
        regla_domestico_es_mascota(nodo)  # Aplica la regla de los animales domésticos.
        regla_mamiferos_no_vuelan(nodo)  # Aplica la regla de los mamíferos.

# -----------------------------------------------
# Consultar propiedades de un nodo (lógica descriptiva)
# -----------------------------------------------
# Permite consultar las propiedades de un nodo específico en la red semántica.

def describir_nodo(nodo):
    if nodo in red_semantica:  # Verifica si el nodo existe en la red.
        print(f"\nPropiedades de {nodo}:")
        for prop, valor in red_semantica[nodo].items():  # Itera sobre las propiedades del nodo.
            print(f" - {prop}: {valor}")  # Muestra cada propiedad y su valor.
    else:
        print(f"Nodo '{nodo}' no encontrado en la red.")  # Mensaje si el nodo no existe.

# -----------------------------------------------
# Ejecución
# -----------------------------------------------
# Aquí se ejecuta el motor de inferencia y se realizan consultas.

# Aplicamos reglas de inferencia para actualizar la red semántica.
print("Aplicando reglas de inferencia...")
aplicar_reglas()

# Consultamos las propiedades de algunos nodos para verificar los resultados.
describir_nodo("perro")  # Consulta las propiedades del nodo "perro".
describir_nodo("aguila")  # Consulta las propiedades del nodo "aguila".
describir_nodo("pinguino")  # Consulta las propiedades del nodo "pinguino".

# --------------------------------------------
# Ontología simple en Python (simulada)
# --------------------------------------------

# Clase base: Animal
class Animal:
    """
    Clase base para representar un animal en la ontología.
    Cada animal tiene un nombre y un conjunto de propiedades.
    """
    def __init__(self, nombre):
        # Inicializa el nombre del animal y un diccionario para sus propiedades
        self.nombre = nombre
        self.propiedades = {}

    def agregar_propiedad(self, propiedad, valor):
        """
        Agrega una propiedad al animal.
        :param propiedad: Nombre de la propiedad.
        :param valor: Valor de la propiedad.
        """
        # Añade una nueva propiedad al diccionario de propiedades
        self.propiedades[propiedad] = valor

    def tiene_propiedad(self, propiedad):
        """
        Verifica si el animal tiene una propiedad específica.
        :param propiedad: Nombre de la propiedad.
        :return: Valor de la propiedad o None si no existe.
        """
        # Devuelve el valor de la propiedad si existe, o None si no está definida
        return self.propiedades.get(propiedad, None)

# Subclase Mamífero
class Mamifero(Animal):
    def __init__(self, nombre):
        # Llama al constructor de la clase base (Animal)
        super().__init__(nombre)
        # Agrega una propiedad específica para los mamíferos
        self.agregar_propiedad("tiene_pelo", True)

# Subclase Ave
class Ave(Animal):
    def __init__(self, nombre):
        # Llama al constructor de la clase base (Animal)
        super().__init__(nombre)
        # Agrega una propiedad específica para las aves
        self.agregar_propiedad("tiene_plumas", True)

# Clase para manejar la ontología
class Ontologia:
    """
    Clase para manejar la ontología y realizar consultas.
    """
    def __init__(self):
        # Inicializa una lista vacía para almacenar los individuos
        self.individuos = []

    def agregar_individuo(self, individuo):
        """
        Agrega un individuo a la ontología.
        :param individuo: Instancia de la clase Animal o sus subclases.
        """
        # Añade un nuevo individuo a la lista de la ontología
        self.individuos.append(individuo)

    def consultar(self, propiedad, valor=None):
        """
        Realiza una consulta sobre los individuos de la ontología.
        :param propiedad: Propiedad a consultar.
        :param valor: Valor esperado de la propiedad (opcional).
        """
        print(f"\nConsulta: Animales con '{propiedad}' = {valor}")
        # Filtra los individuos que cumplen con la propiedad y el valor especificado
        encontrados = [a.nombre for a in self.individuos if a.propiedades.get(propiedad) == valor]
        if encontrados:
            # Muestra los nombres de los animales encontrados
            print(f"Resultado: {', '.join(encontrados)}")
        else:
            # Indica que no se encontraron resultados
            print("No se encontraron animales que cumplan con la consulta.")

# Creamos instancias de la ontología
ontologia = Ontologia()

# Creamos instancias de animales y les asignamos propiedades
perro = Mamifero("Perro")
perro.agregar_propiedad("vuela", False)
perro.agregar_propiedad("es_domestico", True)
perro.agregar_propiedad("tiene_patas", 4)

gato = Mamifero("Gato")
gato.agregar_propiedad("vuela", False)
gato.agregar_propiedad("es_domestico", True)
gato.agregar_propiedad("tiene_patas", 4)

aguila = Ave("Águila")
aguila.agregar_propiedad("vuela", True)
aguila.agregar_propiedad("es_domestico", False)
aguila.agregar_propiedad("tiene_patas", 2)

pez = Animal("Pez")
pez.agregar_propiedad("vuela", False)
pez.agregar_propiedad("es_domestico", False)
pez.agregar_propiedad("vive_en_agua", True)

loro = Ave("Loro")
loro.agregar_propiedad("vuela", True)
loro.agregar_propiedad("es_domestico", True)
loro.agregar_propiedad("tiene_patas", 2)

# Agregamos los individuos a la ontología
ontologia.agregar_individuo(perro)
ontologia.agregar_individuo(gato)
ontologia.agregar_individuo(aguila)
ontologia.agregar_individuo(pez)
ontologia.agregar_individuo(loro)

# Interfaz de usuario para realizar consultas
while True:
    # Muestra las opciones disponibles para el usuario
    print("\nOpciones de consulta:")
    print("1. ¿Qué animales vuelan?")
    print("2. ¿Qué animales son domésticos?")
    print("3. ¿Qué animales tienen 4 patas?")
    print("4. ¿Qué animales viven en el agua?")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    # Realiza la consulta correspondiente según la opción seleccionada
    if opcion == "1":
        ontologia.consultar("vuela", True)
    elif opcion == "2":
        ontologia.consultar("es_domestico", True)
    elif opcion == "3":
        ontologia.consultar("tiene_patas", 4)
    elif opcion == "4":
        ontologia.consultar("vive_en_agua", True)
    elif opcion == "5":
        # Finaliza el programa
        print("Saliendo del programa...")
        break
    else:
        # Maneja opciones no válidas
        print("Opción no válida. Intente de nuevo.")

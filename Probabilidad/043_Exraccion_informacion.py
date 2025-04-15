import spacy

# ----- Paso 1: Cargar el modelo de lenguaje en español -----
# Este modelo ya sabe detectar entidades en español como personas, lugares, fechas, etc.
# Asegúrate de haber instalado el modelo con: python -m spacy download es_core_news_sm
nlp = spacy.load("es_core_news_sm")

# ----- Paso 2: Definir una función para procesar texto -----
def extraer_entidades(texto):
    """
    Procesa el texto de entrada y extrae las entidades nombradas.
    """
    # Procesar el texto con spaCy
    doc = nlp(texto)

    # Mostrar las entidades reconocidas
    print("Entidades nombradas encontradas:\n")
    for ent in doc.ents:
        # Mostrar el texto de la entidad y su tipo
        print(f"Texto: {ent.text} → Tipo: {ent.label_}")

    # Explicación adicional de los tipos de entidades
    print("\nTipos de entidades comunes:")
    print("PER: Persona, LOC: Lugar, ORG: Organización, DATE: Fecha, MISC: Misceláneo")

# ----- Paso 3: Texto de entrada -----
texto = """
Lionel Messi nació en Rosario, Argentina, el 24 de junio de 1987.
Actualmente juega para el Inter de Miami en la MLS.
Ganó la Copa del Mundo con la selección de Argentina en Qatar 2022.
"""

# ----- Paso 4: Llamar a la función para extraer entidades -----
extraer_entidades(texto)

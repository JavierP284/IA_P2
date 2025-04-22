# Sistema experto mejorado para recomendar cultivos agrícolas

# Paso 1: Base de conocimientos (reglas)
# Cada regla contiene las condiciones necesarias (humedad, tipo de suelo, clima)
# y el cultivo recomendado para esas condiciones.
reglas = [
    {"condiciones": {"humedad": "alta", "suelo": "arcilloso", "clima": "tropical"}, "cultivo": "Arroz"},
    {"condiciones": {"humedad": "media", "suelo": "arenoso", "clima": "templado"}, "cultivo": "Maíz"},
    {"condiciones": {"humedad": "baja", "suelo": "pedregoso", "clima": "seco"}, "cultivo": "Cactus"},
    {"condiciones": {"humedad": "alta", "suelo": "limoso", "clima": "templado"}, "cultivo": "Plátano"},
]

# Paso 2: Función para obtener datos del usuario
# Esta función solicita al usuario que ingrese las condiciones del terreno.
# Los datos ingresados se normalizan (se convierten a minúsculas y se eliminan espacios).
def obtener_datos_usuario():
    print("Por favor, ingresa las condiciones del terreno:")
    humedad = input("Humedad (alta/media/baja): ").strip().lower()  # Solicita la humedad
    suelo = input("Tipo de suelo (arcilloso/arenoso/pedregoso/limoso): ").strip().lower()  # Solicita el tipo de suelo
    clima = input("Clima (tropical/templado/seco): ").strip().lower()  # Solicita el clima
    # Devuelve un diccionario con las condiciones ingresadas
    return {"humedad": humedad, "suelo": suelo, "clima": clima}

# Paso 3: Motor de inferencia
# Esta función analiza las condiciones del terreno proporcionadas por el usuario
# y determina el cultivo más adecuado según las reglas definidas.
def recomendar_cultivo(terreno):
    print("\nAnalizando condiciones del terreno...")
    # Recorremos cada regla en la base de conocimientos
    for regla in reglas:
        condiciones = regla["condiciones"]  # Extraemos las condiciones de la regla actual
        # Verificamos si todas las condiciones coinciden exactamente con las ingresadas por el usuario
        if condiciones == terreno:
            print(f"Recomendación: Puedes sembrar {regla['cultivo']}")  # Cultivo recomendado
            print(f"Explicación: Basado en las condiciones {condiciones}.")  # Explicación de la recomendación
            return  # Terminamos la función si encontramos una coincidencia exacta

    # Si no hay coincidencia exacta, buscamos coincidencias parciales
    print("No se encontró una recomendación exacta. Buscando coincidencias parciales...")
    recomendaciones_parciales = []  # Lista para almacenar coincidencias parciales

    # Recorremos nuevamente las reglas para evaluar coincidencias parciales
    for regla in reglas:
        # Contamos cuántas condiciones coinciden entre las ingresadas y las de la regla actual
        coincidencias = sum(1 for key in terreno if terreno[key] == regla["condiciones"][key])
        if coincidencias > 0:  # Si hay al menos una coincidencia
            recomendaciones_parciales.append((regla["cultivo"], coincidencias))  # Guardamos el cultivo y el número de coincidencias

    # Si hay coincidencias parciales, las ordenamos por relevancia (mayor número de coincidencias primero)
    if recomendaciones_parciales:
        recomendaciones_parciales.sort(key=lambda x: x[1], reverse=True)  # Orden descendente por coincidencias
        print("Recomendaciones basadas en coincidencias parciales:")
        # Mostramos las recomendaciones parciales al usuario
        for cultivo, coincidencias in recomendaciones_parciales:
            print(f"- {cultivo} (coincidencias: {coincidencias})")
    else:
        # Si no hay coincidencias parciales, informamos al usuario
        print("No se encontraron recomendaciones. Consulta a un experto.")

# Paso 4: Ejecución del sistema experto
# Esta función principal coordina la ejecución del sistema experto.
def main():
    print("Sistema experto: Recomendador de cultivos")  # Mensaje de bienvenida
    terreno = obtener_datos_usuario()  # Obtenemos las condiciones del terreno del usuario
    recomendar_cultivo(terreno)  # Llamamos al motor de inferencia para obtener una recomendación

# Punto de entrada del programa
if __name__ == "__main__":
    main()  # Ejecutamos la función principal

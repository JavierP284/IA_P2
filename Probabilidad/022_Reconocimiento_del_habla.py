import speech_recognition as sr  # Importar la biblioteca para reconocimiento de voz

# -------------------------------
# 1. Crear un reconocedor de voz
# -------------------------------
# El objeto 'Recognizer' se utiliza para procesar y reconocer el audio
reconocedor = sr.Recognizer()

# -------------------------------
# 2. Usar el micrófono como fuente de audio
# -------------------------------
try:
    # Verificar si hay un micrófono disponible en el sistema
    if not sr.Microphone.list_microphone_names():
        print("No se detectó ningún micrófono. Por favor, conecta uno e intenta de nuevo.")
        exit()  # Salir del programa si no hay micrófono disponible

    # Usar el micrófono como fuente de entrada de audio
    with sr.Microphone() as fuente:
        # Ajustar el ruido ambiental para mejorar la precisión del reconocimiento
        print("Ajustando al ruido ambiental... Por favor, espera.")
        reconocedor.adjust_for_ambient_noise(fuente, duration=1)

        # Indicar al usuario que hable para capturar su voz
        print("Habla ahora (esperando entrada de voz)...")
        audio = reconocedor.listen(fuente)  # Escuchar la entrada de voz del usuario

    # -------------------------------
    # 3. Intentar reconocer el texto usando Google
    # -------------------------------
    try:
        # Usar el servicio de Google para convertir el audio en texto
        # El idioma está configurado en español (es-ES)
        texto = reconocedor.recognize_google(audio, language="es-ES")
        print("Texto reconocido:", texto)  # Mostrar el texto reconocido en la consola

        # Guardar el texto reconocido en un archivo de texto
        with open("texto_reconocido.txt", "w", encoding="utf-8") as archivo:
            archivo.write(texto)  # Escribir el texto en el archivo
        print("El texto reconocido se ha guardado en 'texto_reconocido.txt'.")

    # Manejar el caso en que no se pueda entender el audio
    except sr.UnknownValueError:
        print("No se pudo entender el audio. Por favor, intenta de nuevo.")

    # Manejar errores relacionados con la conexión al servicio de Google
    except sr.RequestError as e:
        print(f"Error al conectarse con el servicio de Google: {e}")

# Manejar errores relacionados con el acceso al micrófono
except OSError as e:
    print(f"Error al acceder al micrófono: {e}")

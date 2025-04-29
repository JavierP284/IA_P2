import matplotlib.pyplot as plt

# -------------------------------------------
# Conjuntos Difusos: Clasificación de temperatura
# Este programa utiliza lógica difusa para clasificar temperaturas
# en tres categorías: "Fría", "Templada" y "Caliente".
# Cada categoría tiene una función de pertenencia que determina
# el grado de pertenencia de una temperatura a esa categoría.
# -------------------------------------------

# Función de pertenencia al conjunto "Fría"
# Devuelve el grado de pertenencia de una temperatura al conjunto "Fría".
def temperatura_fria(temp):
    if temp <= 10:
        return 1.0  # Pertenencia total si la temperatura es menor o igual a 10°C
    elif 10 < temp <= 20:
        return (20 - temp) / 10  # Pertenencia decrece linealmente de 1 a 0 entre 10°C y 20°C
    else:
        return 0.0  # No pertenece al conjunto "Fría" si la temperatura es mayor a 20°C

# Función de pertenencia al conjunto "Templada"
# Devuelve el grado de pertenencia de una temperatura al conjunto "Templada".
def temperatura_templada(temp):
    if 15 < temp < 25:
        return (temp - 15) / 10  # Pertenencia sube linealmente de 0 a 1 entre 15°C y 25°C
    elif 25 <= temp <= 30:
        return (30 - temp) / 5   # Pertenencia baja linealmente de 1 a 0 entre 25°C y 30°C
    else:
        return 0.0  # No pertenece al conjunto "Templada" fuera de este rango

# Función de pertenencia al conjunto "Caliente"
# Devuelve el grado de pertenencia de una temperatura al conjunto "Caliente".
def temperatura_caliente(temp):
    if temp <= 25:
        return 0.0  # No pertenece al conjunto "Caliente" si la temperatura es menor o igual a 25°C
    elif 25 < temp < 35:
        return (temp - 25) / 10  # Pertenencia sube linealmente de 0 a 1 entre 25°C y 35°C
    else:
        return 1.0  # Pertenencia total si la temperatura es mayor o igual a 35°C

# -------------------------------------------
# Evaluar una temperatura dada
# Esta función evalúa una temperatura específica y calcula
# el grado de pertenencia a cada conjunto difuso.
def evaluar_temperatura(temp):
    print(f"\nEvaluando temperatura: {temp}°C")

    # Calcular el grado de pertenencia a cada conjunto
    fria = round(temperatura_fria(temp), 2)
    templada = round(temperatura_templada(temp), 2)
    caliente = round(temperatura_caliente(temp), 2)

    # Mostrar los resultados
    print(f" - Pertenencia a FRÍA     : {fria}")
    print(f" - Pertenencia a TEMPLADA : {templada}")
    print(f" - Pertenencia a CALIENTE : {caliente}")

    # Devolver los resultados como un diccionario
    return {"Fría": fria, "Templada": templada, "Caliente": caliente}

# -------------------------------------------
# Graficar funciones de pertenencia
# Esta función genera una gráfica que muestra las funciones de pertenencia
# para los conjuntos "Fría", "Templada" y "Caliente" en un rango de temperaturas.
def graficar_funciones():
    # Crear un rango de temperaturas de 0°C a 40°C
    temperaturas = [i for i in range(0, 41)]
    
    # Calcular los grados de pertenencia para cada conjunto
    fria = [temperatura_fria(t) for t in temperaturas]
    templada = [temperatura_templada(t) for t in temperaturas]
    caliente = [temperatura_caliente(t) for t in temperaturas]

    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(temperaturas, fria, label="Fría", color="blue")  # Línea azul para "Fría"
    plt.plot(temperaturas, templada, label="Templada", color="green")  # Línea verde para "Templada"
    plt.plot(temperaturas, caliente, label="Caliente", color="red")  # Línea roja para "Caliente"
    plt.title("Funciones de Pertenencia de Temperatura")  # Título de la gráfica
    plt.xlabel("Temperatura (°C)")  # Etiqueta del eje X
    plt.ylabel("Grado de Pertenencia")  # Etiqueta del eje Y
    plt.legend()  # Mostrar la leyenda
    plt.grid(True)  # Mostrar la cuadrícula
    plt.show()  # Mostrar la gráfica

# -------------------------------------------
# Probar con distintas temperaturas
# Punto de entrada principal del programa
if __name__ == "__main__":
    # Graficar las funciones de pertenencia
    graficar_funciones()

    # Permitir al usuario evaluar temperaturas ingresadas manualmente
    while True:
        try:
            # Solicitar al usuario una temperatura
            temp = float(input("\nIngrese una temperatura para evaluar (o 'q' para salir): "))
            # Evaluar la temperatura ingresada
            evaluar_temperatura(temp)
        except ValueError:
            # Salir del programa si el usuario ingresa algo no válido
            print("Saliendo del programa.")
            break

import numpy as np
import matplotlib.pyplot as plt

# -------- Función para visualizar patrones (5x5) --------
def mostrar_patron(patron, titulo=""):
    """
    Muestra un patrón en una cuadrícula 5x5.
    :param patron: Vector de 25 elementos que representa el patrón.
    :param titulo: Título de la visualización.
    """
    plt.imshow(patron.reshape(5, 5), cmap='binary')  # Convierte el vector en una matriz 5x5
    plt.title(titulo)  # Agrega un título
    plt.axis('off')  # Oculta los ejes
    plt.show()  # Muestra la visualización

# -------- Patrones de entrenamiento (letras A y B) --------
# Los patrones están representados como vectores de 25 elementos con valores -1 y 1.
# Estos valores son necesarios para trabajar con redes de Hopfield y Boltzmann.
patron_A = np.array([
    -1,  1,  1,  1, -1,
     1, -1, -1, -1,  1,
     1,  1,  1,  1,  1,
     1, -1, -1, -1,  1,
     1, -1, -1, -1,  1
])

patron_B = np.array([
     1,  1,  1,  1, -1,
     1, -1, -1, -1,  1,
     1,  1,  1,  1, -1,
     1, -1, -1, -1,  1,
     1,  1,  1,  1, -1
])

# -------- Algoritmo de Hamming --------
def distancia_hamming(patron1, patron2):
    """
    Calcula la distancia de Hamming entre dos patrones.
    La distancia de Hamming es el número de posiciones en las que los valores son diferentes.
    :param patron1: Primer patrón (array).
    :param patron2: Segundo patrón (array).
    :return: Distancia de Hamming.
    """
    return np.sum(patron1 != patron2)  # Cuenta las posiciones donde los valores son diferentes

def ejemplo_hamming():
    """
    Ejemplo de cálculo de distancia de Hamming.
    """
    print("Ejemplo de Hamming:")
    print("Patrón A:")
    mostrar_patron(patron_A, titulo="Patrón A")  # Visualiza el patrón A
    print("Patrón B:")
    mostrar_patron(patron_B, titulo="Patrón B")  # Visualiza el patrón B

    # Calcular la distancia de Hamming entre los patrones A y B
    distancia = distancia_hamming(patron_A, patron_B)
    print(f"Distancia de Hamming entre A y B: {distancia}")  # Muestra el resultado

# -------- Máquina de Boltzmann --------
def energia_boltzmann(W, estado):
    """
    Calcula la energía de un estado en una Máquina de Boltzmann.
    La energía mide qué tan "estable" es un estado dado.
    :param W: Matriz de pesos (simétrica).
    :param estado: Vector de estado (patrón).
    :return: Energía del estado.
    """
    return -0.5 * np.dot(estado, np.dot(W, estado))  # Fórmula de energía de Boltzmann

def entrenar_boltzmann(patrones):
    """
    Entrena una Máquina de Boltzmann con una matriz de pesos simétrica.
    :param patrones: Lista de patrones de entrenamiento.
    :return: Matriz de pesos W.
    """
    n = len(patrones[0])  # Número de neuronas (tamaño del patrón)
    W = np.zeros((n, n))  # Inicializa la matriz de pesos con ceros
    for p in patrones:
        W += np.outer(p, p)  # Suma el producto externo de cada patrón consigo mismo
    np.fill_diagonal(W, 0)  # Elimina auto-conexiones (diagonal de la matriz)
    return W

def ejemplo_boltzmann():
    """
    Ejemplo de entrenamiento y cálculo de energía en una Máquina de Boltzmann.
    """
    print("Ejemplo de Máquina de Boltzmann:")
    patrones = [patron_A, patron_B]  # Lista de patrones de entrenamiento
    W = entrenar_boltzmann(patrones)  # Entrena la matriz de pesos

    # Mostrar y calcular la energía del patrón A
    print("Patrón A:")
    mostrar_patron(patron_A, titulo="Patrón A")
    energia_A = energia_boltzmann(W, patron_A)
    print(f"Energía del patrón A: {energia_A}")

    # Mostrar y calcular la energía del patrón B
    print("Patrón B:")
    mostrar_patron(patron_B, titulo="Patrón B")
    energia_B = energia_boltzmann(W, patron_B)
    print(f"Energía del patrón B: {energia_B}")

# -------- Red de Hopfield --------
def entrenar_hopfield(patrones):
    """
    Entrena una red de Hopfield usando la regla de Hebb.
    :param patrones: Lista de patrones de entrenamiento.
    :return: Matriz de pesos W.
    """
    n = len(patrones[0])  # Número de neuronas (tamaño del patrón)
    W = np.zeros((n, n))  # Inicializa la matriz de pesos con ceros
    for p in patrones:
        W += np.outer(p, p)  # Suma el producto externo de cada patrón consigo mismo
    np.fill_diagonal(W, 0)  # Elimina auto-conexiones (diagonal de la matriz)
    return W

def recuperar(W, entrada, iteraciones=10):
    """
    Recupera un patrón usando la red de Hopfield.
    :param W: Matriz de pesos entrenada.
    :param entrada: Patrón de entrada (con ruido).
    :param iteraciones: Número de iteraciones para actualizar el estado.
    :return: Patrón recuperado.
    """
    estado = entrada.copy()  # Copia el patrón de entrada
    for _ in range(iteraciones):  # Realiza varias iteraciones para estabilizar el estado
        for i in range(len(estado)):  # Actualiza cada neurona
            suma = np.dot(W[i], estado)  # Calcula la suma ponderada de las conexiones
            estado[i] = 1 if suma >= 0 else -1  # Actualiza el estado de la neurona
    return estado

def ejemplo_hopfield():
    """
    Ejemplo completo de entrenamiento y recuperación con la red de Hopfield.
    """
    patrones = [patron_A, patron_B]  # Lista de patrones de entrenamiento
    W = entrenar_hopfield(patrones)  # Entrena la matriz de pesos

    # Mostrar el patrón original A
    print("Patrón original A:")
    mostrar_patron(patron_A, titulo="Patrón Original A")

    # Crear un patrón con ruido (modificar algunos bits)
    patron_ruido = patron_A.copy()
    patron_ruido[3] = -patron_ruido[3]  # Invertir un bit
    patron_ruido[7] = -patron_ruido[7]  # Invertir otro bit

    print("Patrón con ruido:")
    mostrar_patron(patron_ruido, titulo="Patrón con Ruido")

    # Recuperar el patrón original usando la red de Hopfield
    patron_recuperado = recuperar(W, patron_ruido)
    print("Patrón recuperado:")
    mostrar_patron(patron_recuperado, titulo="Patrón Recuperado")

# -------- Menú principal --------
if __name__ == "__main__":
    print("Seleccione un ejemplo para ejecutar:")
    print("1. Red de Hopfield")
    print("2. Algoritmo de Hamming")
    print("3. Máquina de Boltzmann")
    opcion = input("Ingrese el número de la opción: ")

    if opcion == "1":
        ejemplo_hopfield()  # Ejecuta el ejemplo de Hopfield
    elif opcion == "2":
        ejemplo_hamming()  # Ejecuta el ejemplo de Hamming
    elif opcion == "3":
        ejemplo_boltzmann()  # Ejecuta el ejemplo de Boltzmann
    else:
        print("Opción no válida.")  # Maneja opciones no válidas

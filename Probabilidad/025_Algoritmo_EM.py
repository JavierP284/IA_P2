import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# -------------------------------
# 1. Generamos datos sintéticos
# -------------------------------

np.random.seed(42)  # Fijamos la semilla para reproducibilidad

# Creamos dos grupos de datos con distribuciones gaussianas
datos1 = np.random.normal(10, 2, 100)  # Grupo 1: media=10, desviación estándar=2
datos2 = np.random.normal(20, 3, 100)  # Grupo 2: media=20, desviación estándar=3
datos = np.hstack([datos1, datos2])    # Combinamos ambos grupos en un solo conjunto de datos

# Número de componentes gaussianos que queremos ajustar
K = 2

# -------------------------------
# 2. Algoritmo EM
# -------------------------------

def inicializar_parametros(datos, K):
    """
    Inicializa los parámetros del modelo:
    - Pesos: Inicialmente iguales para cada componente.
    - Medias: Seleccionadas aleatoriamente de los datos.
    - Desviaciones estándar: Valores aleatorios mayores a 1.
    """
    pesos = np.ones(K) / K  # Pesos iniciales iguales
    medias = np.random.choice(datos, K)  # Seleccionamos K valores aleatorios de los datos como medias iniciales
    desviaciones = np.random.random(K) + 1  # Desviaciones iniciales aleatorias mayores a 1
    return pesos, medias, desviaciones

def calcular_log_verosimilitud(datos, pesos, medias, desviaciones):
    """
    Calcula la log-verosimilitud del modelo.
    La log-verosimilitud mide qué tan bien el modelo ajusta los datos.
    """
    N = len(datos)  # Número de datos
    log_verosimilitud = 0
    for i in range(N):
        suma = 0
        for k in range(K):
            # Calculamos la probabilidad de cada dato bajo cada componente gaussiano
            suma += pesos[k] * norm.pdf(datos[i], medias[k], desviaciones[k])
        # Sumamos el logaritmo de las probabilidades
        log_verosimilitud += np.log(suma)
    return log_verosimilitud

def em_gmm(datos, K, max_iter=100, tol=1e-4):
    """
    Implementa el algoritmo EM para ajustar una mezcla de gaussianas.
    - E-step: Calcula las responsabilidades (probabilidades de pertenencia).
    - M-step: Actualiza los parámetros del modelo (pesos, medias, desviaciones).
    """
    N = len(datos)  # Número de datos
    # Inicializamos los parámetros
    pesos, medias, desviaciones = inicializar_parametros(datos, K)
    log_verosimilitudes = []  # Lista para almacenar la log-verosimilitud en cada iteración

    for iter in range(max_iter):
        # E-step: Calculamos las responsabilidades
        responsabilidades = np.zeros((N, K))  # Matriz de responsabilidades (N x K)
        for k in range(K):
            # Calculamos la probabilidad de cada dato bajo el componente k
            responsabilidades[:, k] = pesos[k] * norm.pdf(datos, medias[k], desviaciones[k])
        
        # Normalizamos las responsabilidades para que sumen 1 por fila
        sum_responsabilidades = np.sum(responsabilidades, axis=1).reshape(-1, 1)
        responsabilidades /= sum_responsabilidades

        # M-step: Actualizamos los parámetros usando las responsabilidades
        Nk = np.sum(responsabilidades, axis=0)  # Suma de responsabilidades para cada componente
        for k in range(K):
            # Actualizamos la media del componente k
            medias[k] = np.sum(responsabilidades[:, k] * datos) / Nk[k]
            # Actualizamos la desviación estándar del componente k
            desviaciones[k] = np.sqrt(np.sum(responsabilidades[:, k] * (datos - medias[k])**2) / Nk[k])
            # Actualizamos el peso del componente k
            pesos[k] = Nk[k] / N

        # Calculamos la log-verosimilitud del modelo
        log_verosimilitud = calcular_log_verosimilitud(datos, pesos, medias, desviaciones)
        log_verosimilitudes.append(log_verosimilitud)

        # Verificamos la convergencia
        if iter > 0 and abs(log_verosimilitudes[-1] - log_verosimilitudes[-2]) < tol:
            print(f"Convergencia alcanzada en la iteración {iter}")
            break

    return pesos, medias, desviaciones, responsabilidades, log_verosimilitudes

# Ejecutamos el algoritmo EM
pesos, medias, desviaciones, responsabilidades, log_verosimilitudes = em_gmm(datos, K)

# -------------------------------
# 3. Mostramos resultados
# -------------------------------

print("\nResultados finales del Algoritmo EM:")
print("-" * 40)
print(f"Pesos finales: {np.round(pesos, 4)}")  # Pesos de cada componente
print(f"Medias finales: {np.round(medias, 4)}")  # Medias de cada componente
print(f"Desviaciones finales: {np.round(desviaciones, 4)}")  # Desviaciones estándar de cada componente
print("-" * 40)

# -------------------------------
# 4. Visualización
# -------------------------------

# Histograma de los datos y componentes gaussianos
x = np.linspace(min(datos)-5, max(datos)+5, 1000)  # Rango de valores para graficar las gaussianas
plt.figure(figsize=(10, 6))
plt.hist(datos, bins=30, density=True, alpha=0.5, label="Datos reales")  # Histograma de los datos
for k in range(K):
    # Graficamos cada componente gaussiano ajustado
    plt.plot(x, pesos[k] * norm.pdf(x, medias[k], desviaciones[k]), label=f'Componente {k+1}')
plt.title("Resultado del Algoritmo EM con GMM")
plt.xlabel("Valor")
plt.ylabel("Densidad")
plt.legend()
plt.grid()
plt.show()

# Gráfico de la log-verosimilitud
plt.figure(figsize=(10, 6))
plt.plot(log_verosimilitudes, marker='o', label="Log-verosimilitud")  # Evolución de la log-verosimilitud
plt.title("Evolución de la Log-Verosimilitud")
plt.xlabel("Iteración")
plt.ylabel("Log-Verosimilitud")
plt.legend()
plt.grid()
plt.show()

# Visualización de responsabilidades
plt.figure(figsize=(10, 6))
plt.scatter(datos, responsabilidades[:, 0], alpha=0.6, label="Responsabilidad Componente 1")  # Responsabilidad del componente 1
plt.scatter(datos, responsabilidades[:, 1], alpha=0.6, label="Responsabilidad Componente 2")  # Responsabilidad del componente 2
plt.title("Responsabilidades de los Componentes")
plt.xlabel("Datos")
plt.ylabel("Responsabilidad")
plt.legend()
plt.grid()
plt.show()

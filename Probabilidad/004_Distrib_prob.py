import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Definimos una distribución de probabilidad discreta (ejemplo: lanzamiento de un dado)
eventos = [1, 2, 3, 4, 5, 6]  # Resultados posibles de un dado
probabilidades = [1/6] * 6  # Probabilidad uniforme (todas las caras tienen la misma probabilidad)

# Mostramos la distribución de probabilidad discreta
print("Distribución de probabilidad discreta (dado justo):")
for i in range(len(eventos)):
    print(f"P(X={eventos[i]}) = {probabilidades[i]:.2f}")

# Graficamos la distribución discreta
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.bar(eventos, probabilidades, color='blue', alpha=0.7)
plt.xlabel('Resultado del dado')
plt.ylabel('Probabilidad')
plt.title('Distribución de probabilidad discreta')

# Definimos una distribución de probabilidad continua (ejemplo: distribución normal)
media = 0      # Media de la distribución
desviacion = 1  # Desviación estándar

# Generamos valores para la distribución normal
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, media, desviacion)  # Calculamos la función de densidad de probabilidad

# Graficamos la distribución continua
plt.subplot(1, 2, 2)
plt.plot(x, y, color='red', label="Distribución Normal")
plt.xlabel('Valores de X')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución de probabilidad continua')
plt.legend()

# Mostramos la gráfica
plt.tight_layout()
plt.show()

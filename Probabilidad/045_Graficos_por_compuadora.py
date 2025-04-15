import matplotlib.pyplot as plt

def bresenham_line(x0, y0, x1, y1):
    """
    Algoritmo de Bresenham para trazar una línea entre (x0, y0) y (x1, y1).
    Devuelve una lista de puntos que forman la línea.
    """
    puntos = []  # Lista donde almacenamos los puntos de la línea

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    sx = 1 if x0 < x1 else -1  # Dirección en X
    sy = 1 if y0 < y1 else -1  # Dirección en Y

    err = dx - dy  # Error inicial

    while True:
        puntos.append((x0, y0))  # Agrega el punto actual a la línea
        if x0 == x1 and y0 == y1:  # Si llegamos al punto final, terminamos
            break

        e2 = 2 * err  # Doblar el error para comparar

        if e2 > -dy:  # Ajuste horizontal
            err -= dy
            x0 += sx

        if e2 < dx:  # Ajuste vertical
            err += dx
            y0 += sy

    return puntos

# ----- Función para graficar múltiples líneas -----
def graficar_lineas(lineas):
    """
    Dibuja múltiples líneas en un gráfico con una cuadrícula que simula píxeles.
    Cada línea se dibuja con un color diferente.
    """
    colores = ['red', 'blue', 'green', 'orange', 'purple']  # Lista de colores para las líneas
    plt.figure(figsize=(8, 8))
    
    for i, linea in enumerate(lineas):
        x_vals, y_vals = zip(*linea)
        color = colores[i % len(colores)]  # Seleccionar un color de la lista (cíclico si hay más líneas que colores)
        plt.plot(x_vals, y_vals, 'o-', color=color, label=f"Línea ({linea[0]} -> {linea[-1]})")  # Puntos con líneas

    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.title("Líneas usando el algoritmo de Bresenham")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.xticks(range(0, 20))  # Ajustar según el rango esperado
    plt.yticks(range(0, 20))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.show()

# ----- Prueba del algoritmo -----
# Coordenadas iniciales y finales para múltiples líneas
coordenadas = [
    (2, 2, 12, 8),  # Línea 1
    (5, 5, 15, 5),  # Línea 2
    (10, 2, 10, 12) # Línea 3
]

# Generar las líneas usando el algoritmo de Bresenham
lineas = [bresenham_line(x0, y0, x1, y1) for x0, y0, x1, y1 in coordenadas]

# Graficar las líneas
graficar_lineas(lineas)

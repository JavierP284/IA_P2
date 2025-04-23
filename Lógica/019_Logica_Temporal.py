# ----------------------------------------------
# Lógica Temporal - Simulación simple en Python
# ----------------------------------------------

# Secuencia temporal de verdad para la proposición P
# Por ejemplo: [True, True, False, True]
# Significa que en t0: P, t1: P, t2: no P, t3: P
tiempo_P = [True, True, False, True]

# G P: "Siempre" P (en todos los tiempos a partir del actual)
def siempre_P(P_tiempos, inicio=0):
    """
    Verifica si P es verdadera en todos los tiempos desde 'inicio'.
    Recorre la lista desde el índice 'inicio' hasta el final.
    Si encuentra un valor False, retorna False.
    Si no encuentra ningún False, retorna True.
    """
    for t in range(inicio, len(P_tiempos)):
        if not P_tiempos[t]:  # Si P no es verdadera en algún tiempo
            return False
    return True  # P es verdadera en todos los tiempos

# F P: "Algún día" P (existe algún tiempo futuro donde P es verdadera)
def algun_dia_P(P_tiempos, inicio=0):
    """
    Verifica si existe algún tiempo futuro (desde 'inicio') donde P es verdadera.
    Recorre la lista desde el índice 'inicio' hasta el final.
    Si encuentra un valor True, retorna True.
    Si no encuentra ningún True, retorna False.
    """
    for t in range(inicio, len(P_tiempos)):
        if P_tiempos[t]:  # Si P es verdadera en algún tiempo
            return True
    return False  # P nunca es verdadera

# X P: "Próximo" P (en el siguiente instante P es verdadera)
def siguiente_P(P_tiempos, actual):
    """
    Verifica si P es verdadera en el siguiente instante al tiempo 'actual'.
    Si el índice actual + 1 está dentro de los límites de la lista, retorna el valor.
    Si no hay un siguiente instante (índice fuera de rango), retorna None.
    """
    if actual + 1 < len(P_tiempos):  # Verifica si hay un siguiente instante
        return P_tiempos[actual + 1]
    else:
        return None  # No hay siguiente tiempo

# P U Q: P hasta que Q (P se mantiene verdadera hasta que Q sea verdadera)
def hasta_que(P_tiempos, Q_tiempos):
    """
    Verifica si P se mantiene verdadera hasta que Q sea verdadera.
    Recorre ambas listas simultáneamente.
    Si Q es verdadera en algún tiempo, verifica que P haya sido verdadera
    en todos los tiempos anteriores. Si es así, retorna True.
    Si Q nunca es verdadera, retorna False.
    """
    if len(P_tiempos) != len(Q_tiempos):  # Validación: ambas listas deben tener la misma longitud
        raise ValueError("Las secuencias P y Q deben tener la misma longitud.")
    
    for t in range(len(P_tiempos)):
        if Q_tiempos[t]:  # Si Q es verdadera en el tiempo t
            # Verifica que P haya sido verdadera en todos los tiempos anteriores
            return all(P_tiempos[i] for i in range(t))
    return False  # Q nunca se cumple

# Simulamos otra proposición Q en el tiempo
# Por ejemplo: [False, False, False, True]
# Significa que Q solo se cumple en t3
tiempo_Q = [False, False, False, True]

# Función para mostrar las secuencias temporales
def mostrar_secuencia(nombre, secuencia):
    """
    Muestra una secuencia temporal de manera legible.
    Convierte los valores True y False en símbolos 'V' y 'F' respectivamente.
    """
    print(f"{nombre}: {' '.join(['V' if x else 'F' for x in secuencia])}")

# Mostrar las secuencias temporales
print("Secuencias temporales:")
mostrar_secuencia("P", tiempo_P)  # Muestra la secuencia de P
mostrar_secuencia("Q", tiempo_Q)  # Muestra la secuencia de Q

# Resultados de las operaciones lógicas temporales
print("\nResultados de las operaciones:")
print("G P desde t0 (siempre P):", siempre_P(tiempo_P))  # Verifica si P es siempre verdadera desde t0
print("F P desde t0 (algún día P):", algun_dia_P(tiempo_P))  # Verifica si P es verdadera en algún momento desde t0
print("X P en t1 (P en el siguiente instante):", siguiente_P(tiempo_P, 1))  # Verifica si P es verdadera en t2
print("P U Q (P hasta que Q):", hasta_que(tiempo_P, tiempo_Q))  # Verifica si P se mantiene verdadera hasta que Q sea verdadera

# Casos adicionales para mayor claridad
print("\nCasos adicionales:")
print("G P desde t2 (siempre P desde t2):", siempre_P(tiempo_P, inicio=2))  # Verifica si P es siempre verdadera desde t2
print("F P desde t2 (algún día P desde t2):", algun_dia_P(tiempo_P, inicio=2))  # Verifica si P es verdadera en algún momento desde t2
print("X P en t3 (P en el siguiente instante):", siguiente_P(tiempo_P, 3))  # No hay siguiente instante, debería retornar None

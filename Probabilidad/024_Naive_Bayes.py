from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

# -------------------------------
# 1. Datos de entrenamiento
# -------------------------------

# Cada fila representa una persona con dos características: [edad, salario]
X = np.array([
    [25, 5000],
    [30, 6000],
    [45, 8000],
    [35, 12000],
    [50, 15000],
    [23, 4000],
    [40, 9000],
])

# Etiquetas correspondientes para cada persona: "yes" (comprador) o "no" (no comprador)
y = np.array(["no", "no", "yes", "yes", "yes", "no", "yes"])

# Dividimos los datos en conjuntos de entrenamiento y prueba
# 80% de los datos se usarán para entrenar el modelo, y 20% para probarlo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizamos los datos para que las características (edad y salario) tengan la misma escala
# Esto ayuda a mejorar la consistencia del modelo
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # Ajustamos el escalador con los datos de entrenamiento
X_test = scaler.transform(X_test)       # Aplicamos la misma transformación a los datos de prueba

# -------------------------------
# 2. Creamos y entrenamos el modelo
# -------------------------------

# Creamos un modelo Naive Bayes Gaussiano
modelo = GaussianNB()

# Entrenamos el modelo con los datos de entrenamiento
modelo.fit(X_train, y_train)

# -------------------------------
# 3. Nuevos datos a clasificar
# -------------------------------

# Solicitamos al usuario que ingrese los datos de una nueva persona
try:
    # Pedimos la edad y el salario como entrada del usuario
    edad = float(input("Ingrese la edad de la persona: "))
    salario = float(input("Ingrese el salario de la persona: "))

    # Creamos un arreglo con los datos ingresados
    nueva_persona = np.array([[edad, salario]])

    # Normalizamos los datos ingresados usando el mismo escalador
    nueva_persona_normalizada = scaler.transform(nueva_persona)

    # -------------------------------
    # 4. Hacemos la predicción
    # -------------------------------

    # Usamos el modelo entrenado para predecir si la persona es comprador o no
    prediccion = modelo.predict(nueva_persona_normalizada)

    # También obtenemos las probabilidades de cada clase ("yes" y "no")
    probs = modelo.predict_proba(nueva_persona_normalizada)

    # -------------------------------
    # 5. Mostramos resultados
    # -------------------------------

    # Mostramos los resultados de la predicción
    print("\n--- Resultados de la Clasificación ---")
    print(f"Datos ingresados: Edad = {edad}, Salario = {salario}")
    # Interpretamos la predicción: "yes" significa comprador, "no" significa no comprador
    print(f"Clasificación: {'Comprador' if prediccion[0] == 'yes' else 'No comprador'}")

    # Mostramos las probabilidades de cada clase
    print("Probabilidades:")
    for clase, probabilidad in zip(modelo.classes_, probs[0]):
        print(f"  - {clase.capitalize()}: {probabilidad * 100:.2f}%")

    # -------------------------------
    # 6. Evaluamos el modelo (opcional)
    # -------------------------------

    # Calculamos la precisión del modelo en los datos de prueba
    accuracy = modelo.score(X_test, y_test)
    print(f"\nPrecisión del modelo en datos de prueba: {accuracy * 100:.2f}%")

except ValueError:
    # Si el usuario ingresa datos no válidos, mostramos un mensaje de error
    print("Por favor, ingrese valores numéricos válidos para la edad y el salario.")


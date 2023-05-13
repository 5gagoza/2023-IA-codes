#Supongamos que queremos estimar la posición de un objeto móvil en un espacio bidimensional. Utilizaremos un modelo de filtro de partículas para realizar esta tarea.

import numpy as np

# Definir la función de transición de estado
def transicion_estado(x, y):
    nuevo_x = x + np.random.normal(0, 1)
    nuevo_y = y + np.random.normal(0, 1)
    return nuevo_x, nuevo_y

# Definir la función de observación
def observacion(x, y):
    return np.sqrt(x**2 + y**2) + np.random.normal(0, 0.5)

# Definir el modelo de filtro de partículas
def particle_filter(num_particulas, observacion_actual):
    # Inicializar las partículas de manera aleatoria
    particulas = np.random.uniform(-10, 10, size=(num_particulas, 2))

    # Realizar la transición de estado y actualización del peso para cada partícula
    for i in range(num_particulas):
        particulas[i] = transicion_estado(particulas[i, 0], particulas[i, 1])
        peso = observacion(particulas[i, 0], particulas[i, 1])
        particulas[i] = (particulas[i, 0], particulas[i, 1], peso)

    # Normalizar los pesos de las partículas
    pesos = np.array([particula[2] for particula in particulas])
    pesos = pesos / np.sum(pesos)

    # Realizar el muestreo de las partículas basado en los pesos
    particulas_muestreadas = np.random.choice(particulas, size=num_particulas, replace=True, p=pesos)
    particulas_muestreadas = [(particula[0], particula[1]) for particula in particulas_muestreadas]

    # Calcular la estimación de la posición
    estimacion_x = np.mean([particula[0] for particula in particulas_muestreadas])
    estimacion_y = np.mean([particula[1] for particula in particulas_muestreadas])

    return estimacion_x, estimacion_y

# Simular el movimiento del objeto y realizar las estimaciones
posicion_actual = (0, 0)
observaciones = [observacion(posicion_actual[0], posicion_actual[1]) for _ in range(10)]

for i in range(len(observaciones)):
    estimacion_x, estimacion_y = particle_filter(1000, observaciones[i])
    print(f"Iteración {i+1}: Estimación de la posición: ({estimacion_x:.2f}, {estimacion_y:.2f})")


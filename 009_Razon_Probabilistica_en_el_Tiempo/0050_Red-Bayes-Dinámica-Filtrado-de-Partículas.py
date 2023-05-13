"""
Este código implementa un algoritmo de filtrado de partículas para el seguimiento de un objeto en movimiento en un entorno determinado. 
En primer lugar, se define el modelo dinámico del sistema, es decir, cómo se espera que el objeto se mueva en función de su velocidad y dirección actuales. 
Luego, se define el modelo de observación, que describe cómo se espera que las mediciones (por ejemplo, de un sensor) del estado del objeto se relacionen con su posición y velocidad.

A continuación, se utiliza un filtro de partículas para estimar la distribución de probabilidad posterior del estado del objeto, dado el modelo dinámico y las mediciones observadas. 
El filtro de partículas utiliza una serie de partículas, cada una de las cuales representa una posible estimación del estado actual del objeto. 
En cada iteración del filtro, se actualizan las posiciones y pesos de las partículas en función de su adecuación a las mediciones observadas y al modelo dinámico del sistema. 
Al final, se calcula la estimación del estado del objeto a partir de las posiciones y pesos de las partículas.
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from numpy.random import randn

# Definir el modelo
def transition_model(x, u):
    # Modelo de transición: random walk con una leve desviación
    return x + (randn() * 0.1) + u

def observation_model(x):
    # Modelo de observación: Gaussiana con media x y desviación estándar 0.1
    return norm(x, 0.1).rvs()

# Definir el número de partículas
N = 1000

# Inicializar las partículas
particles = np.zeros((N, 2))
particles[:, 0] = np.random.normal(0, 1, N)
weights = np.ones(N) / N

# Inicializar la estimación
x_est = np.zeros(2)

# Definir la trayectoria de entrada
U = np.zeros((100, 2))
U[:, 0] = 0.2 * np.sin(np.linspace(0, 6 * np.pi, 100))
U[:, 1] = 0.2 * np.cos(np.linspace(0, 6 * np.pi, 100))

# Simulación
for t in range(len(U)):
    # Predecir la posición de las partículas
    for i in range(N):
        particles[i, 1] = transition_model(particles[i, 0], U[t, 0])
        particles[i, 0] = transition_model(particles[i, 1], U[t, 1])
    
    # Calcular las observaciones
    observations = np.array([observation_model(particles[i, 0]) for i in range(N)])
    
    # Calcular los pesos
    weights *= norm.pdf(observations, loc=particles[:, 0], scale=0.1)
    weights /= np.sum(weights)
    
    # Estimar la posición del robot
    x_est = np.average(particles, weights=weights, axis=0)
    
    # Mostrar los resultados
    print("Tiempo:", t)
    print("Posición del robot estimada:", x_est)
    print("Posición del robot real:", U[t])
    print()
    
    # Re-muestrear las partículas
    indices = np.random.choice(N, size=N, p=weights)
    particles = particles[indices]
    weights = np.ones(N) / N

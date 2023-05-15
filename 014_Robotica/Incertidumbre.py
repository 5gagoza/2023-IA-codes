
import numpy as np
from scipy.stats import norm

# Longitudes de las dos articulaciones del robot
L1 = 2
L2 = 3

# Coordenadas del objetivo en el plano
x = 4
y = 2

# Medición de la posición del robot
x_robot = np.random.normal(0, 0.1)
y_robot = np.random.normal(0, 0.1)

# Medición de la posición del objetivo
x_obj = np.random.normal(x, 0.1)
y_obj = np.random.normal(y, 0.1)

# Calcular la distancia del objetivo al origen del plano
r = np.sqrt((x_obj - x_robot)**2 + (y_obj - y_robot)**2)

# Calcular el ángulo entre el objetivo y el eje x
theta1 = np.arctan2(y_obj - y_robot, x_obj - x_robot)

# Calcular el ángulo entre las dos articulaciones del robot
theta2 = np.arccos((L1**2 + L2**2 - r**2) / (2 * L1 * L2))

# Calcular el ángulo de la primera articulación del robot
phi1 = theta1 + np.arctan2(L2 * np.sin(theta2), L1 + L2 * np.cos(theta2))

# Calcular el ángulo de la segunda articulación del robot
phi2 = np.pi - theta2

# Calcular la probabilidad de alcanzar el objetivo
prob = norm.pdf(x_obj, x_robot + L1*np.cos(phi1) + L2*np.cos(phi1 + phi2), 0.1) * norm.pdf(y_obj, y_robot + L1*np.sin(phi1) + L2*np.sin(phi1 + phi2), 0.1)

# Imprimir los ángulos de las articulaciones del robot y la probabilidad de alcanzar el objetivo
print("Articulación 1: ", phi1)
print("Articulación 2: ", phi2)
print("Probabilidad de alcanzar el objetivo: ", prob)


import numpy as np
import matplotlib.pyplot as plt

# Definimos la función de modelo de movimiento del robot
def motion_model(x, u):
    x_new = x + u
    return x_new

# Definimos la función de modelo de observación del robot
def observation_model(x):
    # Generamos una observación simulada del sensor de distancia
    # Se asume que el sensor siempre detecta la pared en la posición x = 10
    obs = np.random.normal(loc=10 - x, scale=0.5)
    return obs

# Definimos los parámetros del filtro de partículas
num_particles = 1000
Q = 0.1  # varianza del ruido de movimiento del robot
R = 0.5  # varianza del ruido de observación del sensor de distancia

# Generamos el mapa del entorno (no es necesario en este ejemplo)

# Generamos los datos de control simulados
num_steps = 20
u = 0.1*np.ones(num_steps)  # movimiento lineal constante del robot

# Inicializamos las partículas
x_true = 0  # posición verdadera del robot en x
x_est = np.random.normal(loc=x_true, scale=1, size=num_particles)  # distribución inicial de las partículas
weights = np.ones(num_particles) / num_particles

# Iteramos a través de los pasos de tiempo
for t in range(num_steps):
    # Movemos el robot y las partículas
    x_true = motion_model(x_true, u[t]) + np.random.normal(loc=0, scale=np.sqrt(Q))
    x_est = motion_model(x_est, u[t]) + np.random.normal(loc=0, scale=np.sqrt(Q), size=num_particles)
    
    # Calculamos los pesos de las partículas basados en la observación del sensor de distancia
    obs = observation_model(x_true)
    likelihood = np.exp(-0.5*(x_est - obs)**2/R)
    weights = likelihood / np.sum(likelihood)
    
    # Seleccionamos nuevas partículas basadas en sus pesos
    indices = np.random.choice(num_particles, size=num_particles, replace=True, p=weights)
    x_est = x_est[indices]
    weights = weights[indices]
    weights /= np.sum(weights)
    
    # Calculamos la estimación de la posición del robot
    x_mean = np.mean(x_est)
    print(f"Tiempo {t}: Posición verdadera: {x_true:.2f}, Posición estimada: {x_mean:.2f}")

    


"""
Este código implementa un filtro de Kalman para estimar el estado de un sistema a partir de mediciones ruidosas. El filtro de Kalman es un 
algoritmo de estimación óptima que combina la información disponible en las mediciones con un modelo del sistema para 
producir una estimación del estado más precisa que cualquiera de las mediciones individuales.

En este código, se utiliza un modelo muy simple de un sistema en el que el estado es un escalar que evoluciona en el tiempo con una velocidad constante y una aceleración constante. 
El modelo asume que el ruido en las mediciones es gaussiano y que el ruido en la evolución del estado es también gaussiano y no correlacionado con el ruido en las mediciones.
"""

import numpy as np
import matplotlib.pyplot as plt

# Definimos las matrices de estado y medición
A = np.array([[1, 1], [0, 1]])  # Matriz de estado
C = np.array([[1, 0]])  # Matriz de medición

# Definimos las matrices de ruido del proceso y de la medición
Q = np.array([[0.1, 0.1], [0.1, 0.1]])
R = np.array([[1]])

# Generamos una trayectoria aleatoria de posición y velocidad
np.random.seed(0)
n_steps = 50
dt = 0.1
pos_true = np.zeros(n_steps)
vel_true = np.zeros(n_steps)
pos_meas = np.zeros(n_steps)
for i in range(1, n_steps):
    vel_true[i] = 0.5 * vel_true[i-1] + 0.1 * np.random.randn()
    pos_true[i] = pos_true[i-1] + vel_true[i-1]*dt
    pos_meas[i] = pos_true[i] + np.sqrt(R[0,0]) * np.random.randn()

# Definimos el vector de estado inicial y la matriz de covarianza inicial
x0 = np.array([pos_meas[0], 0])
P0 = np.array([[10, 0], [0, 1]])

# Ejecutamos el filtro de Kalman para estimar la posición y velocidad
x_est = np.zeros((n_steps, 2))
P_est = np.zeros((n_steps, 2, 2))
x_est[0] = x0
P_est[0] = P0
for i in range(1, n_steps):
    # Predicción del estado y de la covarianza
    x_pred = A @ x_est[i-1]
    P_pred = A @ P_est[i-1] @ A.T + Q

    # Actualización del estado y de la covarianza
    y = pos_meas[i] - C @ x_pred
    S = C @ P_pred @ C.T + R
    K = P_pred @ C.T @ np.linalg.inv(S)
    x_est[i] = x_pred + K @ y
    P_est[i] = (np.eye(2) - K @ C) @ P_pred

# Graficamos la trayectoria estimada junto con la trayectoria real
plt.figure(figsize=(8, 6))
plt.plot(np.arange(n_steps)*dt, pos_true, label='Posición real')
plt.plot(np.arange(n_steps)*dt, x_est[:, 0], label='Posición estimada')
plt.legend()
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Definir las matrices A, B y Q del modelo del sistema
A = np.array([[1.0, 0.1], [0.0, 1.0]])
B = np.array([[0.0], [1.0]])
Q = np.diag([1.0, 1.0])

# Definir la matriz R del costo del control
R = np.array([[1.0]])

# Calcular la matriz P usando la ecuación de Riccati
P = np.matrix(np.zeros([2,2]))
P_new = Q
i = 0
while not np.allclose(P, P_new):
    i += 1
    P = P_new
    K = np.linalg.inv(R + B.T @ P @ B) @ B.T @ P @ A
    P_new = Q + A.T @ P @ (A - B @ K)
    
# Calcular la matriz K del controlador LQR
K = np.linalg.inv(R + B.T @ P @ B) @ B.T @ P @ A 

# Definir el estado inicial y el tiempo de simulación
x0 = np.array([0.0, 0.0])
T = 10.0
dt = 0.01
t = np.arange(0.0, T, dt)

# Simular el sistema con el controlador LQR
x = np.zeros([len(t), 2])
u = np.zeros([len(t), 1])
x[0,:] = x0
for i in range(len(t)-1):
    u[i,:] = -K @ x[i,:]
    x[i+1,:] = A @ x[i,:] + B @ u[i,:]

# Graficar los resultados
plt.figure()
plt.plot(t, x[:,0], label='Posición')
plt.plot(t, x[:,1], label='Velocidad')
plt.plot(t, u[:,0], label='Control')
plt.legend()
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición / Velocidad / Control')
plt.show()

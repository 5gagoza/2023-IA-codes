
import numpy as np
import matplotlib.pyplot as plt
import time

q_start = np.array([0, 0]) # posición inicial
q_goal = np.array([2, 3]) # posición deseada

# Definir puntos intermedios
delta = 0.1
x = np.arange(q_start[0], q_goal[0], delta)
y = np.arange(q_start[1], q_goal[1], delta)
X, Y = np.meshgrid(x, y)
waypoints = np.vstack([X.flatten(), Y.flatten()]).T

# Controlador de movimiento en el espacio de configuración
def move_to_waypoint(q_current, q_goal):
    distance = np.linalg.norm(q_goal - q_current)
    direction = (q_goal - q_current) / distance
    return q_current + direction * delta, distance < delta

q_current = q_start

# Crear la figura y el eje para visualización
fig, ax = plt.subplots()
ax.set_xlim([q_start[0], q_goal[0]])
ax.set_ylim([q_start[1], q_goal[1]])
ax.set_aspect('equal')

# Visualizar los puntos intermedios y la trayectoria planificada
ax.plot(waypoints[:, 0], waypoints[:, 1], 'b--', label='Trajectory')
ax.plot(q_start[0], q_start[1], 'go', label='Start')
ax.plot(q_goal[0], q_goal[1], 'ro', label='Goal')
ax.legend()

while np.linalg.norm(q_current - q_goal) > delta:
    # Mover el robot hacia el siguiente punto intermedio
    q_next, reached_waypoint = move_to_waypoint(q_current, waypoints[0])
    if reached_waypoint:
        waypoints = waypoints[1:] # eliminar el punto actual de la lista de puntos intermedios
    q_current = q_next
    
    # Actualizar la posición del robot en la visualización
    ax.plot(q_current[0], q_current[1], 'yo')
    fig.canvas.draw()
    time.sleep(delta)

plt.show()

"""Este código visualiza los puntos intermedios y la trayectoria planificada en un gráfico 
2D y actualiza la posición del robot en cada iteración de la simulación. La visualización 
permite observar el movimiento del robot en tiempo real en el espacio de configuración, 
desde su posición inicial hasta su posición deseada.
"""
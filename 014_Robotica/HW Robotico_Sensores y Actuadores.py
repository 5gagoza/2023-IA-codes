
import numpy as np
import matplotlib.pyplot as plt

# Definimos el tamaño del entorno bidimensional que estaremos utilizando
size_x = 10
size_y = 10

# Definimos la posición inicial del robot
start_x = np.random.randint(0, size_x)
start_y = np.random.randint(0, size_y)

# Creamos el mapa del entorno indicando una matriz bidimensional de 10 x 10 inicializada en ceros
environment = np.zeros((size_y, size_x))

# Establecemos la posición del robot en el mapa del entorno
environment[start_y, start_x] = 1

# Función para mostrar el mapa del entorno y la posición actual del robot
def plot_environment():
    #Mostramos el entorno con tonalidades azules
    plt.imshow(environment, cmap='Blues', interpolation='nearest')
    plt.xticks(range(size_x))
    plt.yticks(range(size_y))
    #Definimos la forma de las celdas y el color
    plt.grid(color='black', lw=0.5)
    plt.show()

# Función para mover el robot basado en la probabilidad de los sensores y actuadores
def move():
    robot_x, robot_y = start_x, start_y
    sensor_error = 0.2 # Error en la medición del sensor
    movement_error = 0.2 # Error en el movimiento del robot

    while True:
        # Calcular las probabilidades de movimiento
        probabilities = []
        total_probability = 0

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = robot_x + dx, robot_y + dy

            if 0 <= new_x < size_x and 0 <= new_y < size_y:
                # Calcular la probabilidad del sensor
                sensor_prob = 1 - sensor_error if environment[new_y, new_x] == 1 else sensor_error
                # Calcular la probabilidad del movimiento
                movement_prob = 1 - movement_error if (dx == 0 and dy == 0) else movement_error / 3
                # Calcular la probabilidad total
                probability = sensor_prob * movement_prob
                probabilities.append((probability, new_x, new_y))
                total_probability += probability

        # Normalizar las probabilidades
        probabilities = [(prob / total_probability, new_x, new_y) for prob, new_x, new_y in probabilities]

        # Seleccionar una dirección basada en las probabilidades
        selected_probability = np.random.random()
        cumulative_probability = 0

        for probability, new_x, new_y in probabilities:
            cumulative_probability += probability

            if selected_probability <= cumulative_probability:
                # Actualizar la posición del robot en el mapa del entorno
                environment[robot_y, robot_x] = 0
                environment[new_y, new_x] = 1
                robot_x, robot_y = new_x, new_y
                break

        # Mostrar el entorno actualizado y la posición actual del robot
        plot_environment()

# Ejecutar el algoritmo de movimiento basado en la probabilidad
move()

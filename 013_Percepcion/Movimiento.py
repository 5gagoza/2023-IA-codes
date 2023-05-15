
import random
#Libreria para mostrar de manera grafica el entorno
import matplotlib.pyplot as plt

#Definimos el tamaño del entorno bidimensional que estaremos utilizando
tamaño_x = 10
tamaño_y = 10

#Definir la posición inicial del robot
start_x = random.randint(0, tamaño_x-1)
start_y = random.randint(0, tamaño_y-1)

#Creamos el mapa del entorno indicando una matriz bidimensional de 10 x 10 inicializada en ceros
environment = [[0] * tamaño_x for _ in range(tamaño_y)]
environment[start_y][start_x] = 1

#Función para mostrar el mapa del entorno
def plot_environment():
    plt.imshow(environment, cmap='Blues', interpolation='nearest')
    plt.xticks(range(tamaño_x))
    plt.yticks(range(tamaño_y))
    plt.grid(color='black', lw=0.5)
    plt.show()

#Mostrar el entorno inicial
plot_environment()

#Definir la función de movimiento basado en la probabilidad
def move():
    current_x, current_y = start_x, start_y

    while True:
        #Calcular las probabilidades de movimiento
        probabilities = []
        total_probability = 0

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = current_x + dx, current_y + dy

            if 0 <= new_x < tamaño_x and 0 <= new_y < tamaño_y:
                probability = random.random()
                probabilities.append((probability, new_x, new_y))
                total_probability += probability

        #Normalizar las probabilidades
        probabilities = [(prob / total_probability, new_x, new_y) for prob, new_x, new_y in probabilities]

        #Seleccionar una dirección basada en las probabilidades
        selected_probability = random.random()
        cumulative_probability = 0

        for probability, new_x, new_y in probabilities:
            cumulative_probability += probability

            if selected_probability <= cumulative_probability:
                current_x, current_y = new_x, new_y
                environment[current_y][current_x] += 1
                break

        #Mostrar el entorno actualizado
        plot_environment()

#Ejecutar el algoritmo de movimiento basado en la probabilidad
move()

import numpy as np

# Definir la matriz de transición de estados
transition_matrix = np.array([[0.8, 0.1, 0.1],
                              [0.4, 0.4, 0.2],
                              [0.2, 0.3, 0.5]])

# Definir los estados
states = ['Soleado', 'Nublado', 'Lluvioso']
#Supongamos que queremos modelar el clima utilizando un modelo de cadena de Markov de primer orden. Definimos tres estados posibles para el clima: soleado, nublado y lluvioso. Además, conocemos las probabilidades de transición entre los estados en función del clima del día anterior.
# Definir la distribución inicial de probabilidades
initial_distribution = np.array([0.4, 0.4, 0.2])

# Generar una secuencia de estados utilizando el modelo de cadena de Markov
num_steps = 7  # Número de pasos en la secuencia
current_state = np.random.choice(states, p=initial_distribution)
sequence = [current_state]

for _ in range(num_steps):
    current_state = np.random.choice(states, p=transition_matrix[states.index(current_state)])
    sequence.append(current_state)

print("Secuencia de estados generada:", sequence)


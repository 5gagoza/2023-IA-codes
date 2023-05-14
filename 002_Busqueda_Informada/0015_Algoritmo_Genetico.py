import random

# Definimos la función que queremos optimizar
def fitness_function(x):
    return -1 * (x ** 2)

# Configuración del algoritmo genético
population_size = 10
mutation_rate = 0.1
generations = 50

# Generamos una población inicial aleatoria
def generate_initial_population():
    return [random.uniform(-10, 10) for i in range(population_size)]

# Evaluamos la aptitud de cada individuo de la población
def evaluate_population(population):
    return [fitness_function(x) for x in population]

# Seleccionamos a los individuos más aptos para la reproducción
def select_parents(population, fitness_scores):
    # Seleccionamos aleatoriamente dos padres de la población
    parent1 = population[fitness_scores.index(max(fitness_scores))]
    parent2 = population[fitness_scores.index(max(fitness_scores))]
    return parent1, parent2

# Creamos nuevos individuos mediante la combinación de características de los padres y la mutación aleatoria
def breed(parent1, parent2):
    child = (parent1 + parent2) / 2
    if random.random() < mutation_rate:
        child += random.uniform(-1, 1)
    return child

# Ejecutamos el algoritmo genético
population = generate_initial_population()
for i in range(generations):
    fitness_scores = evaluate_population(population)
    parent1, parent2 = select_parents(population, fitness_scores)
    new_population = [breed(parent1, parent2) for i in range(population_size)]
    population = new_population

# Mostramos la solución encontrada
best_solution = max(population, key=fitness_function)
print("La mejor solución encontrada es:", best_solution)

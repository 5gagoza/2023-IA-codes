import networkx as nx
import random
import math

# Definición del grafo
n = 5  # número de nodos
G = nx.complete_graph(n)

# Función para calcular el costo de una solución (ordenamiento de nodos)
def get_cost(G, solution):
    cost = 0
    for i in range(len(solution)):
        for j in range(i+1, len(solution)):
            cost += G[solution[i]][solution[j]]['weight']
    return cost

# Función de recocido simulado
def simulated_annealing(G, initial_temp, final_temp, alpha):
    # Inicialización de la solución aleatoria
    solution = list(G.nodes())
    random.shuffle(solution)
    
    # Parámetros iniciales del algoritmo
    current_temp = initial_temp
    
    while current_temp > final_temp:
        # Selecciona un vecino aleatorio
        new_solution = solution.copy()
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        while i == j:
            j = random.randint(0, n-1)
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
        
        # Calcula la diferencia de costo
        delta_cost = get_cost(G, new_solution) - get_cost(G, solution)
        
        # Si la nueva solución es mejor, la acepta automáticamente
        if delta_cost < 0:
            solution = new_solution.copy()
        else:
            # Si la nueva solución es peor, la acepta con una probabilidad dada por la ecuación de Boltzmann
            boltzmann_factor = math.exp(-delta_cost / current_temp)
            if random.random() < boltzmann_factor:
                solution = new_solution.copy()
        
        # Actualiza la temperatura
        current_temp *= alpha
    
    return solution

# Asignación de pesos aleatorios a las aristas
for (u, v) in G.edges():
    G[u][v]['weight'] = random.randint(1, 10)

# Ejemplo de uso
solution = simulated_annealing(G, initial_temp=1000, final_temp=1, alpha=0.99)
print("La solución óptima es: ", solution)

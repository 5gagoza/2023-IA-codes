import random
import math
import matplotlib.pyplot as plt

def distance(city1, city2):
    """
    Calcula la distancia euclidiana entre dos ciudades.
    """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_distance(cities, tour):
    """
    Calcula la distancia total del recorrido dado por un tour.
    """
    return sum(distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1)) + distance(cities[tour[-1]], cities[tour[0]])

def random_tour(cities):
    """
    Genera un tour aleatorio que visita todas las ciudades.
    """
    tour = list(range(len(cities)))
    random.shuffle(tour)
    return tour

def local_beam_search(cities, k, max_iter):
    """
    Aplica el algoritmo de búsqueda de haz local para resolver el problema del TSP.
    cities: lista de coordenadas (x, y) de las ciudades.
    k: número de soluciones en el haz.
    max_iter: número máximo de iteraciones.
    """
    # Generar k soluciones aleatorias
    tours = [random_tour(cities) for _ in range(k)]
    
    # Iterar hasta que se alcance el número máximo de iteraciones
    for i in range(max_iter):
        # Generar soluciones vecinas de todas las soluciones actuales
        neighbors = []
        for tour in tours:
            for i in range(len(cities)):
                for j in range(i+1, len(cities)):
                    neighbor = tour[:]
                    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                    neighbors.append(neighbor)
        
        # Evaluar la función objetivo para cada solución vecina
        fx = [total_distance(cities, tour) for tour in neighbors]
        
        # Seleccionar las k mejores soluciones del haz
        sorted_indices = sorted(range(len(fx)), key=lambda i: fx[i])[:k]
        tours = [neighbors[i] for i in sorted_indices]
    
    # Devolver el mejor tour encontrado
    best_tour = min(tours, key=lambda tour: total_distance(cities, tour))
    return best_tour

def plot_tour(tour, cities):
    """
    Dibuja el tour en un plano cartesiano.
    
    Args:
    tour: una lista de índices de ciudades.
    cities: una lista de coordenadas de ciudades.
    """
    
    x = [city[0] for city in cities]
    y = [city[1] for city in cities]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x[tour], y[tour], 'ro-')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.show()


cities = [(0, 0), (1, 2), (3, 1), (5, 4), (2, 7)]
best_tour = local_beam_search(cities, k=3, max_iter=1000)
print(best_tour)
#plot_tour(best_tour, cities)


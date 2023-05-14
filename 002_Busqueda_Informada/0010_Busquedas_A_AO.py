import pygame
import random
import time
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from queue import PriorityQueue
import math

# Definir las constantes de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20

# Definir los colores
START = (0, 255, 0)
GOAL = (0, 0, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 128, 0)
VIOLET = (175, 0, 255)
VINE = (86, 7, 12)
WHITE = (255, 255, 255)

# Inicializar Pygame
pygame.init()

# Crear la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def generate_maze(n):
    maze = [[1] * (n + 1) for _ in range(n + 1)]  # creamos una matriz llena de unos
    p = 0.3
    for i in range(1, n, 2):
        for j in range(1, n, 2):
            maze[i][j] = random.choices([0, 1], weights = [0.6, 0.4])[0]  # hacemos un camino horizontal en cada fila par
            if maze[i][j] == 1 and (maze[i + 1][j + 1] == 1 or maze[i + 1][j - 1] == 1 or maze[i - 1][j + 1] == 1 or maze[i - 1][j - 1] == 1):
                maze[i][j] = 0
            maze[i + 1][j] = random.choices([0, 1], weights=[1 - p, p])[0]
            maze[i - 1][j] = random.choices([0, 1], weights=[1 - p, p])[0]
            maze[i][j + 1] = random.choices([0, 1], weights=[1 - p, p])[0]
            maze[i][j - 1] = random.choices([0, 1], weights=[1 - p, p])[0]
    return maze

def maze_to_graph(maze):
    n = len(maze) - 2  # obtenemos el tamaño del laberinto
    G = nx.Graph()  # creamos un grafo vacío
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if maze[i][j] == 0:  # si es un camino, agregamos una arista
                node = (i, j)
                neighbors = []
                if maze[i - 1][j] == 0:
                    neighbors.append((i - 1, j))
                if maze[i + 1][j] == 0:
                    neighbors.append((i + 1, j))
                if maze[i][j - 1] == 0:
                    neighbors.append((i, j - 1))
                if maze[i][j + 1] == 0:
                    neighbors.append((i, j + 1))
                for neighbor in neighbors:
                    G.add_edge(node, neighbor, weight = 1)
    return G

# Función para calcular la distancia entre dos nodos
def distancia(nodo1, nodo2):
    return ((nodo2[0] - nodo1[0]) ** 2 + (nodo2[1] - nodo1[1]) ** 2) ** 0.5

# Definir la función heurística
def h(node, end):
    # Estimar el costo del camino más corto desde el nodo actual hasta el nodo de destino
    return nx.shortest_path_length(G, node, end, weight='weight')

def a_estrella(G, start, end, h):
    # Inicializar el diccionario de costos g para cada nodo en el grafo
    g = {node: float('inf') for node in G.nodes()}
    g[start] = 0
    
    # Inicializar el diccionario de nodos visitados y su nodo predecesor
    visited = {}
    visited[start] = None
    
    # Inicializar la lista de nodos por visitar con el nodo de inicio
    open_list = [start]
    
    # Mientras hayan nodos por visitar
    while open_list:
        time.sleep(0.05)
        # Seleccionar el nodo con el costo total más bajo (f = g + h) de la lista abierta
        current_node = min(open_list, key=lambda node: g[node] + h(node, end))
        maze[current_node[0]][current_node[1]] = 2
        
        # Si hemos llegado al nodo de destino, retornar la ruta
        if current_node == end:
            path = []
            while current_node is not None:
                time.sleep(0.05)
                maze[current_node[0]][current_node[1]] = 4
                path.append(current_node)
                current_node = visited[current_node]
                draw_grid(maze)
            return path[::-1]
        
        # Remover el nodo actual de la lista abierta
        open_list.remove(current_node)
        
        # Agregar el nodo actual a la lista de nodos visitados
        visited[current_node] = visited.get(current_node)
        
        # Para cada nodo adyacente al nodo actual
        for neighbor in G.neighbors(current_node):
            # Calcular el costo del camino desde el nodo actual al vecino
            tentative_g = g[current_node] + G[current_node][neighbor]['weight']
            
            # Si el costo del camino es menor al costo guardado en el diccionario g
            if tentative_g < g[neighbor]:
                # Actualizar el costo del camino en el diccionario g
                g[neighbor] = tentative_g
                
                # Agregar el vecino a la lista abierta si no ha sido visitado aún
                if neighbor not in open_list:
                    open_list.append(neighbor)
                    maze[neighbor[0]][neighbor[1]] = 3
                    
                    # Agregar el vecino como el predecesor del nodo actual
                    visited[neighbor] = current_node
        maze[Start[0]][Start[1]] = 9
        maze[Goal[0]][Goal[1]] = 8
        draw_grid(maze)
                    
    # Si no se encontró un camino desde el nodo de inicio al nodo de destino, retornar None
    return None


def ao_estrella(G, start, end, h, c):
    """
    Encuentra el camino más corto desde el nodo de inicio hasta el nodo de destino utilizando el algoritmo AO*.

    Args:
        G (networkx.Graph): El grafo en el que buscar el camino.
        start: El nodo de inicio.
        end: El nodo de destino.
        h (func): Una función heurística que estima el costo del camino más corto desde un nodo dado al nodo de destino.
        c (float): Un factor de corrección para la función heurística.

    Returns:
        La ruta más corta desde el nodo de inicio hasta el nodo de destino.

    """
    # Inicializar las listas de nodos por visitar y nodos visitados
    open_list = [start]
    closed_list = []

    # Inicializar los diccionarios de distancias y padres
    g_scores = {start: 0}
    parents = {start: None}

    # Mientras haya nodos por visitar
    while open_list:
        time.sleep(0.05)
        # Obtener el nodo con el menor costo f_score
        current = min(open_list, key=lambda node: g_scores[node] + c * h(node, end))
        maze[current[0]][current[1]] = 2

        # Si el nodo actual es el nodo de destino, se ha encontrado la ruta más corta
        if current == end:
            # Reconstruir la ruta y devolverla
            path = [current]
            while parents[path[0]] is not None:
                
                time.sleep(0.05)
                maze[path[0][0]][path[0][1]] = 4
                path.insert(0, parents[path[0]])
                draw_grid(maze)
            return path

        # Mover el nodo actual de la lista de nodos por visitar a la lista de nodos visitados
        open_list.remove(current)
        closed_list.append(current)

        # Calcular las distancias desde el nodo actual a sus vecinos
        for neighbor in G.neighbors(current):
            if neighbor in closed_list:
                continue

            # Calcular el costo g_score desde el inicio hasta el vecino
            tentative_g_score = g_scores[current] + h(current, neighbor)

            # Si el vecino no está en la lista de nodos por visitar o el nuevo costo g_score es menor
            # que el anterior, actualizar las listas de distancias y padres
            if neighbor not in open_list or tentative_g_score < g_scores[neighbor]:
                parents[neighbor] = current
                g_scores[neighbor] = tentative_g_score
                maze[neighbor[0]][neighbor[1]] = 3

                # Si el vecino no está en la lista de nodos por visitar, añadirlo
                if neighbor not in open_list:
                    open_list.append(neighbor)
        maze[Start[0]][Start[1]] = 9
        maze[Goal[0]][Goal[1]] = 8
        draw_grid(maze)
    # Si no se ha encontrado una ruta, devolver None
    return None

# Dibujar la cuadrícula
def draw_grid(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 9:
                color = START
            elif maze[row][col] == 8:
                color = GOAL
            elif maze[row][col] == 4:
                color = VINE
            elif maze[row][col] == 1:
                color = BLACK
            elif maze[row][col] == 2:
                color = ORANGE
            elif maze[row][col] == 3:
                color = VIOLET
            else:
                color = WHITE
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()

tamanio = 20

maze = generate_maze(tamanio)

G = maze_to_graph(maze)

pos = nx.spring_layout(G)  # posición de los nodos
nx.draw_networkx_nodes(G, pos, node_color='lightblue')  # dibujamos los nodos
nx.draw_networkx_edges(G, pos, edge_color='black')  # dibujamos las aristas
nx.draw_networkx_labels(G, pos, font_size=8, font_family='sans-serif')  # etiquetamos los nodos
nx.draw_networkx_edge_labels(G, pos, edge_labels = nx.get_edge_attributes(G, 'weight'))


plt.axis('off')  # ocultamos los ejes

plt.show()  # mostramos el grafo
Start = list(G.nodes())[random.randrange(1, G.number_of_nodes())]
Goal = list(G.nodes())[random.randrange(1, G.number_of_nodes())]

maze[Start[0]][Start[1]] = 9
maze[Goal[0]][Goal[1]] = 8
    
# Calcular la ruta utilizando A*
a_star_path = a_estrella(G, Start, Goal, h)
# Imprimir la ruta más corta encontrada
if a_star_path is not None:
    print(f"A* La ruta más corta desde el nodo {Start} hasta el nodo {Goal} es: {a_star_path}")
else:
    print(f"A* No se pudo encontrar una ruta desde el nodo {Start} hasta el nodo {Goal}")

maze[Start[0]][Start[1]] = 9
maze[Goal[0]][Goal[1]] = 8

for i in range(tamanio + 1):
        for j in range(tamanio + 1):
            if maze[i][j] > 1 and maze[i][j] < 8: 
                maze[i][j] = 0
                draw_grid(maze)
                time.sleep(0.02)
draw_grid(maze)
time.sleep(1)

C = 0.5
# Calcular la ruta utilizando AO*
ao_star_path = ao_estrella(G, Start, Goal, h, C)
# Imprimir la ruta más corta encontrada
if ao_star_path is not None:
    print(f"AO* ({C}) La ruta más corta desde el nodo {Start} hasta el nodo {Goal} es: {ao_star_path}")
else:
    print(f"AO* ({C}) No se pudo encontrar una ruta desde el nodo {Start} hasta el nodo {Goal}")

maze[Start[0]][Start[1]] = 9
maze[Goal[0]][Goal[1]] = 8

for i in range(tamanio + 1):
        for j in range(tamanio + 1):
            if maze[i][j] > 1 and maze[i][j] < 8: 
                maze[i][j] = 0  
                draw_grid(maze)
                time.sleep(0.02) 
draw_grid(maze)
time.sleep(1)

C = 5
ao_star_path2 = ao_estrella(G, Start, Goal, h, C)
# Imprimir la ruta más corta encontrada
if ao_star_path2 is not None:
    print(f"AO* ({C}) La ruta más corta desde el nodo {Start} hasta el nodo {Goal} es: {ao_star_path2}")
else:
    print(f"AO* ({C}) No se pudo encontrar una ruta desde el nodo {Start} hasta el nodo {Goal}")
time.sleep(1)

# Dibujar el grafo y las rutas encontradas
#pos = {node: node for node in G.nodes()}
#nx.draw_networkx_nodes(G, pos, node_size=500)
#nx.draw_networkx_edges(G, pos)
#nx.draw_networkx_labels(G, pos)
#plt.plot([node[0] for node in a_star_path], [node[1] for node in a_star_path], 'b--', label="A*")
#plt.plot([node[0] for node in ao_star_path], [node[1] for node in ao_star_path], 'r-', label="AO*")
#plt.plot([node[0] for node in ao_star_path2], [node[1] for node in ao_star_path2], 'g-', label="AO*")
#plt.legend()
#plt.show()
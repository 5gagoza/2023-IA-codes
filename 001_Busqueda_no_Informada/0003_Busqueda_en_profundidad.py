import pygame
import random
import time
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

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
                    G.add_edge(node, neighbor)
    return G

def dfs(graph, start, goal):
    visited = set()    # conjunto para almacenar los nodos visitados
    path = []           # lista para almacenar el camino encontrado
    
    dfs_recursive(graph, start, visited, path, goal)
    
    if goal not in path:
        print(f"No se encontró un camino de {start} a {goal}")
    else:
        print(f"Camino encontrado de {start} a {goal}: {path}")
    
def dfs_recursive(graph, node, visited, path, goal):
    time.sleep(0.05)
    maze[node[0]][node[1]] = 2
    if node == Start:
        maze[node[0]][node[1]] = 9
    # Dibujar la cuadrícula
    draw_grid(maze)
        
    visited.add(node)  # agregamos el nodo actual al conjunto de nodos visitados
    path.append(node)  # agregamos el nodo actual al camino
    
    if node == goal:   # si hemos llegado al objetivo, retornamos el camino
        for i in path[::-1]:
            time.sleep(0.05)
            maze[i[0]][i[1]] = 4
            draw_grid(maze)
        return path
    
    for neighbor in graph.neighbors(node):  # recorremos los vecinos del nodo actual
        if neighbor not in visited:
            maze[neighbor[0]][neighbor[1]] = 3
            draw_grid(maze)
            result = dfs_recursive(graph, neighbor, visited, path, goal)  # llamamos recursivamente la función para el vecino no visitado
            if result is not None:  # si se encontró el objetivo en el camino, retornamos el camino
                return result
    path.pop()  # eliminamos el último nodo del camino, ya que no lleva al objetivo


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

maze = generate_maze(20)

G = maze_to_graph(maze)

pos = nx.spring_layout(G)  # posición de los nodos
nx.draw_networkx_nodes(G, pos, node_color='lightblue')  # dibujamos los nodos
nx.draw_networkx_edges(G, pos, edge_color='black')  # dibujamos las aristas
nx.draw_networkx_labels(G, pos, font_size=8, font_family='sans-serif')  # etiquetamos los nodos


plt.axis('off')  # ocultamos los ejes

plt.show()  # mostramos el grafo
Start = list(G.nodes())[random.randrange(1, G.number_of_nodes())]
Goal = list(G.nodes())[random.randrange(1, G.number_of_nodes())]

maze[Start[0]][Start[1]] = 9
maze[Goal[0]][Goal[1]] = 8

dfs(G, Start, Goal)
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

def IDDFS(graph, start, goal):
    depth = 0
    while True:
        result = dfs_limitado(graph, start, goal, depth)
        print(depth)
        if result is not None:
            for i in result[::-1]:
                time.sleep(0.05)
                maze[i[0]][i[1]] = 4
                draw_grid(maze)
            return result
        for row in range(len(maze)):
            for col in range(len(maze[0])):
                if maze[row][col] > 1 and maze[row][col] < 8:
                    maze[row][col] = 0
        draw_grid(maze)
        depth += 1

def dfs_limitado(grafo, origen, destino, profundidad_limite):
    visitados = set()
    pila = [(origen, [origen])]
    while pila:
        time.sleep(0.1)
        (vertice, camino) = pila.pop()
        if vertice == destino:
            for i in camino[::-1]:
                time.sleep(0.05)
                maze[i[0]][i[1]] = 4
                draw_grid(maze)
            return camino
        if vertice not in visitados and len(camino) < profundidad_limite:
            visitados.add(vertice)
            maze[vertice[0]][vertice[1]] = 2
            for vecino in grafo[vertice]:
                if vecino not in visitados:
                    maze[vecino[0]][vecino[1]] = 3
                    nuevo_camino = list(camino)
                    nuevo_camino.append(vecino)
                    pila.append((vecino, nuevo_camino))
        if origen == Start:
            maze[origen[0]][origen[1]] = 9
        # Dibujar la cuadrícula
        draw_grid(maze)
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

#dfs_limitado(G, Start, Goal, 15)
print(IDDFS(G, Start, Goal))

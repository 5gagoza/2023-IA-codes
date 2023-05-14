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

def bfs(graph, start, goal):
    visited = set()  # nodos visitados
    queue = deque([(start, None)])  # cola con el nodo inicial y su padre
    parents = {start: None}  # diccionario con los padres de cada nodo en el camino
    
    # Mientras queden nodos por visitar
    while queue:
        time.sleep(0.05)
        #print(queue)
        vertex, parent = queue.popleft()  # sacamos el primer elemento de la cola
        if vertex not in visited:
            visited.add(vertex)  # lo marcamos como visitado
            parents[vertex] = parent
            #print('v', vertex)  # imprimimos el nodo
            maze[vertex[0]][vertex[1]] = 2
            if vertex == Start:
              maze[vertex[0]][vertex[1]] = 9  
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.extend([(neighbor, vertex)])  # agregamos los vecinos no visitados a la cola
                    maze[neighbor[0]][neighbor[1]] = 3
                        
            if vertex == goal:
                # se encontró el nodo objetivo, construimos el camino de regreso
                path = []
                current = vertex
                
                while current is not None:
                    time.sleep(0.05)
                    maze[current[0]][current[1]] = 4
                    path.append(current)
                    current = parents[current]
                    draw_grid(maze)
                    
                return path[::-1]  # invertimos la lista para obtener el camino de inicio a fin
            
        # Dibujar la cuadrícula
        draw_grid(maze)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.quit()
                return

    return None

def bidirectional_bfs(graph, start, goal):
    # inicializamos las búsquedas
    forward_queue = deque([start])
    backward_queue = deque([goal])
    forward_visited = {start: None}
    backward_visited = {goal: None}
    
    # mientras ambas búsquedas no se hayan encontrado
    while forward_queue and backward_queue:
        time.sleep(0.05)
        # avanzamos la búsqueda hacia adelante
        current = forward_queue.popleft()
        maze[current[0]][current[1]] = 2
        for neighbor in graph[current]:
            if neighbor not in forward_visited:
                maze[neighbor[0]][neighbor[1]] = 3
                forward_visited[neighbor] = current
                forward_queue.append(neighbor)
            # si encontramos un nodo visitado por la búsqueda hacia atrás
            if neighbor in backward_visited:
                #print('------')
                #print('N', neighbor)
                #print('C', current)
                #print('F', forward_visited)
                #print('B', backward_visited)
                return get_path(forward_visited, backward_visited, current, neighbor)
        
        if current == Start:
              maze[current[0]][current[1]] = 9
              
        # avanzamos la búsqueda hacia atrás
        current = backward_queue.popleft()
        maze[current[0]][current[1]] = 2
        for neighbor in graph[current]:
            if neighbor not in backward_visited:
                maze[neighbor[0]][neighbor[1]] = 3
                backward_visited[neighbor] = current
                backward_queue.append(neighbor)
            # si encontramos un nodo visitado por la búsqueda hacia adelante
            if neighbor in forward_visited:
                #print('N', neighbor)
                #print('C', current)
                #print('F', forward_visited)
                #print('B', backward_visited)
                return get_path(forward_visited, backward_visited, neighbor, current)

        if current == Goal:
              maze[current[0]][current[1]] = 8
        # Dibujar la cuadrícula
        draw_grid(maze)
        
    # si no hay camino, retornamos None
    return None

def get_path(forward_visited, backward_visited, forward_node, backward_node):
    # reconstruimos el camino desde el nodo inicial al final
    path = [forward_node]
    while forward_node != None: #backward_node:
        time.sleep(0.5)
        maze[forward_node[0]][forward_node[1]] = 4
        forward_node = forward_visited.get(forward_node, None)
        #print(forward_node, backward_node)
        path.append(forward_node)
        draw_grid(maze)
    path.reverse()
    # continuamos el camino desde el nodo final al inicial
    while backward_node != None:
        time.sleep(0.5)
        maze[backward_node[0]][backward_node[1]] = 4
        path.append(backward_node)
        backward_node = backward_visited.get(backward_node, None)
        draw_grid(maze)
    return path

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

path = bidirectional_bfs(G, Start, Goal)


if path:
    print('Camino encontrado desde {} hasta {}: {}'.format(Start, Goal, path))
else:
    print('No se encontró un camino desde {} hasta {}'.format(Start, Goal))
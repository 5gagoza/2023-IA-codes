import networkx as nx
import matplotlib.pyplot as plt
import random
import time

def hill_climbing(graph, start_node):
    current_node = start_node
    node_colors = {}
    for node in G.nodes():
            node_colors[node] = 'lightblue'
    node_colors[current_node] = 'red'
    plt.clf()
    plt.plot()  # mostramos el grafo
    nx.draw_networkx_nodes(G, pos, node_color=[node_colors[node] for node in G.nodes()])  # dibujamos los nodos
    nx.draw_networkx_edges(G, pos, edge_color='black')  # dibujamos las aristas
    nx.draw_networkx_labels(G, pos, font_size=8, font_family='sans-serif', labels = node_labels)  # etiquetamos los nodos
    #nx.draw_networkx_labels(G, pos, font_size=8, font_family='sans-serif')  # etiquetamos los nodos
    #nx.draw_networkx_edge_labels(G, pos, edge_labels = nx.get_edge_attributes(G, 'weight'
    while True:
        neighbors = graph.neighbors(current_node)
        best_neighbor = max(neighbors, key=lambda node: graph.nodes[node]['value'])
        
        #node_color = {current_node: 'r'}
        if graph.nodes[best_neighbor]['value'] > graph.nodes[current_node]['value']:
            current_node = best_neighbor
        else:
            break
        for node in G.nodes():
            node_colors[node] = 'lightblue'
        node_colors[current_node] = 'red'
        plt.clf()
        plt.plot()  # mostramos el grafo
        nx.draw_networkx_nodes(G, pos, node_color=[node_colors[node] for node in G.nodes()])  # dibujamos los nodos
        nx.draw_networkx_edges(G, pos, edge_color='black')  # dibujamos las aristas
        nx.draw_networkx_labels(G, pos, font_size=8, font_family='sans-serif', labels = node_labels)  # etiquetamos los nodos
        #nx.draw_networkx_labels(G, pos, font_size=8, font_family='sans-serif')  # etiquetamos los nodos
        #nx.draw_networkx_edge_labels(G, pos, edge_labels = nx.get_edge_attributes(G, 'weight'))

        plt.axis('off')  # ocultamos los ejes
        
        plt.pause(2)
    return current_node


# Ejemplo de uso
G = nx.Graph()
#G.add_nodes_from([(1, {'value': 10}), (2, {'value': 80}), (3, {'value': 12})])
#G.add_edges_from([(1, 2), (1, 3)])

# Generar grafo aleatorio
num_nodes = 50  # número de nodos
prob_conn = 0.5  # probabilidad de conexión
G = nx.gnp_random_graph(num_nodes, prob_conn)

# Asignar valores a los nodos
values = [random.randint(1, 100) for _ in range(num_nodes)]  # valores aleatorios entre 1 y 100
node_attrs = {i: {'value': values[i]} for i in range(num_nodes)}
nx.set_node_attributes(G, node_attrs)

node_labels = {}
for node in G.nodes():
    node_labels[node] = f"{node}\nValue: {G.nodes[node]['value']}"

# Obtener valores de los nodos
#node_labels = {node: data['value'] for node, data in G.nodes(data=True)}

pos = nx.spring_layout(G)  # posición de los nodos
nx.draw_networkx_nodes(G, pos, node_color='lightblue')  # dibujamos los nodos
nx.draw_networkx_edges(G, pos, edge_color='black')  # dibujamos las aristas
nx.draw_networkx_labels(G, pos, font_size=8, font_family='sans-serif', labels = node_labels)  # etiquetamos los nodos
nx.draw_networkx_labels(G, pos, font_size=8, font_family='sans-serif')  # etiquetamos los nodos
#nx.draw_networkx_edge_labels(G, pos, edge_labels = nx.get_edge_attributes(G, 'weight'))

plt.axis('off')  # ocultamos los ejes

plt.plot()  # mostramos el grafo
plt.pause(1)

start_node = 1
result_node = hill_climbing(G, start_node)
print("El nodo de mayor valor encontrado es:", result_node, 'Value: ', G.nodes[result_node]['value'])
plt.show()

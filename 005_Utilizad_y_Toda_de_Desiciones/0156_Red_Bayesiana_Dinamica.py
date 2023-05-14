"""
Una red bayesiana dinámica (RBD) es una forma de modelar las relaciones causales entre variables en un dominio que
cambia con el tiempo, y se puede aplicar en la búsqueda en grafos al realizar inferencias temporales sobre el estado
futuro de las variables en función de las observaciones actuales y pasadas.
"""

"""
A continuación, se muestra un ejemplo básico de una RBD que modela el estado del clima (soleado, nublado, lluvioso) a lo
largo de varios días. Suponiendo que el clima en un día dado solo depende del clima del día anterior.

Este código creará una representación gráfica de la RBD con los estados del clima como nodos y los arcos que indican la
dependencia temporal entre ellos.

Este es solo un ejemplo básico para ilustrar el concepto. En aplicaciones prácticas, una RBD puede tener más nodos y
conexiones más complejas.
"""

import networkx as nx
import matplotlib.pyplot as plt

# Crear el grafo
G = nx.DiGraph()

# Definir los estados del clima
clima = ['soleado', 'nublado', 'lluvioso']

# Añadir los nodos al grafo
for i in range(len(clima)):
    G.add_node(i, label=clima[i])

# Añadir los arcos al grafo
for i in range(1, len(clima)):
    G.add_edge(i-1, i)

# Dibujar el grafo
labels = nx.get_node_attributes(G, 'label')
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, arrows=True)
nx.draw_networkx_labels(G, pos, labels)
plt.show()

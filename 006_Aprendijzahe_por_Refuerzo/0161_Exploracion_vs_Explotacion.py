"""
La exploración y explotación son dos estrategias utilizadas en la búsqueda en grafos para encontrar soluciones óptimas o
satisfactorias.

La exploración se refiere a la búsqueda de nuevas opciones o caminos en el grafo. Durante la exploración, se pueden
visitar nodos no explorados previamente, expandiendo así el espacio de búsqueda y buscando posibles soluciones.

Por otro lado, la explotación se centra en aprovechar la información ya conocida para elegir las mejores opciones en
cada paso. Se utilizan heurísticas o información previa para tomar decisiones informadas y seleccionar los caminos más
prometedores hacia la solución.

En resumen, la exploración se enfoca en la expansión y descubrimiento de nuevas opciones, mientras que la explotación
se centra en el aprovechamiento de información conocida para seleccionar las mejores opciones. Ambas estrategias son
importantes y pueden combinarse de manera inteligente en la búsqueda en grafos para encontrar soluciones eficientes.
"""

"""
En este ejemplo, la clase Graph representa un grafo y tiene dos métodos: explore y exploit. El método explore implementa
la estrategia de exploración, donde se visitan todos los nodos del grafo de forma recursiva. El método exploit
implementa la estrategia de explotación, donde se selecciona el vecino con el valor máximo y se continúa explorando
desde ese nodo.

Al ejecutar el código, se verá la salida que muestra los nodos que se están explorando o explotando.
"""

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination):
        if source in self.graph:
            self.graph[source].append(destination)
        else:
            self.graph[source] = [destination]

    def explore(self, node):
        print("Exploring node:", node)

        if node in self.graph:
            neighbors = self.graph[node]
            for neighbor in neighbors:
                self.explore(neighbor)

    def exploit(self, node):
        print("Exploiting node:", node)

        if node in self.graph:
            neighbors = self.graph[node]
            best_neighbor = max(neighbors)  # Ejemplo de explotación: selecciona el vecino con el valor máximo
            self.exploit(best_neighbor)

# Crear un grafo de ejemplo
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)
graph.add_edge(3, 7)

# Ejemplo de exploración
print("=== Exploración ===")
graph.explore(1)

# Ejemplo de explotación
print("=== Explotación ===")
graph.exploit(1)

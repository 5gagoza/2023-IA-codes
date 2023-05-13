"""
Los mapas autoorganizados de Kohonen, también conocidos 
como SOM (Self-Organizing Maps), son una técnica de aprendizaje 
no supervisado utilizada en el procesamiento de datos multidimensionales. 
Estos mapas agrupan los datos en regiones cercanas en función de 
sus características similares, permitiendo la visualización y el análisis de datos complejos
"""
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
from minisom import MiniSom
import matplotlib.pyplot as plt

# Cargar el conjunto de datos Iris
data = load_iris()
X = data.data
y = data.target

# Normalizar los datos en un rango de [0, 1]
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

# Definir las dimensiones del mapa autoorganizado
som_shape = (10 , 10)

# Crear e inicializar el mapa autoorganizado de Kohonen
som = MiniSom(som_shape[0], som_shape[1], X.shape[1], sigma=0.3, learning_rate=0.7)
som.random_weights_init(X)
som.train_random(X, 100)

# Visualizar los resultados en un mapa de calor
plt.figure(figsize=(som_shape[0], som_shape[1]))
plt.pcolor(som.distance_map().T, cmap='cool_r')
plt.colorbar()

# Asignar etiquetas a los nodos del mapa
target_names = data.target_names
for i, x in enumerate(X):
    w = som.winner(x)
    plt.text(w[0] + 0.5, w[1] + 0.5, target_names[y[i]], ha='center', va='center', color='black', fontweight='bold')

plt.xticks(np.arange(0, som_shape[0] + 1, 1))
plt.yticks(np.arange(0, som_shape[1] + 1, 1))
plt.grid(visible=True)
plt.show()

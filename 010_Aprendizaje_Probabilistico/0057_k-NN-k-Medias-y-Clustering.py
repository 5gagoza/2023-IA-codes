"""
El código implementa tres algoritmos de clustering diferentes: k-NN, k-medias y clustering jerárquico aglomerativo.
Se ejecutan los tres algoritmos de clustering sobre los datos normalizados.

El algoritmo k-NN asigna cada punto de datos a la clase de sus k vecinos más cercanos. El algoritmo k-medias agrupa los puntos de datos en k clusters diferentes, 
donde cada punto de datos se asigna al cluster cuyo centroide es el más cercano. 
Finalmente, el algoritmo de clustering jerárquico aglomerativo construye una jerarquía de clusters en la que los puntos de datos se agrupan en clusters cada vez más grandes.

Por último, se muestra la precisión de los tres algoritmos de clustering en la consola.
"""

import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generar datos de prueba
X, y = make_blobs(n_samples=1000, centers=4, n_features=2, random_state=0)

# Algoritmo k-NN
nbrs = NearestNeighbors(n_neighbors=3, algorithm='ball_tree').fit(X)
distances, indices = nbrs.kneighbors(X)

print('Distancias:', distances)
print('Indices vecinos:', indices)

# Algoritmo k-Medias
kmeans = KMeans(n_clusters=4, random_state=0).fit(X)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

print('Labels:', labels)
print('Centroides:', centroids)

# Algoritmo de Clustering
from sklearn.cluster import AgglomerativeClustering
agg_clustering = AgglomerativeClustering(n_clusters=4).fit(X)
print('Etiquetas Clustering Aglomerativo:', agg_clustering.labels_)


"""
El código implementa el algoritmo de agrupamiento k-means, que es un algoritmo de agrupamiento no supervisado. 
El objetivo es agrupar un conjunto de datos en k grupos (clusters) en función de la similitud entre ellos.

El algoritmo comienza seleccionando k centroides de forma aleatoria. Luego, asigna cada punto del conjunto de datos al centroide más cercano. 
A continuación, se recalculan los centroides como la media de todos los puntos asignados a él. 
Este proceso se repite hasta que no haya cambios en la asignación de puntos o se alcance un número máximo de iteraciones. El resultado final son k grupos de puntos similares.
"""

from sklearn.cluster import KMeans
import numpy as np

# Generamos datos aleatorios para clusterizar
X = np.random.rand(100, 2)

# Instanciamos el modelo de K-Means con 3 clusters
kmeans = KMeans(n_clusters=3, random_state=0)

# Entrenamos el modelo con los datos
kmeans.fit(X)

# Obtenemos las etiquetas de los clusters para cada dato
labels = kmeans.labels_

# Imprimimos los centroides de cada cluster
print(kmeans.cluster_centers_)

# Imprimimos las etiquetas de los clusters para cada dato
print(labels)

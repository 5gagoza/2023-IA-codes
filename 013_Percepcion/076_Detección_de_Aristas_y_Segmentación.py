"""
La detección de aristas es una técnica utilizada para identificar los bordes 
y los contornos de objetos en una imagen. Se basa en la detección de cambios 
abruptos en la intensidad de los píxeles. La segmentación se refiere a la tarea 
de dividir una imagen en regiones o segmentos significativos. Son pasos
fundamentales para el análisis de imágenes y el reconocimiento de objetos.
"""
import cv2
import matplotlib.pyplot as plt

# Cargar la imagen
image = cv2.imread("imagen.jpg")

# Convertir la imagen a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar el algoritmo de Canny
edges = cv2.Canny(gray_image, 100, 200)

# Mostrar las imágenes
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Imagen Original")

plt.subplot(1, 2, 2)
plt.imshow(edges, cmap="gray")
plt.title("Detección de Aristas")

plt.show()

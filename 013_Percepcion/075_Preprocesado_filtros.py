"""
El preprocesamiento se refiere a las técnicas y los métodos utilizados para 
preparar los datos de entrada antes de ser procesados por un sistema de percepción.
Incluye tareas como la normalización, la reducción de ruido, el filtrado y la mejora 
de la calidad de la imagen o la señal de entrada. Se busca mejorar la calidad de los 
datos y resaltar características relevantes para un procesamiento más eficiente y preciso.
"""
import cv2
import matplotlib.pyplot as plt

# Cargar la imagen
image = cv2.imread("imagen.jpg")

# Convertir la imagen a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar el filtro de desenfoque (blur)
blurred_image = cv2.blur(gray_image, (10, 15))

# Mostrar las imágenes
plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap="gray")
plt.title("Imagen en escala de grises")

plt.subplot(1, 2, 2)
plt.imshow(blurred_image, cmap="gray")
plt.title("Imagen con filtro de desenfoque")

plt.show()

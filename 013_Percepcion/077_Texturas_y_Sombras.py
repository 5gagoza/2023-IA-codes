"""
El análisis de texturas se enfoca en la identificación y el modelado 
de los patrones repetitivos y las estructuras de textura en una imagen.
Las sombras son áreas oscuras o proyecciones causadas por la obstrucción 
de la luz en una imagen. Es importante para el reconocimiento de objetos, 
la detección de anomalías y otras tareas de análisis de imágenes.
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
image = cv2.imread("imagen.jpg", cv2.IMREAD_GRAYSCALE)

# Calcular la transformada de Fourier de la imagen
fft_image = np.fft.fft2(image)

# Calcular el espectro de potencia
power_spectrum = np.abs(fft_image) ** 2

# Aplicar un umbral para detectar sombras y texturas
threshold = np.max(power_spectrum) * 0.01
mask = power_spectrum > threshold

# Aplicar la transformada inversa de Fourier
filtered_image = np.fft.ifft2(fft_image * mask)

# Mostrar las imágenes
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Imagen Original")

plt.subplot(1, 2, 2)
plt.imshow(np.abs(filtered_image), cmap='gray')
plt.title("Detección de Texturas y Sombras")

plt.show()

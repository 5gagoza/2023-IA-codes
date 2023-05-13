import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la distribución binomial
n = 10  # Número de ensayos
p = 0.5  # Probabilidad de éxito

# Generar valores de x (número de éxitos) y sus probabilidades correspondientes
x = np.arange(0, n+1)
probabilidades = np.array([np.math.comb(n, k) * p**k * (1-p)**(n-k) for k in x])

# Graficar la distribución de probabilidad binomial
plt.bar(x, probabilidades)
plt.xlabel('Número de éxitos')
plt.ylabel('Probabilidad')
plt.title('Distribución de Probabilidad Binomial (n=10, p=0.5)')
plt.show()

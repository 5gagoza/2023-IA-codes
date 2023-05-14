"""
Generación de un grafico en 2D por desconocer el uso de recurso necesario 
de recursos por parte del computador
"""
import matplotlib.pyplot as plt

# Datos del gráfico
x = [1, 1.5, 3, 4, 5]
y = [2, 4, 6, 7, 10]

# Crear el gráfico
plt.plot(x, y)

# Personalizar el gráfico
plt.title("Gráfico 2D")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Mostrar el gráfico
plt.show()

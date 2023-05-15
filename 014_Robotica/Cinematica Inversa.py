
import math

#Longitudes de las dos articulaciones del robot
L1 = 2
L2 = 3

#Coordenadas del objetivo en el plano
x = 4
y = 2

#Calcular la distancia del objetivo al origen del plano
r = math.sqrt(x**2 + y**2)

#Calcular el ángulo entre el objetivo y el eje x
theta1 = math.atan2(y, x)

#Calcular el ángulo entre las dos articulaciones del robot
theta2 = math.acos((L1**2 + L2**2 - r**2) / (2 * L1 * L2))

#Calcular el ángulo de la primera articulación del robot
phi1 = theta1 + math.atan2(L2 * math.sin(theta2), L1 + L2 * math.cos(theta2))

#Calcular el ángulo de la segunda articulación del robot
phi2 = math.pi - theta2

#Imprimir los ángulos de las articulaciones del robot
print("Articulación 1: ", phi1)
print("Articulación 2: ", phi2)

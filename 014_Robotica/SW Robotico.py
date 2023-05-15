
import pygame
import random

import pygame
import random
import threading
import sys

# Inicializar Pygame
pygame.init()

# Crear una ventana de Pygame
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ejemplo de SW robótica')

# Crear una posición aleatoria para el robot
x, y = random.randint(0, width), random.randint(0, height)

# Definir el controlador del robot
def controller():
    global x, y
    while True:
        # Obtener la entrada del usuario
        keys = pygame.key.get_pressed()

        # Actualizar la posición del robot en función de la entrada del usuario
        if keys[pygame.K_LEFT]:
            x -= 1
        if keys[pygame.K_RIGHT]:
            x += 1
        if keys[pygame.K_UP]:
            y -= 1
        if keys[pygame.K_DOWN]:
            y += 1

        # Limitar la posición del robot a la ventana
        x = max(0, min(x, width))
        y = max(0, min(y, height))

# Crear un hilo separado para ejecutar el controlador del robot
thread = threading.Thread(target=controller)
thread.start()

# Ejecutar la simulación
while True:
    # Dibujar el robot en la pantalla
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 20)
    pygame.display.flip()

    # Esperar un tiempo antes de actualizar la pantalla
    pygame.time.wait(10)

    # Comprobar si se ha pulsado el botón de salir
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

import pygame
import sys
import math

# Inicializar Pygame
pygame.init()

# Configurar ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Trayectoria Circular")

# Colores
NEGRO = (0, 0, 0)
GRIS = (150, 150, 150)
BLANCO = (255, 255, 255)
colores = [NEGRO, GRIS, BLANCO]  # Ciclo de colores

# Centro y parámetros del movimiento circular
centro_x, centro_y = 400, 300
radio = 150
angulo = 0
velocidad_angular = 0.03  # velocidad del movimiento circular

# Rectángulo
rect_ancho, rect_alto = 80, 50

# Variables para cambio rápido de color
indice_color = 0
cambio_tiempo = 0  # contador de tiempo
velocidad_color = 0.05  # cuanto menor, más rápido cambia de color

# Bucle principal
clock = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento circular
    rect_x = centro_x + radio * math.cos(angulo) - rect_ancho / 2
    rect_y = centro_y + radio * math.sin(angulo) - rect_alto / 2
    angulo += velocidad_angular

    # Cambio rápido de color 
    cambio_tiempo += velocidad_color
    if cambio_tiempo >= 1:
        cambio_tiempo = 0
        indice_color = (indice_color + 1) % len(colores)

    # Dibujar todo
    ventana.fill((0, 235, 0)) 
    pygame.draw.rect(ventana, colores[indice_color], (rect_x, rect_y, rect_ancho, rect_alto))

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

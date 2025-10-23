import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Diseño geométrico: Círculos concéntricos")

# Definir colores (puedes personalizarlos)
colors = [
    (255, 0, 0),      # Rojo
    (255, 165, 0),    # Naranja
    (255, 255, 0),    # Amarillo
    (0, 128, 0),      # Verde
    (0, 0, 255)       # Azul
]

# Coordenadas del centro
center_x = width // 2
center_y = height // 2

# Radios crecientes
radii = [20, 40, 60, 80, 100]

# Bucle principal
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fondo blanco
    screen.fill((255, 255, 255))

    # Dibujar los círculos concéntricos
    for i in range(5):
        pygame.draw.circle(screen, colors[i], (center_x, center_y), radii[i], 3)
        # El último parámetro (3) es el grosor del borde del círculo. 
        # Si lo quitas o lo cambias a 0, se rellena el círculo.

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

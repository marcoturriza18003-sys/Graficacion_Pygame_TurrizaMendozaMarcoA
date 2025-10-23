import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración
cols, rows = 8, 8            # 8x8 tablero
square_size = 80             # tamaño de cada casilla en píxeles
width, height = cols * square_size, rows * square_size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tablero de ajedrez 8x8")

# Colores (puedes cambiarlos)
WHITE = (245, 245, 245)
BLACK = (30, 30, 30)

# Bucle principal
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dibujar tablero: recorremos filas y columnas
    for row in range(rows):
        for col in range(cols):
            # Alternar color según la suma de fila+col
            if (row + col) % 2 == 0:
                color = WHITE
            else:
                color = BLACK

            rect = pygame.Rect(col * square_size, row * square_size, square_size, square_size)
            pygame.draw.rect(screen, color, rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

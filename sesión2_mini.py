import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Casa con cambio de color")

# Colores
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
YELLOW = (255, 255, 100)
PURPLE = (180, 0, 180)
ORANGE = (255, 165, 0)

# Color inicial de la casa
house_color = ORANGE

# Coordenadas base de la casa
house_x, house_y = 300, 300
house_width, house_height = 200, 150

# Bucle principal
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Cambiar color de la casa al presionar teclas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_v:   # Verde
                house_color = GREEN
            elif event.key == pygame.K_a: # Amarillo
                house_color = YELLOW
            elif event.key == pygame.K_m: # Morado
                house_color = PURPLE
            elif event.key == pygame.K_o: # Naranja
                house_color = ORANGE

    # Fondo
    screen.fill(WHITE)

    # Dibujar cuerpo de la casa (rectángulo)
    pygame.draw.rect(screen, house_color, (house_x, house_y, house_width, house_height))

    # Dibujar techo (triángulo)
    roof_points = [
        (house_x - 20, house_y),                        # esquina izquierda
        (house_x + house_width + 20, house_y),          # esquina derecha
        (house_x + house_width // 2, house_y - 100)     # punta del techo
    ]
    pygame.draw.polygon(screen, (139, 69, 19), roof_points)  # marrón

    # Dibujar ventanas (círculos)
    pygame.draw.circle(screen, (173, 216, 230), (house_x + 50, house_y + 50), 20)  # izquierda
    pygame.draw.circle(screen, (173, 216, 230), (house_x + 150, house_y + 50), 20) # derecha

    # Dibujar puerta
    pygame.draw.rect(screen, (100, 50, 0), (house_x + 85, house_y + 80, 30, 70))

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

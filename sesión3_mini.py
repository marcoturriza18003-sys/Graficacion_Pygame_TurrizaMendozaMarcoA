import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Movimiento con rastro de círculos")

# Colores
FONDO = (30, 30, 30)
RECT_COLOR = (0, 200, 255)
CIRCULO_COLOR = (255, 255, 0)

# Configuración del rectángulo
rect_x = 400
rect_y = 300
rect_ancho = 60
rect_alto = 40
velocidad = 5

# Lista para almacenar las posiciones del rastro
rastro = []
max_rastro = 100  # número máximo de círculos que se mostrarán

# Reloj para controlar FPS
clock = pygame.time.Clock()

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento con teclas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        rect_x -= velocidad
    if teclas[pygame.K_RIGHT]:
        rect_x += velocidad
    if teclas[pygame.K_UP]:
        rect_y -= velocidad
    if teclas[pygame.K_DOWN]:
        rect_y += velocidad

    # Evitar que se salga de la ventana
    if rect_x < 0:
        rect_x = 0
    if rect_x + rect_ancho > ANCHO:
        rect_x = ANCHO - rect_ancho
    if rect_y < 0:
        rect_y = 0
    if rect_y + rect_alto > ALTO:
        rect_y = ALTO - rect_alto

    # Agregar la posición actual del centro del rectángulo a la lista del rastro
    centro_x = rect_x + rect_ancho // 2
    centro_y = rect_y + rect_alto // 2
    rastro.append((centro_x, centro_y))

    # Limitar el tamaño del rastro
    if len(rastro) > max_rastro:
        rastro.pop(0)

    # Dibujar el fondo
    ventana.fill(FONDO)

    # Dibujar los círculos del rastro
    for pos in rastro:
        pygame.draw.circle(ventana, CIRCULO_COLOR, pos, 5)

    # Dibujar el rectángulo
    pygame.draw.rect(ventana, RECT_COLOR, (rect_x, rect_y, rect_ancho, rect_alto))

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)

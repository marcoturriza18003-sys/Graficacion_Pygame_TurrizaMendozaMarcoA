import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 600, 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Movimiento con cambio de color al tocar bordes")

# Colores
ROJO_FONDO = (255, 0, 0)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Configuración del cuadrado
rect_x = 250
rect_y = 150
rect_tamano = 80
velocidad = 5
color_rect = BLANCO

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

    # Verificar contacto con bordes y evitar salida
    tocado_borde = False

    if rect_x < 0:
        rect_x = 0
        tocado_borde = True
    elif rect_x + rect_tamano > ANCHO:
        rect_x = ANCHO - rect_tamano
        tocado_borde = True

    if rect_y < 0:
        rect_y = 0
        tocado_borde = True
    elif rect_y + rect_tamano > ALTO:
        rect_y = ALTO - rect_tamano
        tocado_borde = True

    # Cambiar color si toca un borde
    if tocado_borde:
        if color_rect == BLANCO:
            color_rect = NEGRO
        else:
            color_rect = BLANCO

    # Dibujar fondo y cuadrado
    ventana.fill(ROJO_FONDO)
    pygame.draw.rect(ventana, color_rect, (rect_x, rect_y, rect_tamano, rect_tamano))

    # Actualizar pantalla
    pygame.display.flip()

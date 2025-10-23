import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la ventana
ANCHO, ALTO = 600, 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Cambio de color con la tecla C")

# Definir colores (RGB)
VERDE = (0, 255, 100)
MORADO = (150, 0, 255)

# Color inicial
color_fondo = VERDE

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Detectar si se presiona una tecla
        if evento.type == pygame.KEYDOWN:
            # Si la tecla es C o c
            if evento.key == pygame.K_c:
                # Cambiar el color de fondo
                if color_fondo == VERDE:
                    color_fondo = MORADO
                else:
                    color_fondo = VERDE

    # Rellenar la ventana con el color actual
    ventana.fill(color_fondo)

    # Actualizar la pantalla
    pygame.display.flip()

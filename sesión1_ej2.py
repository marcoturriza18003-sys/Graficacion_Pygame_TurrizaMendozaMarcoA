import pygame

# Inicializar Pygame
pygame.init()

# Ventana de 1000x800 píxeles
ventana = pygame.display.set_mode((1000, 800))

# Título personalizado
pygame.display.set_caption("EJEMPLO 2 (CERRAR VENTANA CON ESC)")

# Color de fondo rojo vino (RGB)
color_fondo = (128, 0, 32)

# Bucle para cerrar ventana
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        # Si se cierra la ventana
        if evento.type == pygame.QUIT:
            corriendo = False
        # Si se presiona una tecla
        if evento.type == pygame.KEYDOWN:
            # Si la tecla es ESC (Escape)
            if evento.key == pygame.K_ESCAPE:
                corriendo = False
    
    # Rellenar el fondo
    ventana.fill(color_fondo)
    pygame.display.update()

# Salir de Pygame
pygame.quit()

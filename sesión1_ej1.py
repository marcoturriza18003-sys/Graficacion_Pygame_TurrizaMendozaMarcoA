import pygame

# Inicializar Pygame
pygame.init()

# Ventana de 1000x800 píxeles
ventana = pygame.display.set_mode((1000, 800))

# Título personalizado
pygame.display.set_caption("Mi primer programa gráfico")

# Color de fondo rojo vino (RGB)
color_fondo = (128, 0, 32)

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    
    # Rellenar el fondo con el color rojo vino
    ventana.fill(color_fondo)
    
    # Actualizar la ventana
    pygame.display.update()

# Salir de Pygame
pygame.quit()

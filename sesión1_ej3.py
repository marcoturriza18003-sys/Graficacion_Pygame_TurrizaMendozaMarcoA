import pygame
import time

# Inicializar Pygame
pygame.init()

# Ventana de 1000x800 píxeles
ventana = pygame.display.set_mode((1000, 800))

# Título personalizado
pygame.display.set_caption("EJEMPLO 3 (CERRAR VENTANA A LOS 300 FRAMES)")

# Color de fondo rojo vino (RGB)
color_fondo = (128, 0, 32)

# Mostrar 300 frames
for frame in range(1, 301):
    print(f"Frame: {frame}")
    ventana.fill(color_fondo)
    pygame.display.update()
    time.sleep(0.01)  # Pequeña pausa para que se note el cambio de frame

# Cerrar Pygame
pygame.quit()


import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Configuración de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bola moviéndose de derecha a izquierda")

# Definir la clase Bola
class Bola(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.right = SCREEN_WIDTH
        self.rect.centery = random.randint(0, SCREEN_HEIGHT)
        self.velocidad_x = 5  # Velocidad en píxeles por fotograma

    def update(self):
        self.rect.x -= self.velocidad_x
        if self.rect.right <= 0:
            self.reset()

# Crear el sprite de la bola
bola = Bola()

# Crear un grupo de sprites y añadir la bola al grupo
all_sprites = pygame.sprite.Group()
all_sprites.add(bola)

# Bucle principal del juego
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar la posición de la bola
    all_sprites.update()

    # Limpiar la pantalla
    screen.fill(BLACK)

    # Dibujar todos los sprites
    all_sprites.draw(screen)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    clock.tick(60)

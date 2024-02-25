from .utils import *
import random


class Goku_nube(pg.sprite.Sprite):
    def __init__(self, pantalla):
        super().__init__()
        self.pantalla = pantalla
        self.image = pg.image.load("PYGAME_APP/images/GOKU/GOKU_NUBE22.png")
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.centery = pantalla.get_height() // 2
        self.vidas = 3
        self.speed = 5

    def update(self, dy):

        self.rect.y += dy * self.speed  
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > self.pantalla.get_height():
            self.rect.bottom = self.pantalla.get_height()

    def dibujar(self):
        self.pantalla.blit(self.image, self.rect)

    def mover(self):
        botones = pg.key.get_pressed()
        if botones[pg.K_UP]:
            self.update(-1)
        if botones[pg.K_DOWN]:
            self.update(1)


    def Vidas(self,surface):

        CORAZON = pg.image.load(IMG_CORAZON)
        x = 15
        y = 15
        
        for _ in range(self.vidas):
            surface.blit(pg.transform.scale(CORAZON, (CORAZON_ANCHO, CORAZON_ALTO)), (x, y))
            x += CORAZON_ANCHO + 5



    
class Obstaculos(pg.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
            super().__init__()
            self.image_choices = ["PYGAME_APP/images/BOLAS/BOLA_ENERGIA00.png", "PYGAME_APP/images/BOLAS/BOLA_ROJA00.png"]
            self.image = pg.image.load(random.choice(self.image_choices))
            self.rect = self.image.get_rect()
            self.rect.x = screen_width
            self.rect.y = random.randint(0, screen_height - self.rect.height)
            self.speed = random.randint(2, 6)
            

    def update(self):
        self.rect.x -= self.speed 


class Explosion(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = []
        for i in range(1, 6):
            img = pg.image.load(f"PYGAME_APP/images/EXPLOSION/EXPLOSION.png")
            img = pg.transform.scale(img, (64, 64))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0
        self.sound = pg.mixer.Sound("PYGAME_APP/songs/SONIDO_COLISION.mp3")
        self.sound.set_volume(0.3)
        self.sound.play()

    def update(self):
        self.counter += 1
        if self.counter % 3 == 0:
            self.index += 1
            if self.index >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.index]




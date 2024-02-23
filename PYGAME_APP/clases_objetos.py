from .utils import *
import random


class GOKU_NUBE:
    def __init__(self,pos_x,pos_y,color=COLOR_BLANCO,w=30,h=110,vy=5):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w = w
        self.h = h
        self.vy = vy
        self.Goku = pg.image.load(IMG_GOKU)
        self._direccion = ''


    @property
    def direccion(self):
        return self._direccion
    
    @direccion.setter
    def direccion(self,valor):
        self._direccion = valor

    def dibujar(self,surface):
        surface.blit(self.Goku, (self.pos_x - (self.w // 2), self.pos_y - (self.h // 2)))

    def mover(self,teclado_arriba,teclado_abajo,y_max= ALTO, y_min=ALTO_MIN):
        estado_teclado = pg.key.get_pressed()

        if estado_teclado[teclado_arriba] == True and self.pos_y > y_min+(self.h//2):
            self.pos_y -= 1
            self.vy = 5
        if estado_teclado[teclado_abajo] == True and self.pos_y < y_max-(self.h//2):
            self.pos_y += 1
            self.vy = 5


    @property
    def derecha(self):
        return self.pos_x + (self.w//2)
    
    @property
    def izquierda(self):
        return self.pos_x - (self.w//2)  
    
    @property
    def arriba(self):
        return self.pos_y - (self.h//2)
    
    @property
    def abajo(self):
        return self.pos_y + (self.h//2) 
    

 
class Bola1:
    def __init__(self,pos_x, pos_y,color=COLOR_BLANCO,radio=1):
            self.pos_x = pos_x
            self.pos_y = pos_y
            self.color = color
            self.radio = radio
            self.vx = random.randint(1,2)
            self.vy = random.randint(1,2)
            self.sonido = pg.mixer.Sound(SONIDO_EXPLOSION)
            self.pelota = pg.image.load(IMG_BOLA2)


    def dibujar(self,surface):
 
        surface.blit(self.pelota,(self.pos_x,self.pos_y) )   
         

    
    
    def mover(self):
        self.pos_x -= self.vx
        
        if self.pos_x + self.radio <= -100:
            self.pos_x = ANCHO
            self.pos_y = random.randint(0,550)
            self.vx = random.randint(1,2)
            self.vy = random.randint(1,2)


class Bola2:
    def __init__(self,pos_x, pos_y,color=COLOR_BLANCO,radio=1):
            self.pos_x = pos_x
            self.pos_y = pos_y
            self.color = color
            self.radio = radio
            self.vx = random.randint(1,2)
            self.vy = random.randint(1,2)
            self.sonido = pg.mixer.Sound(SONIDO_EXPLOSION)
            self.pelota = pg.image.load(IMG_BOLA1)


    def dibujar(self,surface):
 
        surface.blit(self.pelota,(self.pos_x,self.pos_y) )   
         

    
    def mover(self):
        self.pos_x -= self.vx
        
        if self.pos_x + self.radio <= -100:
            self.pos_x = ANCHO
            self.pos_y = random.randint(0,515)
            self.vx = random.randint(1,2)
            self.vy = random.randint(1,2)
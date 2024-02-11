from .utils import *


class GOKU_NUBE:
    def __init__(self,pos_x,pos_y,color=COLOR_BLANCO,w=50,h=50):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w = w
        self.h = h
        self.Goku = pg.image.load(IMG_GOKU)
        self._direccion = ''


    @property
    def direccion(self):
        return self._direccion
    
    @direccion.setter
    def direccion(self,valor):
        self._direccion = valor

    def dibujar(self,surface):
        surface.blit(self.Goku[self.direccion](self.pos_x-(self.w//2)))

    def mover(self,teclado_arriba,teclado_abajo,y_max= ALTO, y_min=ALTO_MIN):
        estado_teclado = pg.key.get_pressed()

        if estado_teclado[teclado_arriba] == True and self.pos_y > y_min+(self.h//2):
            self.pos_y -= 1
        
        if estado_teclado[teclado_abajo] == True and self.pos_y < y_max-(self.h//2):
            self.pos_y += 1


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
    


class BOLA_ENERGIA_1:
    def __init__(self, pos_x, pos_y, color = COLOR_BLANCO, radio=20, vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.radio = radio
        self.vx = vx
        self.vy = vy
        self.sonido =  pg.mixer.Sound(SONIDO_EXPLOSION)
        self.imagenBola1 = pg.image.load(IMG_BOLA1)
        self.imagenBola2 = pg.image.load(IMG_BOLA2)
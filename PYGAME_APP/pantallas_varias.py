from PYGAME_APP.clases_objetos import GOKU_NUBE, Bola1, Bola2
from PYGAME_APP.utils import *


class Menu:
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("MENU INICIAL")
        self.tasa_refresco = pg.time.Clock()
        self.sonido = pg.mixer.Sound(SONIDO_MENU)
        self.imagenFondo = pg.image.load(IMG_FONDO_MENU)
        

    def bucle_pantalla(self):
        game_over = True
        while game_over:
            pg.mixer.Sound.set_volume(self.sonido, 0.02)
            pg.mixer.Sound.play(self.sonido)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True
            
            botones = pg.key.get_pressed()
            if botones[pg.K_RETURN]:
                pg.mixer.Sound.stop(self.sonido)
                return "prologo"
            
            elif botones[pg.K_r]:
                pg.mixer.Sound.stop(self.sonido)
                return "record"
          
            
            self.pantalla_principal.blit(self.imagenFondo,(0,0))

           

            pg.display.flip()

class Prologo:
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Prologo")
        self.tasa_refresco = pg.time.Clock()
        self.imagenFondo = pg.image.load(IMG_APORELLOS)
        self.sonido = pg.mixer.Sound(SONIDO_PROLOGO)

    
    def bucle_pantalla(self):
        game_over = True
        while game_over:
            pg.mixer.Sound.set_volume(self.sonido, 0.02)
            pg.mixer.Sound.play(self.sonido)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True
            
            botones = pg.key.get_pressed()
            if botones[pg.K_RETURN]:
                pg.mixer.Sound.stop(self.sonido)
                return "partida"
            

            
            
            self.pantalla_principal.blit(self.imagenFondo,(0,0))


            pg.display.flip()


class Partida:
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Final")
        self.tasa_refresco = pg.time.Clock()
        self.imagenFondo = pg.image.load(IMG_TERRENO_JUEGO1)
        
        
        self.bola = Bola1 (ANCHO,ALTO//2,COLOR_BLANCO)
        self.bola1 = Bola2 (ANCHO,ALTO//4,COLOR_BLANCO)
        self.goku = GOKU_NUBE (15, ALTO//2)



    def bucle_pantalla(self):
        game_over = True
        self.valor_tasa= self.tasa_refresco.tick()
        while game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True
            
            self.pantalla_principal.blit(self.imagenFondo,(0,0))
            self.Vidas()
            self.goku.dibujar(self.pantalla_principal)
            self.bola.dibujar(self.pantalla_principal)
            self.bola1.dibujar(self.pantalla_principal)
            self.goku.mover(pg.K_UP,pg.K_DOWN)
            self.bola.mover()
            self.bola1.mover()
            self.tasa_refresco.tick(60)



            pg.display.flip()         
        
    

    def Vidas(self):

        CORAZON = pg.image.load(IMG_CORAZON)
        x = 10
        y = 10
        
        for _ in range(3):
            self.pantalla_principal.blit(pg.transform.scale(CORAZON, (CORAZON_ANCHO, CORAZON_ALTO)), (x, y))
            x += CORAZON_ANCHO + 5


class Final:
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Final")
        self.tasa_refresco = pg.time.Clock()
        self.imagenFondo = pg.image.load(IMG_BOLAS_DRAGON)
        self.sonido = pg.mixer.Sound(SONIDO_FINAL)

    
    def bucle_pantalla(self):
        game_over = True
        while game_over:
            pg.mixer.Sound.set_volume(self.sonido,0.02)
            pg.mixer.Sound.play(self.sonido)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    pg.mixer.Sound.stop(self.sonido)
                    return True
            

            
            
            self.pantalla_principal.blit(self.imagenFondo,(0,0))


            pg.display.flip()

                










    
    
    
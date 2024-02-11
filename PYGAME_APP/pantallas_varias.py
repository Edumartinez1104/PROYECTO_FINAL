from PYGAME_APP.clases_objetos import GOKU_NUBE
from PYGAME_APP.utils import *

class Partida:
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode( (ANCHO,ALTO) )
        pg.display.set_caption("DRAGON BALL")
        self.tasa_refresco = pg.time.Clock()
        self.FondoPartida = pg.image.load(IMG_TERRENO_JUEGO1)




class MENU:
     def __init__(self):
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("MENU INICIAL")
        self.tasa_refresco = pg.time.Clock()
        self.imagenFondo = pg.image.load(IMG_FONDO_MENU)
        self.fuente = pg.font.Font(FUENTE1,30)
        self.sonido = pg.mixer.Sound(SONIDO_MENU)

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
                return "prologo1"
            elif botones[pg.K_r]:
                pg.mixer.Sound.stop(self.sonido)
                return "record"
          
            
            self.pantalla_principal.blit(self.imagenFondo,(0,0))

            texto_menu_partida = self.fuente.render("PULSA ENTER PARA JUGAR",True,COLOR_NEGRO)
            texto_menu_record = self.fuente.render("PULSA R PARA VER LAS MEJORES PUNTUACIONES",True,COLOR_NEGRO)
            self.pantalla_principal.blit(texto_menu_partida,(200,ALTO//2))
            self.pantalla_principal.blit(texto_menu_record,(10,ALTO//2+40))

            pg.display.flip()

class PROLOGO1:
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("HISTORIA")
        self.tasa_refresco = pg.time.Clock()
        self.imagenFondo = pg.image.load(IMG_FONDO_NAMEK)
        self.fuente = pg.font.Font(FUENTE1,30)
        self.sonido = pg.mixer.Sound(SONIDO_PROLOGO)

    
    def bucle_pantalla(self):
        game_over = True
        while game_over:
            pg.mixer.Sound.set_volume(self.sonido,0.02)
            pg.mixer.Sound.play(self.sonido)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True
                

            botones = pg.key.get_pressed()
            if botones[pg.K_1]:

                return "partida"
            
            self.pantalla_principal.blit(self.imagenFondo,(0,0))
            texto_prologo1 = self.fuente.render("DEBEMOS ENCONTRAR LAS BOLAS DE DRAGON URGENTEMENTE,",True,COLOR_BLANCO)
            texto_prologo11 = self.fuente.render("SE ENCUENTRAN EN EL PLANETA NAMEK..",True,COLOR_BLANCO)
            texto_prologo111 = self.fuente.render("Pulsa 1 para continuar..", True,COLOR_BLANCO)

            self.pantalla_principal.blit(texto_prologo1,(30,450))
            self.pantalla_principal.blit(texto_prologo11,(140,500))
            self.pantalla_principal.blit(texto_prologo111,(180,550))
            pg.display.flip()

class PROLOGO2():
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("HISTORIA")
        self.tasa_refresco = pg.time.Clock()
        self.imagenFondo2 = pg.image.load(IMG_FONDO_NAMEKIANOS)
        self.fuente = pg.font.Font(FUENTE1,30)
   
    def bucle_pantalla(self):
        game_over = True
        while game_over:

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True
                
            botones = pg.key.get_pressed()
            if botones[pg.K_2]:
                
                return "partida"

            
            self.pantalla_principal.blit(self.imagenFondo2,(0,0))
            texto_prologo2 = self.fuente.render("OH NO! UNOS NAMEKIANOS SE INTERPONEN EN TU CAMINO",True,COLOR_NEGRO)
            texto_prologo22 = self.fuente.render("ESQUIVA SUS ATAQUES PARA PODER LLEGAR A TU DESTINO",True,COLOR_NEGRO)
            texto_prologo222 = self.fuente.render("Pulsa 2 para continuar..", True,COLOR_NEGRO)
            self.pantalla_principal.blit(texto_prologo2,(80,450))
            self.pantalla_principal.blit(texto_prologo22,(60,500))
            self.pantalla_principal.blit(texto_prologo222,(90,550))

            pg.display.flip()

class PROLOGO3():
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("HISTORIA")
        self.tasa_refresco = pg.time.Clock()
        self.imagenFondo3 = pg.image.load(IMG_APORELLOS)
        self.fuente = pg.font.Font(FUENTE1,40)
        self.sonido = pg.mixer.Sound(SONIDO_PROLOGO)
        
   
    def bucle_pantalla(self):
        game_over = True
        while game_over:
            pg.mixer.Sound.set_volume(self.sonido,0.02)
            pg.mixer.Sound.play(self.sonido)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True
            
            botones = pg.key.get_pressed()    
            if botones[pg.K_3]:
                pg.mixer.Sound.stop(self.sonido)

                return "partida"


            self.pantalla_principal.blit(self.imagenFondo3,(0,0))
            texto_prologo3 = self.fuente.render("¡¡¡A POR ELLOS!!!", True, COLOR_NEGRO)
            texto_prologo33 = self.fuente.render("¡¡Pulsa 3 para comenzar!!", True, COLOR_NEGRO)
            self.pantalla_principal.blit(texto_prologo3,(300,500))
            self.pantalla_principal.blit(texto_prologo33,(200,550))

            pg.display.flip()
                










    
    
    
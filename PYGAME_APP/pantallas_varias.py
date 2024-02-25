from PYGAME_APP.clases_objetos import Goku_nube, Obstaculos,Explosion
from PYGAME_APP.utils import *
import random


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
        self.pantalla_principal = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("Partida")
        self.tasa_refresco = pg.time.Clock()
        self.imagenFondo = pg.image.load(IMG_TERRENO_JUEGO1)
        self.imagenFondo2 = pg.image.load(IMG_TERRENO_JUEGO2)
        self.goku = Goku_nube(self.pantalla_principal)
        self.grupo_bolas = pg.sprite.Group()
        self.grupo_explosion = pg.sprite.Group()
        self.menu = Menu()
        self.final = Final()
        self.velocidad_obstaculos = 4
        
       
       


    def bucle_pantalla(self):
        game_over = False  
        self.tiempo_restante = 30
        self.tiempo_anterior = pg.time.get_ticks()
        while not game_over and self.tiempo_restante > 0:  
            self.pantalla_principal.blit(self.imagenFondo, (0, 0))
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True  
        





            self.generar_obstaculos()
            self.actualizar_pantalla()
            self.manejar_colisiones()
            
            self.goku.dibujar()
            self.goku.mover()
            self.goku.Vidas(self.pantalla_principal)

            tiempo_actual = pg.time.get_ticks()  # Tiempo actual
            if tiempo_actual - self.tiempo_anterior >= 1000:  # Actualizar cada segundo
                self.tiempo_restante -= 1
                self.tiempo_anterior = tiempo_actual


            font = pg.font.Font(FUENTE1, 36)
            text_surface = font.render(f"Tiempo restante: {self.tiempo_restante}", True, (COLOR_NEGRO))
            text_rect = text_surface.get_rect(center=(ANCHO // 2, 50))
            self.pantalla_principal.blit(text_surface, text_rect)

            self.tasa_refresco.tick(60)
            pg.display.flip()

        
        if self.tiempo_restante <= 0:
            self.eliminacion_obstaculos()
            self.final.bucle_pantalla()



    def manejar_colisiones(self):
        colision = pg.sprite.spritecollide(self.goku, self.grupo_bolas, True)
        if colision:
            self.goku.vidas -= 1
            explosion = Explosion(colision[0].rect.centerx, colision[0].rect.centery)
            self.grupo_explosion.add(explosion)
            if self.goku.vidas == 0:
                self.menu.bucle_pantalla()
                self.reiniciar_juego()
                return

        for explosion in self.grupo_explosion:
            explosion.update()
            self.pantalla_principal.blit(explosion.image, explosion.rect)

    def generar_obstaculos(self):
        probabilidad_generacion= 2

        if self.tiempo_restante <= 15:
            probabilidad_generacion = 4
            self.velocidad_obstaculos += 0.5
            self.pantalla_principal.blit(self.imagenFondo2,(0,0))
        if random.randint(0, 100) < probabilidad_generacion:
            obstaculos = Obstaculos(ANCHO, ALTO)
            self.grupo_bolas.add(obstaculos)

    def actualizar_pantalla(self):
        self.grupo_bolas.update()
        self.grupo_bolas.draw(self.pantalla_principal)

    def reiniciar_juego (self):
        self.goku.vidas = 3
        self.grupo_bolas.empty()
        self.grupo_explosion.empty()
        self.tiempo_restante = 30

    def eliminacion_obstaculos(self):
        self.grupo_bolas.empty()




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

                










    
    
    
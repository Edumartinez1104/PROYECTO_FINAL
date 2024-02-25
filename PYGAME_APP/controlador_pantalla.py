from .pantallas_varias import *

class controlador_pantalla:
    def __init__(self):
        self.menu = Menu()
        self.prologo = Prologo()
        self.partida = Partida()
        self.final = Final()


        



    
    def iniciar(self):
        cerrar = ""

        while True:
            cerrar = self.menu.bucle_pantalla()
            if cerrar == True:
                break
            cerrar == self.prologo.bucle_pantalla()
            if cerrar == True:
                break
            cerrar == self.partida.bucle_pantalla()
            if cerrar == True:
                break
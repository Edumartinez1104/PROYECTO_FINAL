from .pantallas_varias import *

class controlador_pantalla:
    def __init__(self):
        self.menu = MENU()
        self.prologo1 = PROLOGO1()
        self.prologo2 = PROLOGO2()
        self.prologo3 = PROLOGO3()
        self.partida = Partida()
        






    def start(self):
        cerrar=""
        while True:

            cerrar = self.menu.bucle_pantalla()
            if cerrar == True:
                break
            cerrar = self.prologo1.bucle_pantalla()
            if cerrar == True:
                break
            cerrar == self.prologo2.bucle_pantalla()
            if cerrar == True:
                break
            cerrar == self.prologo3.bucle_pantalla()
            if cerrar == True:
                
                break
                
from Integrante import Integrante

class Jugador(Integrante):

    def __init__(self, nombre) -> None:
        super().__init__(nombre, 'Jugador')
    
    def retirarcarta(self,  mazo, crupier = None):
        return crupier.retirarcarta(mazo, crupier)
    
from pickletools import OpcodeInfo
from turtle import delay
from Crupier import Crupier
from Iniciado import Iniciado
from Jugador import Jugador
from State import Context


from Mazo import Mazo

class BlackJack:
    
    def __init__(self) -> None:
        self._nomjugadores = []
        self._inicio = True
    
    def menu(self):
        opcion = "0"
        jugadores = []
        
        while(opcion not in ["1", "2"]):
            opcion = input("1-Iniciar el juego\n2-Salir\n\nElegir: ")
            
            if(opcion == "1"):
                if self._inicio:
                    self._nomjugadores = self.intro()
                    self._inicio = False
                
                for nombre in self._nomjugadores:
                    jugadores.append(Jugador(nombre))

                self.blackJackGame(jugadores)
            if(opcion == "2"):
                print("Hasta la proxima")
                delay(1000)

    def blackJackGame(self, jugadores):
        puntajeMaximo = 21
        mazo = Mazo()
        mazo.mezclar()
        cMazo = mazo.__iter__()
        crupier = Crupier('Julian')

        contexto = Context(Iniciado())
        contexto.request1(jugadores, crupier, cMazo, puntajeMaximo)
        contexto.request2(jugadores, crupier, cMazo, puntajeMaximo, self)

    def intro(self):
        cantJugadores = 3
        nomjugadores = []

        for i in range(0, cantJugadores):
            nombre = input("Ingrese el nombre del jugador N°" + str(i) + ": ")
            nomjugadores.append(nombre)
        
        return nomjugadores
        

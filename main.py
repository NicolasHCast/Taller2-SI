import sys
import os
from mapa import Mapa

from bestFirst import bestFirst


def main():
    os.system('cls')
    mapa = Mapa(4,1,1,2)
    print("------------------------------      START     ------------------------------")
    print("                              ---SIMBOLISMO---")
    print("                                   A: AIRE")
    print("                                  S: PRESTE")
    print('                                   H: HOYO')
    print("                                  W: WUMPUS")
    print("                                   G: ORO")
    print("                           AG: RECORRIDO DEL AGENTE")
    print("                              SEG: LUGAR SEGURO\n")
    mapa.showMap()
    bestFirst(mapa)

main()
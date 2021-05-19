import sys
import os
from mapa import Mapa

from bestFirst import bestFirst

os.system('cls')
mapa = Mapa(4,1,1,3)
#mapa.showMap()
print("------------------------START------------------------")
mapa.showMap()
bf = bestFirst(mapa)
#bf.showMapa()
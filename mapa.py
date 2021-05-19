from os import closerange
from habitacion import Habitacion
import random
import time

class Mapa:
    mapa = []
    heuristica = []
    def __init__ (self, cantRow, cantWumpus, cantOro, cantHoyos):
        for q in range(4):
            self.mapa.append([])
            for w in range(4):
                heu = random.randint(1, 15)
                pos = [q,w]
                array = []
                down = [q, w+1]
                array.append(down)
                right = [q+1, w]
                array.append(right)

                habitacion = Habitacion(pos)
                self.heuristica.append(heu)
                self.mapa[q].append(habitacion)
                adjs = []
                for i in array:
                    if(i[0] >= 0 and i[1] >= 0 and i[0] < cantRow and i[1] < cantRow ):
                        adjs.append(i)                        
                self.mapa[q][w].setAdj(adjs)
        print("-")
        self.setRoom(cantWumpus,"W")
        self.setRoom(cantOro,"G")
        self.setRoom(cantHoyos, "H")
    def showMap(self):
        for q in range(len(self.mapa)):
            fila = []
            for w in range(len(self.mapa)):
                fila.append(self.mapa[w][q].getType())
            print('\t\t',fila)        
        print('\n')

    def setRoom(self, q, name):
        i = 0
        while(i!=q):
            cell = self.randomCell()
            if (cell and cell.getType()=='F'):                
                cell.setType(name, self.mapa)
                i += 1
                

    def randomCell(self):        
        row = random.choice(self.mapa)
        cell = random.choice(row)
        if(cell.getInfo()['pos']!=[0,0] and cell.getInfo()['pos']!=[1,0] and cell.getInfo()['pos']!=[0,1]):
            return cell
        else:
            return False
    def getMapa(self):
        return self.mapa

    def getHeuristica(self):
        return self.heuristica

    def getCell(self,coor):
        return self.mapa[coor[0]][coor[1]]
    
    def popHeuristica(self):
        i = self.heuristica[0]
        #print("------------------------------------------------------return",i,self.heuristica,'\t',len(self.heuristica))
        self.heuristica.pop(0)
        return i
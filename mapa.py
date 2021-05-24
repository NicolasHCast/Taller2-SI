from os import closerange, set_inheritable
from habitacion import Habitacion
import random
import copy

class Mapa:
    mapa = []
    cantGold = int
    cantHoles = int
    cantRows = int
    cantWumpus = int
    heuristica = []

    def __init__ (self, cantRow, cantWumpus, cantGold, cantHoles):
        self.cantWumpus = cantWumpus
        self.cantHoles = cantHoles
        self.cantGold = cantGold
        self.cantRows = cantRow
        for q in range(cantRow):
            self.mapa.append([])
            for w in range(4):
                heu = random.randint(1, 15)
                pos = [q,w]
                
                array = []
                up = [q, w-1]
                array.append(up)
                left = [q-1, w]
                array.append(left)
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
        if cantWumpus != 0 and cantGold != 0 and cantHoles != 0:
            self.setRoom(cantWumpus,"W")
            self.setRoom(cantGold,"G")
            self.setRoom(cantHoles, "H")
    def showMap(self):
        for q in self.mapa:
            array = []    
            for w in q:
                array.append(w.getType())
            print('\t\t           ',array)
            
        print('\n')
        print('\n')

    def checkMap(self):
        for q in range(len(self.mapa)):
            fila = []
            for w in range(len(self.mapa)):
                l = self.mapa[w][q].getInfo()
                fila.append(l)
            print('\t\t',fila)   

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
        self.heuristica.pop(0)
        return i
    def getHoles(self):
        return self.cantHoles

    def getGols(self):
        return self.cantGold
    
    def getRows(self):
        return self.cantRows
    
    def getWumpus(self):
        return self.cantWumpus
    
    def getHoles(self):
        return self.cantHoles
    
    def getCopy(self):
        return copy.copy(self.mapa)
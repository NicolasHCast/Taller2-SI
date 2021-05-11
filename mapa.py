from os import closerange
from habitacion import Habitacion
import random

class Mapa:
    cantFilas = int
    matriz = []
    def __init__ (self,cantFilas, cantWumpus, cantOro, cantHoyos):
        tCells = cantFilas*cantFilas
        self.cantFilas = cantFilas
        if(tCells>=cantWumpus+cantHoyos+cantOro):
            for q in range(4):
                self.matriz.append([])
                for w in range(4):
                    pos = [q,w]
                    habitacion = Habitacion(pos)
                    self.matriz[q].append(habitacion)
            self.setRoom(cantWumpus,"WUMPUS")
            self.setRoom(cantOro,"ORO")
            self.setRoom(cantHoyos, "HOYO")
        else:
            print("Error")
    def showMap(self):
        print("------")
        for q in range(len(self.matriz)):
            fila = []
            for w in range(len(self.matriz)):
                fila.append(self.matriz[w][q].getType())
            print(fila)
        print(self.matriz[0][3].getInfo()['pos'])

    def setRoom(self, q, name):
        i = 0
        while(i!=q):
            cell = self.randomCell()
            if (cell):
                if(cell.getType()=='FREE'):
                    cell.setType(name, self.matriz)
                    i += 1
                

    def randomCell(self):        
        row = random.choice(self.matriz)
        cell = random.choice(row)
        if(cell.getInfo()['pos']!=[0,0]):
            return cell
        else:
            return False
from typing import Coroutine
from mapa import Mapa
from agente import Agente

class bestFirst:
    mapa = Mapa

    newMapa = []

    Rec = []

    open = []
    close = []

    listHEU = []

    find = False

    agente = Agente
    def __init__(self, mapa) -> None:
        self.mapa = mapa        
        self.agente = Agente([0,0], self.mapa.getMapa()[0][0])
        print(self.mapa.getHeuristica())
        self.mapa2()
        self.Run()
        pass

    def mapa2(self):
        for q in range(len(self.mapa.getMapa())):
            fila = []
            for w in range(len(self.mapa.getMapa())):
                fila.append(" ")
            self.newMapa.append(fila)            
    
    def showMapa(self):
        for q in range(len(self.mapa.getMapa())):
            row = []
            for w in range(len(self.mapa.getMapa())):
                row.append(self.newMapa[w][q])
            print(row)
        print("\n")
        #print(self.mapa.getMapa())
        #self.mapa.showMap()

    def checkRoom(self, agent):      
        coor = agent.getPos()
        self.newMapa[coor[0]][coor[1]] = 'A'
        row = coor[0]
        col = coor[1]
        

    def Review(self, coor):
        room = self.mapa.getCell(coor)
        shine = room.getInfo()['shine']
        air = room.getInfo()['air']
        edor = room.getInfo()['edor']
        status = []
        if(shine):
            status.append('SHINE')
        if(air):
            status.append('AIR')
        if(edor):
            status.append('EDOR')
        return status

    def Run(self):
        self.bf(self.agente)

    def bf(self, agent):
        coorAgent = agent.getPos()
        review = self.Review(coorAgent)
        if(self.listHEU):
            self.listHEU.pop(0)
        room = self.mapa.getMapa()[coorAgent[0]][coorAgent[1]]
        if(room.getInfo()['gold']):
            print("Oro encontrado en",coorAgent)
            print("------------------------GOLD------------------------")
        elif(len(review)==0):
            self.Rec.append([self.mapa.popHeuristica(), coorAgent])
            adjs = self.Open(coorAgent)
            for q in adjs:
                i = self.mapa.popHeuristica()
                self.listHEU.append([i, q])
            self.listHEU.sort()
            print("PASO: ", coorAgent, "lista:",self.listHEU)

            #print(self.listHEU[0], room.getInfo()['pos'])
            self.agente.setPos(self.listHEU[0][1])
            self.bf(self.agente)
            #self.Open(self.listHEU[0][1])
        else:
            print(review)
            """ if(self.listHEU):
                print("warning in",self.mapa.getMapa()[coorAgent[0]][coorAgent[1]].getInfo()['pos'], review)
                cell = self.listHEU[0][1]
                self.agente.setPos(cell)
                print("next room", cell,"lista:",self.listHEU)
                self.bf(self.agente) """
    
    def Open(self, cell):
        self.open.append(cell)
        roomAgent = self.mapa.getMapa()[cell[0]][cell[1]]
        heu = self.mapa.getHeuristica()
        roomAdjs = roomAgent.getInfo()['adj']
        #print(roomAdjs)
        #print("HEURISTICA:",heu, len(heu))
        #print("REC:", self.Rec, len(self.Rec))
        return roomAdjs
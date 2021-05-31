from habitacion import Habitacion
import time
class Agente:

    memory = []

    warnign = []
    warnign2 =[]

    wumpus = []
    holes = []   

    ok = []
    adjOk = []

    position = []

    arrows = 1

    room = Habitacion

    def __init__(self, pos, room):
        self.position = pos
        self.room = room

    def getPos(self):
        return self.position

    def setPos(self, pos):
        self.position = pos
    
    def getRoom(self):
        return self.room

    def setRoom(self, room):
        self.room = room
    
    def addMemory(self, info):
        if info not in self.memory:
            self.memory.append(info)
        self.memory.sort()            
    def getMemory(self):
        return self.memory
    

    def addWarning(self, coor, info, newMap):
        if coor not in self.ok and coor not in self.adjOk and coor not in self.wumpus and coor not in self.holes:
            self.warnign.append(coor)
            self.warnign2.append([coor, info])
            newMap[coor[0]][coor[1]].viewAgent(info)            
            print("\t\t\t        EN LA CELDA:",coor)
    
    def popWarning(self):
        i = self.warnign[0]
        self.warnign.pop(0)
        for q in range(len(self.warnign2)):
            if i == self.warnign2[q]:
                self.warnign2.pop(q)
        return i

    def checkWarning(self, fc):
        check = []
        for q in range(len(fc[1])):
            count = 0
            for w in range(len(self.warnign2)):
                if fc[1][q] == self.warnign[w]:
                    count += 1
            if count == 2:
                safe = False
                safe2 = True
                posDanger = []
                
                type = ' '
                type2 = str
                count2 = 0
                for w in range(len(self.warnign2)):
                    if fc[1][q][0] == self.warnign2[w][0][0] and fc[1][q][1] == self.warnign2[w][0][1]:
                        posDanger = fc[1][q]
                        if len(fc[0])!=len(self.warnign2[w][1]):
                            l = str
                            safe2 = False
                            if len(fc[0])<len(self.warnign2[w][1]):
                                l = fc[0]
                                if l[0] == 'S':
                                    type2 = 'WUMPUS'
                                elif l[0] == 'A':
                                    type2 = 'HOLE'
                            else:
                                l = self.warnign2[w][1]
                                if l[0] == 'S':
                                    type2 = 'WUMPUS'
                                    safe2 = False
                                elif l[0] == 'A':
                                    safe2 = False
                                    type2 = 'HOLE'
                        else:
                            if len(fc[0])==1:
                                if fc[0][0] != self.warnign2[w][1][0]:
                                    safe = True
                                else:
                                    count2 += 1
                                if fc[0][0] in self.warnign2[w][1] and count2 > 1:
                                    type = '-'
                                    safe = False
                if not safe2:
                    check.append([safe2, posDanger,type2])
                elif count2 >1 or not safe:
                    if len(fc[0])==1:
                        safe = False
                        if fc[0][0] == 'S':
                            type = 'WUMPUS'
                        elif fc[0][0] == 'A':
                            type = 'HOLE'
                    elif len(self.warnign2[w][1][0]) == 1:
                        if self.warnign2[w][1][0] == 'S':
                            type = 'WUMPUS'
                        elif self.warnign2[w][1][0] == 'A':
                            type = 'HOLE'
                    check.append([safe, posDanger,type])
                elif safe:
                    check.clear()
                    check.append([safe2, posDanger])
        return check

    def getWarning(self):
        return self.warnign2
    
    def getCoorWarning(self):
        return self.warnign

    def addOk(self, coor):        
        if type(coor[0]) != list:
            if(coor not in self.ok):
                self.ok.append(coor)
        else:
            for q in coor:
                if(q not in self.ok):
                    self.ok.append(q)        

    def getOk(self):
        return self.ok
    
    def addDanger(self, coor):
        if(coor not in self.danger):
            self.danger.append(coor)

    def addWumpus(self, coor):
        if(coor not in self.wumpus):
            self.wumpus.append(coor)

    def getWumpus(self):
        return self.wumpus
    
    def addHole(self, coor):
        if(coor not in self.holes):
            self.holes.append(coor)

    def getHoles(self):
        return self.holes

    def huntWumpus(self, roomWumpus):
        print("\t\t\t\tRECARGANDO ARCO")
        if self.arrows > 0:
            print("\t\t\tEL AGENTE DISPARO HACIA LA CELDA", roomWumpus.getPos())
            self.arrows -= 1
            return roomWumpus.shootWumpus()
        else:
            print("\t\        EL AGENTE SE QUEDO SIN FLECHAS POR LO TANTO NO PUEDE SEGUIR")
            return False
    def removeWarning(self, dangerRoom):
        room = dangerRoom.getPos()        
        for q in range(len(self.warnign2)):
            if room[0] == self.warnign2[q][0][0] and room[1] == self.warnign2[q][0][1]:
                self.warnign2[q] = "R"
                self.warnign[q] = "R"
        try:
            self.warnign.remove('R')
            self.warnign2.remove('R')
            self.warnign.remove('R')
            self.warnign2.remove('R')
        except:
            a = 0
    
    def addAdjOk(self, coor):
        if coor not in self.adjOk:
            self.adjOk.append(coor)
    
    def getAdjOks(self):
        return self.adjOk

    def getArrows(self):
        if self.arrows == 0:
            return False
        else:
            return True
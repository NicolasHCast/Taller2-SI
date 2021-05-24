import time
import copy
from mapa import Mapa
from agente import Agente
from habitacion import Habitacion

class bestFirst:
    mapa = Mapa

    newMap = []

    HEU = []
    coorHEU = []

    way = []

    agente = Agente

    newRooms = Habitacion

    def __init__(self, mapa) -> None:
        self.mapa = mapa        
        self.agente = Agente([0,0], self.mapa.getMapa()[0][0])
        print(self.mapa.getHeuristica())
        #self.drawMap()
        self.createMap()
        self.Run()
        pass

    def drawMap(self):
        #print(self.newMap.getMapa())
        for q in self.newMap:
            array = []             
            for w in q:
                array.append(w.getType())
            print('\t\t ',array)
            
        print('\n')
        print('\n')
    
    def createMap(self):
        for q in self.mapa.getMapa():
            array = []
            for w in q:
                newRoom = Habitacion(w.getPos())
                newRoom.viewAgent('       ')
                array.append(newRoom)
                #print(w)
            self.newMap.append(array)
        print("NEW MAP CREATED")
                #w.setType(" ", self.newMap)

    def Run(self):
        self.bf(self.agente)
        

    def bf(self, agent):
        gold = False
        posAgent = agent.getPos()
        agent.addOk(posAgent)
        room = self.mapa.getMapa()[posAgent[0]][posAgent[1]]
        roomView = self.newMap[posAgent[0]][posAgent[1]]
        rooms = room.getInfo()['adj']
        if(room.getType()=='W'):
            print("----------------------GG WUMPUS LIVE------------------------")
            print("MAP AGENT")
            self.drawMap()
            print("WAY:", self.way)
            print("OK:",agent.getOk())
        elif(room.getType()=='H'):
            print(' GG HOLE')
            print("MAP AGENT")
            self.drawMap()
            print("WAY:", self.way)
            print("OK:",agent.getOk())
            
        elif(room.getType()=='G'):
            print('\t\t\t   Oro encontrado en la celda',posAgent)
            roomView.viewAgent('   AG-G   ')
            gold = True
            print("MAP AGENT")
            self.drawMap()
            print("WAY:", self.way)
            print("OK:",agent.getOk())
            return
        else:
            self.way.append(posAgent)
            fc = self.firstConditional(agent, room, rooms)
            roomView.viewAgent('   AG   ')
            agent.addAdjOk(posAgent)
            #self.newMap().getMapa()[posAgent[0]][posAgent[1]] = 'A'
            #print("LEEEEEEEEEEEEEEEEEEN",len(fc[0]))
            if(len(fc[0])==0):
                ##roomView.viewAgent('   AG   ')
                self.way.append(posAgent)
                if room.getHeuristica() == -1:
                    aux = self.mapa.popHeuristica()
                    if posAgent != [0,0]:
                        self.HEU.append([aux, posAgent])
                    self.mapa.getMapa()[posAgent[0]][posAgent[1]].setHeuristica(aux)
                #print("                       ",agent.getPos())
                self.nextMove(rooms, agent)
            else:
                check = agent.checkWarning(fc)
                #print('IF CHECK-----------------', check, len(check))
                if check:
                    check = check[0]
                    #print(check[0], check,'<----------------------------------------')
                    if check[0]:
                        ##roomView.viewAgent('   OK   ')
                        #print("++++++++++++++++++++++++++++++++OK?",posAgent)
                        time.sleep(1)
                        OkRoom = self.mapa.getMapa()[check[1][0]][check[1][1]]
                        if OkRoom.getHeuristica() == -1:
                            aux = self.mapa.popHeuristica()
                            self.mapa.getMapa()[check[1][0]][check[1][1]].setHeuristica(aux)
                            self.HEU.append([aux, check[1]])
                            self.newMap[check[1][0]][check[1][1]].viewAgent('   SEG   ')
                            #self.nextMove(rooms, agent)
                    else:
                        ##roomView.viewAgent('PD')
                        dangerRoom = self.mapa.getMapa()[check[1][0]][check[1][1]]
                        roomView = self.newMap[check[1][0]][check[1][1]]
                        #print("DANGER:",check)
                        #time.sleep(1)
                        if check[2]=='WUMPUS':
                            print('\n\t\t                WUMPUS EN LA CELDA', check[1],'\n')
                            #time.sleep(0.5)
                            roomView.viewAgent('   |W|   ')
                            agent.addWumpus(check[1])
                            #print("WUMPUS LIST:",agent.getWumpus())
                            #time.sleep(0.5)
                            if agent.getArrows():
                                #roomView.viewAgent('   R   ')
                                agent.addAdjOk(dangerRoom.getPos())
                                aux = self.mapa.popHeuristica()
                                self.mapa.getMapa()[check[1][0]][check[1][1]].setHeuristica(aux)
                                self.HEU.append([aux, dangerRoom.getPos()])
                                print(agent.getAdjOks())
                            else:
                                print("\t\t\t    EL ANGENTE SE QUEDO SIN FLECHAS")
                        else:
                            print('\t\t\t       HOYO EN LA CELDA', check[1])
                            #time.sleep(0.5)
                            roomView.viewAgent('   |H|   ')
                            agent.addHole(check[1])
                        print("HEU:",self.HEU)
                        #print("+++++++++++++DANGER:", dangerRoom.getPos(), posAgent)
                        agent.removeWarning(dangerRoom)
                        #print("REMOVE WARMING", dangerRoom, dangerRoom.getPos(), dangerRoom.getType())
                        #time.sleep(0.5)
                ##time.sleep(0.5)
            self.HEU.sort()
            if not self.HEU:
                print("HEU:",self.HEU)
                ##roomView.viewAgent('   R   ')
                if not agent.getWumpus():
                    count = 0                    
                    for q in agent.getWarning():
                        if 'S' in q[1]:
                            count += 1
                    if count == 1:
                        pos = []                        
                        for q in agent.getWarning():
                            if 'S' in q[1]:
                                pos = q[0]
                        dangerRoom = self.mapa.getMapa()[pos[0]][pos[1]]
                        print("\t\t\tWUMPUS DETECTADO EN LA CELDA", pos)
                        #time.sleep(0.5)
                        if agent.huntWumpus(dangerRoom):
                            agent.removeWarning(dangerRoom)
                            #roomView.viewAgent('   R   ')
                            ##roomView.viewAgent('   OK   ')
                            #print("------------------------------------------->OK?", posAgent)
                            #time.sleep(0.5)
                            aux = self.mapa.popHeuristica()
                            self.mapa.getMapa()[pos[0]][pos[1]].setHeuristica(aux)
                            self.HEU.append([aux, dangerRoom.getPos()])
                            #print("--------->",self.HEU)
                            newpos = self.HEU.pop(0)
                            agent.setPos(newpos[1])
                            self.bf(agent)
                            gold = True
                       
                else:
                    if agent.getPos() in agent.getWumpus():
                        #roomView.viewAgent('   R   ')
                        dangerRoom = self.mapa.getMapa()[agent.getPos()[0]][agent.getPos()[1]]
                        #print("++++++++++++HEU VOID AND AGENT IN TO WUMPUS")
                        #time.sleep(0.5)
                if not self.HEU and not gold:
                    print("\t\t       NO SE HAN ENCONTRADO MAS CAMINOS SEGUROS.")
                    #time.sleep(0.5)
                    print("MAP AGENT")
                    self.drawMap()
                    print("WAY:", self.way)
                    print("OK:",agent.getOk())
                    print("WORD")
                    self.mapa.showMap()
            else:
                if not gold:
                    print("HEU:",self.HEU)
                    print("WAY:", self.way)
                    newpos = self.HEU.pop(0)
                    agent.setPos(newpos[1])
                    print("MAP AGENT")
                    self.drawMap()
                    print("\t\t\tEL AGENTE AVANZA HACIA LA CELDA",agent.getPos())
                    #time.sleep(0.5)
                    print('\n')
                    if newpos[1] in agent.getWumpus():

                        print('\t\tEL AGENTE SE PREPARA PARA DISPARAR A LA CELDA', newpos[1][0],newpos[1][1])
                        #time.sleep(0.5)
                        dangerRoom = self.mapa.getMapa()[newpos[1][0]][newpos[1][1]]
                        if not agent.huntWumpus(dangerRoom):
                            if self.HEU:
                                newpos = self.HEU.pop(0)
                                agent.setPos(newpos[1])
                    #roomView.viewAgent('   R   ')
                    self.bf(agent)

    def checkHEU(self, pos):
        if(len(self.way)>0):
            for q in self.way:
                if pos == q:
                    return True            
            return False
        else:
            return False

    def firstConditional(self, agent, room, rooms):
        info = room.getInfo()
        array = []
        if info['stink']:
            array.append('S')
        if info['air']:
            array.append('A')  
        if len(array)>=1:
            array2 = []
            print("\t\t\t\tSE A DETECTADO", array)
            #time.sleep(0.5)
            print("\t\t\t\tAGREGANDO REGISTROS")
            #time.sleep(0.5)
            for q in rooms:
                if q not in self.way and q not in agent.getOk() and q not in agent.getAdjOks() :
                #if q not in agent.getAdjOks():
                    agent.addWarning(q, array, self.newMap)
                    array2.append(q)
            return [array, array2]
        else:
            return [[], rooms]

    def nextMove(self, rooms, agent):
        #print("NEXT MOVE HEU BEFORE:",self.HEU)
        for q in rooms:
            room = self.mapa.getMapa()[q[0]][q[1]]
            if q not in agent.getWumpus() or q not in agent.getHoles() and q not in agent.getOk() and q not in agent.getAdjOks():                
                if q not in agent.getCoorWarning():
                    agent.addAdjOk(q)
                    #print(q,'------------------')
                else:
                    agent.removeWarning(room)
                    #print("REMOVE WARMING", room, room.getPos())
                    #time.sleep(0.5)
                    agent.addAdjOk(q)
                    #print(">>>>>",agent.getCoorWarning())
                

            if q not in agent.getOk() and room.getHeuristica() == -1:
                aux = self.mapa.popHeuristica()
                self.newMap[q[0]][q[1]].viewAgent('   SEG   ')
                self.mapa.getMapa()[q[0]][q[1]].setHeuristica(aux)
                self.HEU.append([aux, q])
        #print("NEXT MOVE HEU AFTER:",self.HEU)
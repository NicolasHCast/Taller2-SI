from warnings import resetwarnings


class Habitacion:
    position = []
    
    free = True

    wumpus = False
    edor = False

    oro = False
    resplandor = False

    hoyo = False
    brisa = False
    
    def __init__(self, pos) -> None:
        self.position = pos
    
    def getInfo(self):
        info = {
            "pos": self.position,
            "wumpus": self.wumpus,
            "edor" : self.edor,
            "oro" : self.oro,
            "resplandor" : self.resplandor,
            "hoyo" : self.hoyo,
            "brisa" : self.brisa,
            'free': self.free
        }
        return info 
    
    def setType(self, arg, mapa):
        if(arg == 'WUMPUS'):
            self.free = False
            self.wumpus = True
            self.addStatus(mapa)
        elif(arg =='ORO'):
            self.free = False
            self.oro = True
            self.addStatus(mapa)
        elif(arg=='HOYO'):
            self.free = False
            self.hoyo = True
            self.addStatus(mapa)

    def getType(self):
        if self.wumpus:
            return "WUMPUS" 
        elif self.oro:
            return 'ORO'
        elif self.hoyo:
            return 'HOYO'
        elif self.free:
            return 'FREE'

    def addStatus(self, mapa):
        fila = self.position[0]
        col = self.position[1]
        array = []
        up = [fila, col-1]
        array.append(up)
        left = [fila-1, col]
        array.append(left)
        down = [fila, col+1]
        array.append(down)
        right = [fila+1, col]
        array.append(right)
        if(self.wumpus):
            for q in array:
                if(q[0] >= 0 and q[1] >= 0 and q[0] < len(mapa) and q[1] < len(mapa) ):
                    #mapa[q[0]][q[1]]
                    mapa[q[0]][q[1]].setEdor()
        elif(self.oro):
            for q in array:
                if(q[0] >= 0 and q[1] >= 0 and q[0] < len(mapa) and q[1] < len(mapa) ):
                    #mapa[q[0]][q[1]]
                    mapa[q[0]][q[1]].setResplandor()
        elif(self.hoyo):
            for q in array:
                if(q[0] >= 0 and q[1] >= 0 and q[0] < len(mapa) and q[1] < len(mapa) ):
                    #mapa[q[0]][q[1]]
                    mapa[q[0]][q[1]].setBrisa()
        else:
            return self

    def setEdor(self):
        if(self.edor==False):
            self.edor = True
    def setResplandor(self):
        if(self.resplandor==False):
            self.resplandor = True
    def setBrisa(self):
        if(self.brisa==False):
            self.brisa = True

class Habitacion:
    heuristica = int

    position = []

    adj = []
    
    danger = False
    warning = False
    free = True

    wumpus = False
    edor = False

    gold = False
    shine = False

    hole = False
    air = False
    
    def __init__(self, pos) -> None:
        self.position = pos
    
    def getInfo(self):
        return  {
            "pos": self.position,
            "wumpus": self.wumpus,
            "edor" : self.edor,
            "gold" : self.gold,
            "shine" : self.shine,
            "hole" : self.hole,
            "air" : self.air,
            'free': self.free,
            "danger": self.danger,
            "warning": self.warning,
            "heuristica": self.heuristica,
            "adj": self.adj
        }
        
    
    def setType(self, arg, mapa):
        if(arg == 'W'):
            self.free = False
            self.wumpus = True
            self.addStatus(mapa)
        elif(arg =='G'):
            self.free = False
            self.gold = True
            self.shine = True
            self.addStatus(mapa)
        elif(arg=='H'):
            self.free = False
            self.hole = True
            self.addStatus(mapa)

    def getType(self):
        if self.wumpus:
            return "W" 
        elif self.gold:
            return 'G'
        elif self.hole:
            return 'H'
        elif self.free:
            return 'F'

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
        elif(self.hole):
            for q in array:
                if(q[0] >= 0 and q[1] >= 0 and q[0] < len(mapa) and q[1] < len(mapa) ):
                    #mapa[q[0]][q[1]]
                    mapa[q[0]][q[1]].setAir()
        else:
            return self

    def setEdor(self):
        if(self.edor==False):
            self.edor = True
        else:
            self.edor = False
    def setAir(self):
        if(self.air==False):
            self.air = True
        else:
            self.air = False
    def setDanger(self):
        if(self.danger==False):
            self.danger = True
        else:
            self.danger = False
        
    def setWarning(self):
        if(self.warning==False):
            self.warning = True
        else:
            self.warning = False
            
    def setHeuristica(self, heu):
        self.heuristica = heu

    def setAdj(self, adjs):
        self.adj = adjs
class Habitacion:
    heuristica = -1

    position = []

    adj = []
    
    danger = False
    warning = False
    
    free = True
    

    wumpus = False
    stink = False

    gold = False
    shine = False

    hole = False
    air = False

    type = str
    
    def __init__(self, pos) -> None:
        self.position = pos
    
    def getInfo(self):
        return  {
            "pos": self.position,
            "wumpus": self.wumpus,
            "stink" : self.stink,
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
            
            #self.addStatus(mapa)
    
    def viewAgent(self, type):
        self.free = False
        self.gold = False
        self.wumpus = False
        self.hole = False
        self.type = type

    def getType(self):
        if self.wumpus:
            return "W" 
        elif self.gold:
            return 'G'
        elif self.hole:
            return 'H'
        elif self.free:
            return 'F'
        else:
            return self.type

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
                    mapa[q[0]][q[1]].isStink()
        elif(self.hole):
            for q in array:
                if(q[0] >= 0 and q[1] >= 0 and q[0] < len(mapa) and q[1] < len(mapa) ):
                    #mapa[q[0]][q[1]]
                    mapa[q[0]][q[1]].isAir()
        else:
            return self

    def isStink(self):
        self.stink = True

    def getStink(self):
        return self.stink    
    
    def isAir(self):
        self.air = True
    
    def isDanger(self):
        self.danger = True
        
    def isWarning(self):
        self.warning = True
            
    def setHeuristica(self, heu):
        if self.heuristica == -1:
            self.heuristica = heu

    def getHeuristica(self):
        return self.heuristica

    def setAdj(self, adjs):
        self.adj = adjs

    def getAdj(self):
        return self.adj

    def getPos(self):
        return self.position

    def shootWumpus(self):
        if self.wumpus:
            print("\t\t       SE ESCUCHA UN GRITO (EL WUMPUS MUERE)")
            self.wumpus = False
            self.free = True
            return True
        else:
            print("\t\t\tNO SE ESCUCHA NADA")
            return False
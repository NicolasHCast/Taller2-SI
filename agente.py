from habitacion import Habitacion
class Agente:
    solucion = []

    memory = []

    position = []

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
    
    def appendMemory(self, info):
        self.memory.append(info)
    
    def setMemory(self, info):
        print("set memory")
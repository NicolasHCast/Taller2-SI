class Agente:
    position = []
    row = int
    col = int
    maxRow = int

    def __init__(self, pos, maxRow):
        self.position = pos
        self.row = pos[0]
        self.col = pos[1]
        self.maxRow = maxRow
    def movUp(self):
        if(self.row != 0 or self.row != self.maxRow):
            print('UP')
"""
    def movDown():

    def movLeft():

    def movRight():
 """
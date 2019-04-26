
class Strategy:

    # roads should be of the format [('r', (x1, y1), (x2, y2)), etc]
    def __init__(self, player, type, v=-1, roads=[]):
        self.type = type
        self.player = player
        self.vertex = v

        if type == "settlement":
            self.moves = roads + [('s', v)]
            self.cost = [2+len(roads), len(roads), 1]

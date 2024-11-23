class GameStatistics:

    def __init__(self):
        # overall
        self.frames = 0
        # needs
        self.attention = 50
        self.sway = 50
        self.destruction = 50
        self.satisfaction = 50

    def update_needs(self, modification=(-1, -1, -1, -1)):
        self.attention -= modification[0]
        self.sway -= modification[1]
        self.destruction -= modification[2]
        self.satisfaction -= modification[3]

    def update(self):
        self.frames += 1
        if self.frames % 600 == 0:
            self.update_needs()
class GameStatistics:

    def __init__(self):
        # overall
        self.frames = 0
        # needs
        self.attention = 50
        self.power = 50
        self.destruction = 50
        self.satisfaction = 50

    def update_needs(self, modification=(-1, -1, -1, -1)):
        self.attention += modification[0]
        self.power += modification[1]
        self.destruction += modification[2]
        self.satisfaction += modification[3]

    def update(self):
        self.frames += 1
        if self.frames % 60 == 0:
            self.update_needs()

    def check_lose_condition(self):
        if self.attention <= 0 or self.power <= 0 or self.destruction <= 0 or self.satisfaction <= 0:
            return -1
        if self.attention >= 200 or self.power >= 200 or self.destruction >= 200 or self.satisfaction >= 200:
            return 1
        if self.attention + self.power + self.destruction + self.satisfaction <= 50:
            return -1
        if self.attention + self.power + self.destruction + self.satisfaction >= 600:
            return 1
        return 0

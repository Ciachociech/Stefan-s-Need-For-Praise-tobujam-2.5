class GameStatistics:

    def __init__(self):
        # overall
        self.frames = None
        # needs
        self.attention = None
        self.power = None
        self.destruction = None
        self.satisfaction = None
        # poops/currency
        self.poops = None
        self.currency = None

    def set(self):
        # overall
        self.frames = 0
        # needs
        self.attention = 50
        self.power = 50
        self.destruction = 50
        self.satisfaction = 50
        # poops/currency
        self.poops = 0
        self.currency = 0

    def update_needs(self, modification=(-1, -1, -1, -1)):
        self.attention += modification[0]
        self.power += modification[1]
        self.destruction += modification[2]
        self.satisfaction += modification[3]

    def change_poops_to_currency(self):
        self.currency += self.poops
        self.poops = 0

    def update(self):
        self.frames += 1
        if self.frames % 60 == 0:  # final value can be changed, probably smaller than actual
            self.update_needs()
        if self.frames % 600 == 0:
            self.poops += 1

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

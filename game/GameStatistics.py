import time

from game.JSONStatistics import save_statistics_to_json


class GameStatistics:

    def __init__(self):
        # overall
        self.frames = None
        self.timestamp = time.time()
        # needs
        self.attention = None
        self.power = None
        self.destruction = None
        self.satisfaction = None
        # poops/currency
        self.poops = None
        self.currency = None
        # upgrades
        self.needs_upgrade = None
        self.feeding_upgrade = None
        self.petting_upgrade = None
        self.cleaning_upgrade = None

    def set(self):
        # overall
        self.frames = 0
        self.timestamp = time.time()
        # needs
        self.attention = 50
        self.power = 50
        self.destruction = 50
        self.satisfaction = 50
        # poops/currency
        self.poops = 0
        self.currency = 0
        # upgrades
        self.needs_upgrade = 0
        self.feeding_upgrade = 0
        self.petting_upgrade = 0
        self.cleaning_upgrade = 0

    def update_needs(self, modification=(-1, -1, -1, -1)):
        self.attention += modification[0]
        self.power += modification[1]
        self.destruction += modification[2]
        self.satisfaction += modification[3]

    def change_poops_to_currency(self):
        self.currency += self.poops
        self.poops = 0

    def update(self, frames=1):
        self.frames += frames
        if frames // (3000 * (2 ** self.needs_upgrade)) > 0:
            self.update_needs((-frames // 600, -frames // 600, -frames // 600, -frames // 600))
        # player should learn how to play during first 10 minutes (or maybe a bit more)
        elif self.frames % (3000 * (2 ** self.needs_upgrade)) == 0:
            self.update_needs()
        if self.frames % 600 == 0:
            self.poops += 2 * self.cleaning_upgrade if self.cleaning_upgrade != 0 else 1
        # make a save backup each 18000 frames (should be every 5 minutes)
        if self.frames % 18000 == 0:
            save_statistics_to_json(self, extension=".dat.bkp")

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

from levelup.position import Position
from levelup.gamemap import GameMap

class Character:
    name = ""
    position = Position(0, 0)
    gameMap = None

    def __init__(self, character_name):
        self.name = character_name

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def enter_map(self):
        self.gameMap = GameMap()
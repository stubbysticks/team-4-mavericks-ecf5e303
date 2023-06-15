from levelup.position import Position
from levelup.gamemap import GameMap

class Character:
    name = ""
    position = None
    gameMap = None
    total_moves = 0

    def __init__(self, character_name):
        self.name = character_name

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def enter_map(self):
        self.gameMap = GameMap()
        self.position = self.gameMap.positions[0][0]

    def move(self, direction):
        self.gameMap.CalculatePosition(self.position, direction)
        self.total_moves = self.total_moves + 1

    def get_total_moves(self):
        return self.total_moves

from dataclasses import dataclass
from levelup.position import Position

@dataclass
class GameMap:
    x = ""

    def IsPositionValid(self, position: Position):
        return
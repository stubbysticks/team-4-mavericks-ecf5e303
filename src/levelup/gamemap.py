from dataclasses import dataclass
from levelup.position import Position

@dataclass
class GameMap:
    maxX = 9

    def IsPositionValid(self, position: Position):
        if (position.xCoordinate > self.maxX):
            return False
        elif (position.xCoordinate < 0):
            return False
        else:
            return True
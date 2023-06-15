from dataclasses import dataclass
from levelup.position import Position

@dataclass
class GameMap:
    maxX = 9
    maxY = 9

    def IsPositionValid(self, position: Position):
        if (position.xCoordinate > self.maxX or position.yCoordinate > self.maxY):
            return False
        elif (position.xCoordinate < 0 or position.yCoordinate < 0):
            return False
        else:
            return True
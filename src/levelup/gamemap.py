from dataclasses import dataclass
from levelup.position import Position
from levelup.controller import Direction

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

    def CalculatePosition(self, position: Position, direction: Direction):
        newyCoordinate = -1
        if (direction == Direction.NORTH):
            newyCoordinate = position.yCoordinate + 1
        return Position(position.xCoordinate, newyCoordinate)
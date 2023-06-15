from dataclasses import dataclass
from levelup.position import Position
from levelup.controller import Direction

@dataclass
class GameMap:
    maxX = 9
    maxY = 9
    positions = []

    def __init__(self):
        for row in range(self.maxX + 1):
            col = []
            for column in range(self.maxY + 1):
                col.append(Position(row, column))
            self.positions.append(col)

    def CalculatePosition(self, position: Position, direction: Direction):
        if (direction == Direction.NORTH and position.yCoordinate < 9):
            return self.positions[position.xCoordinate][position.yCoordinate + 1]
        elif (direction == Direction.SOUTH and position.yCoordinate > 0):
            return self.positions[position.xCoordinate][position.yCoordinate - 1]
        elif (direction == Direction.EAST and position.xCoordinate < 9):
            return self.positions[position.xCoordinate + 1][position.yCoordinate]
        elif (direction == Direction.WEST and position.xCoordinate > 0):
            return self.positions[position.xCoordinate - 1][position.yCoordinate]
        else:
            return position
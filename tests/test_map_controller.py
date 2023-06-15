from unittest import TestCase
from levelup.gamemap import GameMap
from levelup.position import Position
from levelup.controller import Direction

class TestGameMap(TestCase):
    def test_init(self):
        testObj = GameMap()
        assert testObj != None
        
    def test_calculatePositionN(self):
        testObj = GameMap()
        testPosition = Position(0, 0)
        newPosition = testObj.CalculatePosition(testPosition, Direction.NORTH)
        assert newPosition.yCoordinate == 1

    def test_calculatePositionS(self):
        testObj = GameMap()
        testPosition = Position(0, 1)
        newPosition = testObj.CalculatePosition(testPosition, Direction.SOUTH)
        assert newPosition.yCoordinate == 0

    def test_calculatePositionE(self):
        testObj = GameMap()
        testPosition = Position(0, 0)
        newPosition = testObj.CalculatePosition(testPosition, Direction.EAST)
        assert newPosition.xCoordinate == 1

    def test_calculatePositionW(self):
        testObj = GameMap()
        testPosition = Position(1, 0)
        newPosition = testObj.CalculatePosition(testPosition, Direction.WEST)
        assert newPosition.xCoordinate == 0
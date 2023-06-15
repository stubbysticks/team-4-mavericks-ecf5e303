from unittest import TestCase
from levelup.gamemap import GameMap
from levelup.position import Position
from levelup.controller import Direction

class TestGameMap(TestCase):
    def test_init(self):
        testObj = GameMap()
        assert testObj != None
        
    def test_isPositionValid(self):
        testObj = GameMap()
        testPosition = Position(0, 0)
        assert testObj.IsPositionValid(testPosition) != ""

    def test_isPositionValidForInvalidXCoordinate10(self):
        testObj = GameMap()
        testPosition = Position(10, 0)
        assert testObj.IsPositionValid(testPosition) == False

    def test_isPositionValidForInvalidXCoordinateNeg1(self):
        testObj = GameMap()
        testPosition = Position(-1, 0)
        assert testObj.IsPositionValid(testPosition) == False

    def test_isPositionValidForInvalidYCoordinate10(self):
        testObj = GameMap()
        testPosition = Position(0, 10)
        assert testObj.IsPositionValid(testPosition) == False

    def test_isPositionValidForInvalidYCoordinateNeg1(self):
        testObj = GameMap()
        testPosition = Position(0, -1)
        assert testObj.IsPositionValid(testPosition) == False

    def test_calculatePositionN(self):
        testObj = GameMap()
        testPosition = Position(0, 0)
        newPosition = testObj.CalculatePosition(testPosition, Direction.NORTH)
        assert newPosition.yCoordinate == 1

    def test_calculatePositionS(self):
        testObj = GameMap()
        testPosition = Position(0, 0)
        newPosition = testObj.CalculatePosition(testPosition, Direction.SOUTH)
        assert newPosition.yCoordinate == -1

    def test_calculatePositionE(self):
        testObj = GameMap()
        testPosition = Position(0, 0)
        newPosition = testObj.CalculatePosition(testPosition, Direction.EAST)
        assert newPosition.xCoordinate == 1

    def test_calculatePositionW(self):
        testObj = GameMap()
        testPosition = Position(0, 0)
        newPosition = testObj.CalculatePosition(testPosition, Direction.WEST)
        assert newPosition.xCoordinate == -1
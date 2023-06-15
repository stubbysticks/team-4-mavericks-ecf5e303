from unittest import TestCase
from levelup.gamemap import GameMap
from levelup.position import Position

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
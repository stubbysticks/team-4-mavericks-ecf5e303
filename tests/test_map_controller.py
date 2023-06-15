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
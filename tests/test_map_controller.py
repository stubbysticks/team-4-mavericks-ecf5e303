from unittest import TestCase
from levelup.gamemap import GameMap

class TestGameMap(TestCase):
    def test_init(self):
        testObj = GameMap()
        assert testObj != None
        

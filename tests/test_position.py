from unittest import TestCase
from levelup.position import Position

class TestPositionInitWithCoordinates(TestCase):
    def test_init(self):
        ARBITRARY_X = 1
        ARBITRARY_Y = 1
        testobj = Position(ARBITRARY_X, ARBITRARY_Y)
        self.assertEqual(ARBITRARY_X, testobj.xCoordinate)
        self.assertEqual(ARBITRARY_Y, testobj.yCoordinate)

    def test_get_position(self):
        ARBITRARY_POSITION = (0, 0)
        testobj = Position(ARBITRARY_POSITION[0], ARBITRARY_POSITION[1])
        self.assertEqual(ARBITRARY_POSITION[0], testobj.get_position()[0])
        self.assertEqual(ARBITRARY_POSITION[1], testobj.get_position()[1])

    def test_set_position(self):
        ARBITRARY_POSITION = (0, 0)
        ARBITRARY_NEW_POSITION = (1, 1)
        testobj = Position(ARBITRARY_POSITION[0], ARBITRARY_POSITION[1])
        testobj.set_position(ARBITRARY_NEW_POSITION[0], ARBITRARY_NEW_POSITION[1])
        self.assertEqual(ARBITRARY_NEW_POSITION[0], testobj.get_position()[0])
        self.assertEqual(ARBITRARY_NEW_POSITION[1], testobj.get_position()[1])
from unittest import TestCase
from levelup.character import Character

ARBITRARY_NAME = "MyName"

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        test_obj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, test_obj.name)

    def test_get_name(self):
        test_obj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, test_obj.get_name())

    # def test_get_position(self):
    #     test_obj = Character(ARBITRARY_NAME)
    #     self.assertEqual((0,0), test_obj.get_position())

    # def test_move(self):
    #     test_obj = Character(ARBITRARY_NAME)
    #     direction = 'n'
    #     test_obj.move(direction)
    #     self.assertEqual((0,1), test_obj.get_position())

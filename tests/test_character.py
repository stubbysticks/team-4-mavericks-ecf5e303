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

    def test_get_character_position(self):
        test_obj = Character(ARBITRARY_NAME)
        test_obj.enter_map()
        self.assertEqual(0, test_obj.get_position().get_position_details()[0])
        self.assertEqual(0, test_obj.get_position().get_position_details()[1])

    def test_enter_map(self):
        test_obj = Character(ARBITRARY_NAME)
        test_obj.enter_map()
        self.assertIsNotNone(test_obj.gameMap)

    def test_move(self):
        test_obj = Character(ARBITRARY_NAME)
        test_obj.enter_map()
        direction = 'n'
        test_obj.move(direction)
        self.assertEqual(0, test_obj.get_position().get_position_details()[0])
        self.assertEqual(0, test_obj.get_position().get_position_details()[1])
        self.assertEqual(1, test_obj.total_moves)

    def test_get_total_moves(self):
        test_obj = Character(ARBITRARY_NAME)
        test_obj.enter_map()
        self.assertEqual(0, test_obj.get_total_moves())

    def test_get_status(self):
        test_obj = Character(ARBITRARY_NAME)
        test_obj.enter_map()
        test_character_status = test_obj.get_status()
        assert test_character_status != None
        assert test_character_status != ""
        assert test_character_status == "Your current position is (0, 0) and has moved 0 times."


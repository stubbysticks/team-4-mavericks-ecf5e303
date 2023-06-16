from unittest import TestCase
from levelup.controller import GameController

class TestGameController(TestCase):
    def test_init(self):
        testObj = GameController()
        assert testObj.status != None
        
    def test_create_character(self):
        ARBITRARY_NAME = "NAME"
        testObj = GameController()                                 
        testObj.create_character(ARBITRARY_NAME)
        self.assertIsNotNone(testObj.character)

    def test_enter_map(self):
        ARBITRARY_NAME = "NAME"
        testObj = GameController()
        testObj.create_character(ARBITRARY_NAME)
        testObj.start_game()
        self.assertIsNotNone(testObj.character.gameMap)
        self.assertEqual(0, testObj.character.get_position().get_position_details()[0])
        
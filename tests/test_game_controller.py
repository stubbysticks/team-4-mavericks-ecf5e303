from unittest import TestCase
from levelup.controller import GameController
from levelup import Direction

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
        
    def test_move(self):
        ARBITRARY_NAME = "NAME"
        testObj = GameController()
        testObj.create_character(ARBITRARY_NAME)
        testObj.start_game()
        testObj.move(Direction.NORTH)
        self.assertEqual(1, testObj.character.get_position().get_position_details()[1])

    def test_get_status(self):
        ARBITRARY_NAME = "NAME"
        testObj = GameController()
        testObj.create_character(ARBITRARY_NAME)
        testObj.start_game()
        test_character_status = testObj.get_status()
        assert test_character_status != None
        assert test_character_status != ""
        assert test_character_status == "Your current position is (0, 0) and you have moved 0 times."
        
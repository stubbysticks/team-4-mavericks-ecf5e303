import logging
from typing import Callable
from levelup.controller import GameController, Direction, InvalidMoveException

VALID_DIRECTIONS = [x.value for x in Direction]

class GameApp:

    controller: GameController

    def __init__(self):
        self.controller = GameController()

    def prompt(self, menu: str, validation_fn: Callable[[str], bool]) -> str:
        while True:
            response = input(f"\n{menu}\n> ")
            if validation_fn(response):
                break
        return response

    def create_character(self):
        character = self.prompt("You chose wisely! What is your name?", lambda x: len(x) > 0)
        self.controller.create_character(character)
        print("Nice to meet you, {0}! Welcome to the journey of space exploration...".format(character))

    def move_loop(self):
        while True:
            response = self.prompt(
                f"Where would you like to go? {VALID_DIRECTIONS}\n(or ctrl+c to quit)",
                lambda x: x in VALID_DIRECTIONS,
            )
            if response in VALID_DIRECTIONS:
                direction = Direction(response)
            else:
                print("Direction invalid, please choose again")
                continue
            try:
                self.controller.move(direction)
            except InvalidMoveException:
                print(f"You cannot move {direction}")
            else:
                print(f"You moved {direction.name}")
            print(self.controller.status)

    def start(self):
        self.start_sequence()
        self.create_character()
        self.controller.start_game()
        self.move_loop()

    def start_sequence(self):
        alien = """
       _..._
     .'     '.
    /`\     /`\    |\\
   (__|     |__)|\  \\  /|
   (     "     ) \\ || //
    \         /   \\||//
     \   _   /  |\|`  /
      '.___.'   \____/
       (___)    (___)
     /`     `\  / /
    |         \/ /
    | |     |\  /
    | |     | "`
    | |     |
    | |     |
    |_|_____|
   (___)_____)
   /    \   |
  /   |\|   |
 //||\\  Y  |
|| || \\ |  |
|/ \\ |\||  |
    \||__|__|
     (___|___)
     /   A   \\
    /   / \   \\
   \___/   \___/        
        """
        print (alien)
        print ("\nWelcome, Earthling!\nWe are terribly sorry to hear that your home planet has been decimated by the asteroid. You are welcome to explore our galaxy to find a new home.\n")
        start = self.prompt("Press any key+enter to continue", lambda x: len(x) > 0)


    def quit(self):
        print(f"\n\n{self.controller.status}")

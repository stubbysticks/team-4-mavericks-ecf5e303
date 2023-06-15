from levelup.position import Position


class Character:
    name = ""
    position = Position(0, 0)

    def __init__(self, character_name):
        self.name = character_name

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position
from unittest import TestCase
from levelup.status import Status

class TestStatusInit(TestCase):
    def test_init(self):
        name = 'test'
        x_postion = 0
        y_position = 0
        test_obj = Status(name, x_postion, y_position)
        self.assertEqual(name, test_obj.character_name)
        self.assertEqual(x_postion, test_obj.current_x_postion)
        self.assertEqual(y_position, test_obj.current_y_position)

        
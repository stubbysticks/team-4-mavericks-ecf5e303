class Position:
    xCoordinate = -1
    yCoordinate = -1

    def __init__(self, xCoordinate, yCoordinate):
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate

    def get_position_details(self):
        return (self.xCoordinate, self.yCoordinate)

    def set_position(self, xCoordinate, yCoordinate):
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate

from src.osb.base import Movable, Rotable


class Move:
    def __init__(self, movable: Movable):
        self.movable = movable

    def execute(self):
        self.movable.set_position(
            self.movable.get_position() + self.movable.get_velocity()
        )


class Rotate:
    def __init__(self, rotable: Rotable):
        self.rotable = rotable

    def execute(self):
        direction = (
            (self.rotable.get_direction() + self.rotable.get_angular_velocity()) % self.rotable.get_directions_number()
        )
        self.rotable.set_direction(direction)

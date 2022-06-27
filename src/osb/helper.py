from dataclasses import dataclass


@dataclass
class Vector:
    x: int
    y: int

    def __add__(self, other: 'Vector') -> 'Vector':
        if not isinstance(other, Vector):
            raise TypeError(f"unsupported operand type(s) for +: 'Vector' and '{type(other).__name__}'")

        return Vector(
            self.x + other.x,
            self.y + other.y,
        )

from pytest import raises
from osb.helper import Vector


class TestVector:
    def test_eq(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, -4)

        assert v1 + v2 == Vector(4, -2)

    def test_eq__with_type_error(self):
        with raises(TypeError) as e:
            v = Vector(1, 1) + 10

        assert e.value.args[0] == "unsupported operand type(s) for +: 'Vector' and 'int'"

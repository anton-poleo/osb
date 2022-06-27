from unittest.mock import Mock, call

from pytest import raises

from osb.actions import Move, Rotate
from osb.helper import Vector
from osb.base import Movable, Rotable


class TestMove:
    def test_execute(self):
        calls = [call(Vector(5, 8))]

        movable = Mock(spec=Movable)
        movable.get_position.return_value = Vector(12, 5)
        movable.get_velocity.return_value = Vector(-7, 3)

        move = Move(movable)
        move.execute()

        movable.set_position.assert_has_calls(calls)

    def test_move__with_get_position_error(self):
        movable = Mock(spec=Movable)
        movable.get_position.side_effect = ValueError("test error")

        move = Move(movable)
        with raises(ValueError) as e:
            move.execute()

        assert e.value.args[0] == "test error"

    def test_move__with_get_velocity_error(self):
        movable = Mock(spec=Movable)
        movable.get_velocity.side_effect = ValueError("test error")

        move = Move(movable)
        with raises(ValueError) as e:
            move.execute()

        assert e.value.args[0] == "test error"

    def test_move__with_set_position_error(self):
        movable = Mock(spec=Movable)
        movable.get_position.return_value = Vector(12, 5)
        movable.get_velocity.return_value = Vector(-7, 3)
        movable.set_position.side_effect = ValueError("test error")

        move = Move(movable)
        with raises(ValueError) as e:
            move.execute()

        assert e.value.args[0] == "test error"


class TestRotate:
    def test_execute(self):
        calls = [call(6)]
        rotable = Mock(spec=Rotable)

        rotable.get_direction.return_value = 1
        rotable.get_angular_velocity.return_value = -3
        rotable.get_directions_number.return_value = 8

        rotate = Rotate(rotable)
        rotate.execute()

        rotable.set_direction.assert_has_calls(calls)

    def test_execute__with_get_direction_error(self):
        rotable = Mock(spec=Rotable)
        rotable.get_direction.side_effect = ValueError("test error")

        move = Rotate(rotable)
        with raises(ValueError) as e:
            move.execute()

        assert e.value.args[0] == "test error"

    def test_execute__with_get_angular_velocity_error(self):
        rotable = Mock(spec=Rotable)
        rotable.get_angular_velocity.side_effect = ValueError("test error")

        move = Rotate(rotable)
        with raises(ValueError) as e:
            move.execute()

        assert e.value.args[0] == "test error"

    def test_execute__with_get_directions_number_error(self):
        rotable = Mock(spec=Rotable)
        rotable.get_direction.return_value = 1
        rotable.get_angular_velocity.return_value = -3
        rotable.get_directions_number.side_effect = ValueError("test error")

        move = Rotate(rotable)
        with raises(ValueError) as e:
            move.execute()

        assert e.value.args[0] == "test error"

    def test_execute__with_set_direction_error(self):
        rotable = Mock(spec=Rotable)
        rotable.get_direction.return_value = 1
        rotable.get_angular_velocity.return_value = -3
        rotable.get_directions_number.return_value = 8
        rotable.set_direction.side_effect = ValueError("test error")

        move = Rotate(rotable)
        with raises(ValueError) as e:
            move.execute()

        assert e.value.args[0] == "test error"

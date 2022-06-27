from abc import ABC, abstractmethod

from osb.helper import Vector


class Movable(ABC):
    @abstractmethod
    def get_position(self) -> Vector:
        """"""

    @abstractmethod
    def get_velocity(self) -> Vector:
        """"""

    @abstractmethod
    def set_position(self, new_vector: Vector):
        """"""


class Rotable(ABC):
    @abstractmethod
    def get_direction(self) -> int:
        """"""

    @abstractmethod
    def get_angular_velocity(self) -> int:
        """"""

    @abstractmethod
    def get_directions_number(self):
        """"""

    @abstractmethod
    def set_direction(self, new_direction: int):
        """"""

from collections import namedtuple
from dataclasses import dataclass

from .brakes import Brakes
from .car import Car


@dataclass
class CarLoad:
    car: Car
    lateral_velocity: float
    longitudinal_velocity: float

    @property
    def weight(self) -> float:
        return 9.81 * self.car.body_mass

    @property
    def normal_drag(self) -> float:
        if self.car.normal_drag_factor == 0:
            return 0
        else:
            raise NotImplementedError

    @property
    def lateral_drag(self) -> float:
        if self.car.lateral_drag_factor == 0:
            return 0
        else:
            raise NotImplementedError

    @property
    def longitudinal_drag(self) -> float:
        if self.car.longitudinal_drag_factor == 0:
            return 0
        else:
            raise NotImplementedError


@dataclass
class WheelLoad:
    brakes: Brakes
    braking_force: float
    applied_torque: float

    @property
    def braking_torque(self) -> float:
        return self.braking_force * self.brakes.radial_offset


WheelLoadSet = namedtuple(
    "WheelLoadSet", ["front_right", "front_left", "rear_right", "rear_left"],
)

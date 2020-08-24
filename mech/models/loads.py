from collections import namedtuple
from dataclasses import dataclass

from .brakes import Brakes
from .engine import Engine
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
    car: Car
    braking_level: float
    engine_level: float
    longitudinal_velocity: float

    @property
    def braking_force(self) -> float:
        return self.car.brakes.force(self.braking_level)

    @property
    def braking_torque(self) -> float:
        return self.car.brakes.torque(self.braking_level)

    @property
    def engine_torque(self) -> float:
        return self.car.engine.torque(self.engine_level, self.longitudinal_velocity)


WheelLoadSet = namedtuple(
    "WheelLoadSet", ["front_right", "front_left", "rear_right", "rear_left"],
)

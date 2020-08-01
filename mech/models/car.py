from collections import namedtuple
from dataclasses import dataclass

from .brakes import Brakes
from .engine import Engine
from .wheel import Wheel

WheelSet = namedtuple(
    "WheelSet", ["front_right", "front_left", "rear_right", "rear_left"],
)


@dataclass
class Car:
    body_mass: float = 320
    axle_span: float = 2
    axle_separation: float = 3

    centre_height: float = 0.3
    centre_lateral_offset: float = 0
    centre_longitudinal_offset: float = 0

    normal_drag_factor: float = 0
    lateral_drag_factor: float = 0
    longitudinal_drag_factor: float = 0

    engine: Engine = Engine()
    brakes: Brakes = Brakes()
    wheels: WheelSet = WheelSet(Wheel(), Wheel(), Wheel(), Wheel())

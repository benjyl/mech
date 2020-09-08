from dataclasses import dataclass

from ..models.loads import WheelLoadSet
from ..models.reactions import WheelReactionSet
from .loads import CarLoad
from .track import Trackpoint


@dataclass
class KinemeaticSnapshot:
    lateral_velocity: float
    longitudinal_velocity: float
    lateral_acceleration: float
    longitudinal_acceleration: float


@dataclass
class DynamicSnapshot:
    car_load: CarLoad
    wheel_load_set: WheelLoadSet
    wheel_reaction_set: WheelReactionSet


@dataclass
class ControlSnapshot:
    engine_level: float
    braking_level: float


@dataclass
class Snapshot:
    time: float
    trackpoint: Trackpoint
    control: ControlSnapshot
    dynamics: DynamicSnapshot
    kinemeatics: KinemeaticSnapshot

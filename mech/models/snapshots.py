from dataclasses import dataclass

from simulate.reactions import WheelReactionSet, WheelLoadSet

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
class Snapshot:
    time: float
    trackpoint: Trackpoint
    dynamics: DynamicSnapshot
    kinemeatics: KinemeaticSnapshot

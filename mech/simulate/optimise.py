from typing import Iterator

from ..models.car import Car
from ..models.snapshots import KinemeaticSnapshot, DynamicSnapshot, Snapshot
from ..models.track import Trackpoint
from ..models.loads import CarLoad, WheelLoad, WheelLoadSet
from ..models.reactions import ReactionSet, WheelReactionSet


def optimal_velocity(car: Car, trackpoints: Iterator[Trackpoint]) -> Iterator[Snapshot]:
    for trackpoint in trackpoints:
        car_load = CarLoad(car, longitudinal_velocity, lateral_velocity)
        wheel_load = WheelLoad(car, longitudinal_velocity, braking_level, engine_level)
        wheel_load_set = WheelLoadSet.s

        wheel_reactions = 0

        dynamic_snapshot = DynamicSnapshot(
            car_load, wheel_loads, wheel_reactions(car_load, wheel_loads)
        )

        kinemeatic_snapshot = KinemeaticSnapshot(
            longitudinal_velocity,
            lateral_velocity,
            longitudinal_acceleration,
            lateral_acceleration,
        )

        yield Snapshot

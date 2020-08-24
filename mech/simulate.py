from typing import Iterator

from .models.car import Car
from .models.snapshots import KinemeaticSnapshot, DynamicSnapshot, Snapshot
from .models.track import Trackpoint
from .models.loads import CarLoad, WheelLoad, WheelLoadSet
from .models.reactions import ReactionSet, WheelReactionSet


def simulate(car: Car, trackpoints: Iterator[Trackpoint]) -> Iterator[Snapshot]:
    for trackpoint in trackpoints:

        time = 0

        longitudinal_velocity = 0
        lateral_velocity = 0

        longitudinal_acceleration = 0
        lateral_acceleration = 0

        braking_level = 0
        engine_level = 0

        car_load = CarLoad(car, longitudinal_velocity, lateral_velocity)
        wheel_loads = WheelLoadSet(
            *[WheelLoad(car, longitudinal_velocity, braking_level, engine_level)] * 4
        )

        dynamic_snapshot = DynamicSnapshot(
            car_load, wheel_loads, wheel_reactions(car_load, wheel_loads)
        )

        kinemeatic_snapshot = KinemeaticSnapshot(
            longitudinal_velocity,
            lateral_velocity,
            longitudinal_acceleration,
            lateral_acceleration,
        )

        yield Snapshot(time, trackpoint, dynamic_snapshot, kinemeatic_snapshot)


def wheel_reactions(car_load: CarLoad, wheel_loads: WheelLoadSet) -> WheelReactionSet:
    no_reaction = ReactionSet(0, 0, 0)
    return WheelReactionSet(*[no_reaction] * 4)

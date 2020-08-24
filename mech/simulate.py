from typing import Iterator

from .models.car import Car
from .models.snapshots import Snapshot
from .models.track import Trackpoint


def simulate(car: Car, trackpoints: Iterator[Trackpoint]) -> Iterator[Snapshot]:
    return iter([])

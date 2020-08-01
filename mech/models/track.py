from dataclasses import dataclass


@dataclass
class Trackpoint:
    index: int
    arc_length: float
    radius_of_curvature: float

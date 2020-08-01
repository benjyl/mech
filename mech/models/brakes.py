from dataclasses import dataclass


@dataclass
class Brakes:
    max_force: float = 50
    brake_radial_offset: float = 0.1

from dataclasses import dataclass


@dataclass
class Brakes:
    max_force: float = 50
    radial_offset: float = 0.1

    def braking_force(self, braking_level: float) -> float:
        return braking_level * self.max_force

    def braking_torque(self, braking_level: float) -> float:
        return self.radial_offset * self.braking_force(braking_level)

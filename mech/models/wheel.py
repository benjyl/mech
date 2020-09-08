from dataclasses import dataclass

import numpy as np

from .base import QuadrigeminalSet, Vector


@dataclass
class Wheel:
    wheel_mass: float = 10
    wheel_width: float = 0.2
    wheel_radius: float = 0.15

    shape_factor: float = 0.0180
    stiffness_factor: float = 18.6206
    curvature_factor: float = 1.1095

    max_slip_angle: float = 30
    max_slip_ratio: float = 30

    def pacejka(self, combined_slip: float, horizontal_shift: float) -> float:
        pacejka_contant = 0.0174533
        slip_factor = pacejka_contant * combined_slip + horizontal_shift
        x = self.stiffness_factor * slip_factor
        y = x - np.arctan(x)
        z = self.stiffness_factor * slip_factor - y * self.curvature_factor
        return float(np.sin(self.shape_factor * np.arctan(z)))

    @property
    def max_lateral_force(self) -> float:
        return max(
            self.pacejka(combined_slip=slip_angle, horizontal_shift=0)
            for slip_angle in np.linspace(0, self.max_slip_angle, 30)
        )

    @property
    def max_longitudinal_force(self) -> float:
        return max(
            self.pacejka(combined_slip=slip_ratio, horizontal_shift=0)
            for slip_ratio in np.linspace(0, self.max_slip_ratio, 30)
        )


class WheelSet(QuadrigeminalSet[Wheel]):
    pass

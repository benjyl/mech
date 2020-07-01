from dataclasses import dataclass
import numpy as np


@dataclass
class Wheel:
    torque: float = 0
    lateral_force: float = 0
    normal_force: float = 0

    stiffness_factor: float = 18.6206
    shape_factor: float = 0.0180
    curvature_factor: float = 1.1095

    @property
    def longitudinal_force(self):
        return (
            self.max_longitudinal_force(
                1 - self.lateral_force ** 2 / self.max_lateral_force ** 2
            )
            ** 0.5
        )

    @property
    def peak_force(self):
        return 3.5223 * 10 ** 4 * np.asarray(self.normal_force) / 180 * 0.6

    def pacejka(self, combined_slip):
        horizontal_shift = 0
        x = 0.0174533 * combined_slip + horizontal_shift
        return np.sin(
            self.shape_factor
            * np.arctan(
                self.stiffness_factor * x
                - self.curvature_factor
                * (self.stiffness_factor * x - np.arctan(self.stiffness_factor * x))
            )
        )

    @property
    def max_lateral_force(self):
        slip_angle_range = np.linspace(-15, 15, 30)
        slip_ratio_range = np.zeroes(30)
        combined_slip = slip_angle_range
        return max(self.pacejka(combined_slip))

    @property
    def max_longitudinal_force(self):
        slip_angle_range = np.zeroes(30)
        slip_ratio_range = np.linspace(-15, 15, 30)
        combined_slip = slip_ratio_range
        return max(self.pacejka(combined_slip))


@dataclass
class Car:
    mass: int = 300
    displacement: float = 0
    velocity: float = 0
    acceleration: float = 0
    wheelbase: float = 1.55
    cog_height: float = 0.3
    weight_distrib: float = 0.5
    drive_ratio: float = 3
    motor_power: int = 80000
    max_torque: int = 240
    wheel_radii: float = 0.175
    fl_wheel: Wheel = Wheel()
    fr_wheel: Wheel = Wheel()
    bl_wheel: Wheel = Wheel()
    br_wheel: Wheel = Wheel()

    def update_wheel_torques(self):
        av_wheel_ang_speed = self.velocity / self.wheel_radii
        motor_speed = av_wheel_ang_speed * drive_ratio
        motor_torque = min(self.max_torque, self.motor_power / motor_speed)
        rear_torque = motor_torque * drive_ratio

        self.fr_wheel.torque = 0
        self.fl_wheel.torque = 0
        self.br_wheel.torque = rear_torque / 2
        self.bl_wheel.torque = rear_torque / 2

    def update_wheel_forces(self, turn_radius):
        g = 9.81
        frontal_normal_force = (
            self.mass
            * (
                g * self.weight_distrib * self.wheelbase
                - self.acceleration * self.cog_height
            )
            / self.wheelbase
        )
        rear_normal_force = self.mass * g - frontal_normal_force
        total_normal_force = frontal_normal_force + rear_normal_force

        self.fr_wheel.normal_force = frontal_normal_force / 2
        self.fl_wheel.normal_force = frontal_normal_force / 2
        self.br_wheel.normal_force = rear_normal_force / 2
        self.bl_wheel.normal_force = rear_normal_force / 2

        centripetal_force = self.mass * self.velocity ** 2 / turn_radius

        self.fr_wheel.lateral_force = (
            centripetal_force * self.fr_wheel.normal_force / total_normal_force
        )
        self.fl_wheel.lateral_force = (
            centripetal_force * self.fl_wheel.normal_force / total_normal_force
        )
        self.br_wheel.lateral_force = (
            centripetal_force * self.br_wheel.normal_force / total_normal_force
        )
        self.bl_wheel.lateral_force = (
            centripetal_force * self.bl_wheel.normal_force / total_normal_force
        )

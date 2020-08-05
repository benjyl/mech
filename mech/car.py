from dataclasses import dataclass

import numpy as np


@dataclass
class Wheel:

    # Dynamics
    axle_load: float = 0
    axle_torque: float = 0
    full_normal_force: float = 0

    # Model factors
    shape_factor: float = 0.0180
    stiffness_factor: float = 18.6206
    curvature_factor: float = 1.1095
    

    @property
    def normal_force(self):
        self.full_normal_force = self.axle_load / 2

    def lateral_force(self, centripetal_force, total_normal_force):

        print(type(total_normal_force), total_normal_force)
        return centripetal_force * self.full_normal_force / total_normal_force

    def longitudinal_force(self, centripetal_force, acceleration, total_normal_force):
        return (
            np.sign(acceleration)
            * self.max_longitudinal_force
            * (
                1
                - abs(self.lateral_force(centripetal_force, total_normal_force)) ** 2
                / self.max_lateral_force ** 2
            )
            ** 0.5
        )

    def pacejka(self, combined_slip):
        horizontal_shift = 0
        x = 0.0174533 * combined_slip + horizontal_shift
        d = 3.5223*10**4 * 0.5 * self.axle_load / 180 * 0.6
        return d * np.sin(
            self.shape_factor
            * np.arctan(
                self.stiffness_factor * x
                - self.curvature_factor
                * (self.stiffness_factor * x - np.arctan(self.stiffness_factor * x))
            )
        )

    @property
    def max_lateral_force(self):
        slip_angle_range = np.linspace(0, 15, 30)
        np.zeros(30)
        combined_slip = slip_angle_range
        return max(self.pacejka(combined_slip))

    @property
    def max_longitudinal_force(self):
        np.zeros(30)
        slip_ratio_range = np.linspace(0, 15, 30)
        combined_slip = slip_ratio_range
        return max(self.pacejka(combined_slip))

    @property
    def torque(self):
        return self.axle_torque / 2


@dataclass
class Car:

    # Dynamics
    mass: int = 300
    velocity: float = 0
    acceleration: float = 0
    centripetal_force: float = 0
    tot_normal_force: float = 0

    # Dimensions
    wheelbase: float = 1.55
    centre_height: float = 0.3
    wheel_radii: float = 0.175

    # Load distributions
    weight_distribution: float = 0.5
    aero_load_distribution: float = 0.5

    # Motor properties
    drive_ratio: float = 3
    motor_power: int = 80000
    max_torque: int = 240

    # Wheels
    model_front_wheel: Wheel = Wheel()
    model_rear_wheel: Wheel = Wheel()

    def update_wheel_loads(self, normal_aero_load=0):
        g = 9.81
        
        self.model_front_wheel.axle_load = (
            self.mass
            * (
                g * self.weight_distribution * self.wheelbase
                - self.acceleration * self.centre_height
            )
            / self.wheelbase
        ) + normal_aero_load * self.aero_load_distribution

        self.model_rear_wheel.axle_load = (
            self.mass * g
            + normal_aero_load * (1 - self.aero_load_distribution)
            - self.model_front_wheel.axle_load
        )

    @property
    def total_normal_force(self):
        self.tot_normal_force = self.model_front_wheel.axle_load + self.model_rear_wheel.axle_load

    def update_wheel_torques(self):
        av_wheel_ang_speed = self.velocity / self.wheel_radii
        motor_speed = av_wheel_ang_speed * self.drive_ratio
        motor_torque = min(self.max_torque, self.motor_power / motor_speed)

        self.model_front_wheel.axle_torque = 0
        self.model_rear_wheel.axle_torque = motor_torque * self.drive_ratio

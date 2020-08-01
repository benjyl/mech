from dataclasses import dataclass


@dataclass
class Engine:
    drive_ratio: float = 3
    max_torque: float = 240
    motor_power: float = 80000

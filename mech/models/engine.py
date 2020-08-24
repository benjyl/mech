from dataclasses import dataclass


@dataclass
class Engine:
    drive_ratio: float = 3
    max_torque: float = 240
    motor_power: float = 80000

    def torque(self, engine_level: float, longitudinal_velocity: float) -> float:
        produced_torque = (
            min(self.motor_power / longitudinal_velocity, self.max_torque)
            if longitudinal_velocity != 0
            else self.max_torque
        )

        return self.drive_ratio * engine_level * produced_torque

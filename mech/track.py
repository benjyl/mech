from typing import Optional
from dataclasses import dataclass


@dataclass
class Trackpoint:
    index: int
    distance: float
    curvature_radius: float
    time: Optional[float] = None
    velocity: Optional[float] = None
    acceleration: Optional[float] = None
    longitudinal_force: Optional[float] = None
    lateral_force: Optional[float] = None
    normal_force: Optional[float] = None

    @staticmethod
    def from_csv(dist_file_path, radius_file_path):
        with open(dist_file_path, "r") as dist_file, open(
            radius_file_path, "r"
        ) as radius_file:
            return [
                Trackpoint(index, float(distance), float(radius))
                for index, (distance, radius) in enumerate(
                    zip(dist_file.read().split(","), radius_file.read().split(","))
                )
            ]

    def update(self, time, car):
        self.time = time
        self.velocity = car.velocity
        self.acceleration = car.acceleration
        self.lateral_force = car.centripetal_force
        self.normal_force = car.total_normal_force
        self.longitudinal_force = (
            car.model_front_wheel.longitudinal_force(
                car.centripetal_force, car.acceleration, car.total_normal_force
            )
            + car.model_front_wheel.longitudinal_force(
                car.centripetal_force, car.acceleration, car.total_normal_force
            )
        ) * 2

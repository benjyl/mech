import numpy as np
from track import Trackpoint
from plot import plot_trackpoints
from car import Car


if __name__ == "__main__":

    # Initialise a car and trackpoints
    car = Car(velocity=0, acceleration=10, centripetal_force=0)
    trackpoints = Trackpoint.from_csv("fixtures/dist.csv", "fixtures/radius.csv")
    
    trackpoints[0].update(time=0, car=car)

    for prev_point, point in zip(trackpoints[:-1], trackpoints[1:]):
        suvat_velocity = (
            prev_point.velocity ** 2
            + 2 * prev_point.acceleration * (point.distance - prev_point.distance)
        ) ** 0.5

        centripetal_limited_velocity = 0 

        time = 0
        car.velocity = min(centripetal_limited_velocity, suvat_velocity)
        car.acceleration = 0
        car.centripetal_force = 0

        # Record the telemetry data at this point on the track
        point.update(time, car)

    plot_trackpoints(trackpoints[:200])
    # acceleration <= min(power_acceleration_limit, braking_acceleration_model)

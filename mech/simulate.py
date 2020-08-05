import numpy as np
from track import Trackpoint
from plot import plot_trackpoints
from car import Car


if __name__ == "__main__":

    # Initialise a car and trackpoints
    car = Car(velocity=0, acceleration=10, centripetal_force=0)
    trackpoints = Trackpoint.from_csv("fixtures/dist.csv", "fixtures/radius.csv")
    time = 0
    suvat_velocity = 0

#    trackpoints[0].update(time=0, car=car)

    # need to update acceleration at all points except last so start with first point
    for point, next_point in zip(trackpoints[:-1], trackpoints[1:]):

        prev_acceleration = 50

        # tolerance for acceleration
        while abs((car.acceleration - prev_acceleration) / prev_acceleration) > 0.1:

            # finding the loads on front and rear axles
            car.update_wheel_loads()
            # print(car.model_front_wheel.axle_load)
            # storing normal forces at front and rear of cars
            front_normal_force = 2*car.model_front_wheel.full_normal_force
            rear_normal_force = car.model_rear_wheel.full_normal_force

            # using method to update total normal force in the car
            car.total_normal_force
            print(car.tot_normal_force)
    
            # finding max possible lateral forces on both axles
            front_max_lateral = car.model_front_wheel.max_lateral_force
            rear_max_lateral = car.model_rear_wheel.max_lateral_force

            # summing all lateral forces multiply by 2 as 2 wheels at front and rear
            total_lateral = 2 * front_max_lateral + 2 * rear_max_lateral
            # print(front_max_lateral, rear_max_lateral, total_lateral)
    

            # finding velocity at all points purely on maximum lateral force and curvature radius
            centripetal_limited_velocity = abs(
                np.sqrt(total_lateral * point.curvature_radius / car.mass)
            )
            
            # checking which velocity is lower and storing as car's velocity
            car.velocity = min(centripetal_limited_velocity, suvat_velocity)

            # finding car's actual centripetal force
            car.centripetal_force = (
                car.mass * car.velocity ** 2
            ) / point.curvature_radius

            # finding actual lateral forces at front and rear using lateral force method
            front_lateral = car.model_front_wheel.lateral_force(
                car.centripetal_force, car.tot_normal_force
            )
            rear_lateral = car.model_rear_wheel.lateral_force(
                car.centripetal_force, car.tot_normal_force
            )

            # finding actual longitudinal forces based on lateral forces
            front_longitudinal = car.model_front_wheel.longitudinal_force(
                car.centripetal_force, car.acceleration, car.tot_normal_force
            )
            rear_longitudinal = car.model_rear_wheel.longitudinal_force(
                car.centripetal_force, car.acceleration, car.tot_normal_force
            )

            total_longitudinal_force = front_longitudinal + rear_longitudinal

            # find wheel torques based on car velocity
            car.update_wheel_torques

            # Finding forces at wheels based on max torque
            wheel_force = car.model_rear_wheel.axle_torque / car.wheel_radii

            # finding limiting longitudinal force for acceleration
            total_longitudinal_force = min(total_longitudinal_force, wheel_force)

            #updating acceleration values
            prev_acceleration = car.acceleration
            car.acceleration = total_longitudinal_force / car.mass

            # Record the telemetry data at this point on the track
            point.update(time, car)

            # updating suvat velocity need it for the next trackpoint though not current
            # not sure how to solve this, potentially make a list of suvat velocities?
            suvat_velocity = (
                point.velocity ** 2
                + 2 *point.acceleration * (next_point.distance - point.distance)
            ) ** 0.5

        # update time, need to use the previous and current trackpoints but only zipped current and next
        # time += 2*
    plot_trackpoints(trackpoints[:200])
    # acceleration <= min(power_acceleration_limit, braking_acceleration_model)

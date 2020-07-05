import numpy as np
from car import Car

if __name__ == "__main__":
    car = Car()

    # using dist from matlab
    track = np.linspace(0, 1200, 600)

    # # Still to define corner radius
    # max_corner_speed = np.sqrt(abs((total_f_lat * corner_radius) / mass))
    # power_lim_speed[i] = min(power_lim_speed, max_corner_speed)
    # max_real_lat_force = (car.mass * power_lim_speed[i] ** 2) / corner_radius

    # wheel_torque = torque(
    #     power_lim_speed[i], car
    # )
    # wheel_force = wheel_torque / car.wheel_radius

    # f_long_real = min(f_long_real, wheel_force)
    # f_long_tot = sum(f_long_real)

    # # Add aero forces
    # # f_long_tot -= aero_forces
    # prev_accel = accel
    # accel = f_long_tot / car.mass

    # power_lim_speed[i + 1] = np.sqrt(
    #     power_lim_speed[i] ** 2 + 2 * accel * (track[i + 1] - track[i])
    # )

    # prev_accel = 0
    
    # if max_corner_speed > 80:
    #     pass

import numpy as np
import math as mt
import matplotlib.pyplot as plt
from car import Car


if __name__ == "__main__":
    car = Car()
    track = np.linspace(0, 1200, 600)

    # force_array = np.zeros((len(track), 4))
    # force_lim_speed = np.zeros(len(track))
    # power_lim_speed = np.zeros(len(track))
    # brake_lim_speed = np.zeros(len(track))

    # for i in range(len(track) - 1):
    #     accel = 0

    #     # arbitrary value that is just to start loop
    #     prev_accel = 50
    #     while abs(accel - prev_accel) / abs(prev_accel) > 0.01:
    #         fz_fl, fz_fr, fz_bl, fz_br = forces(accel, car)

    #         # finding the max lateral force
    #         slip_angles = np.linspace(-15, 15, 30)
    #         slip_ratios = np.zeros(30)

    #         fx_lat, fy_lat = pacejka(
    #             slip_angles, slip_ratios, [fz_fl, fz_fr, fz_bl, fz_br]
    #         )
    #         fy_lat_array = np.array(fy_lat)

    #         # fl_f_lat_max represents the maximum lateral force on the front left tyre
    #         fl_f_lat_max, fr_f_lat_max, bl_f_lat_max, br_f_lat_max = fy_lat_array.max(
    #             axis=1
    #         )

    #         # finding max longitudinal force
    #         slip_angles = np.zeros(30)
    #         slip_ratios = np.linspace(-1, 1, 30)
    #         fx_long, fy_long = pacejka(
    #             slip_angles, slip_ratios, [fz_fl, fz_fr, fz_bl, fz_br]
    #         )
    #         fx_long_array = np.array(fx_long)
    #         (
    #             fl_f_long_max,
    #             fr_f_long_max,
    #             bl_f_long_max,
    #             br_f_long_max,
    #         ) = fx_long_array.max(axis=1)

    #         total_f_lat = sum(fy_lat_array.max(axis=1))
    #         force_lim_vel = np.zeros(len(track))

    #         # still to define corner radius
    #         max_corner_speed = np.sqrt(abs((total_f_lat * corner_radius) / mass))
    #         power_lim_speed[i] = min(power_lim_speed, max_corner_speed)
    #         max_real_lat_force = (car.mass * power_lim_speed[i] ** 2) / corner_radius

    #         fz_sum = sum(fz_fl, fz_fr, fz_bl, fz_br)
    #         fl_f_lat_real = fz_fl / fz_sum * max_real_lat_force
    #         fl_f_long_real = np.sqrt(
    #             (1 - fl_f_lat_real ** 2 / fl_f_lat_max ** 2) * fl_f_long_max ** 2
    #         )

    #         fr_f_lat_real = fz_fr / fz_sum * max_real_lat_force
    #         fr_f_long_real = np.sqrt(
    #             (1 - fr_f_lat_real ** 2 / fr_f_lat_max ** 2) * fr_f_long_max ** 2
    #         )

    #         bl_f_lat_real = fz_bl / fz_sum * max_real_lat_force
    #         bl_f_long_real = np.sqrt(
    #             (1 - bl_f_lat_real ** 2 / bl_f_lat_max ** 2) * bl_f_long_max ** 2
    #         )

    #         br_f_lat_real = fz_br / fz_sum * max_real_lat_force
    #         br_f_long_real = np.sqrt(
    #             (1 - br_f_lat_real ** 2 / br_f_lat_max ** 2) * br_f_long_max ** 2
    #         )

    #         f_long_real = [
    #             fl_f_long_real,
    #             fr_f_long_real,
    #             bl_f_long_real,
    #             br_f_long_real,
    #         ]

    #         wheel_torque = torque(
    #             power_lim_speed[i], car
    #         )
    #         wheel_force = wheel_torque / car.wheel_radius

    #         f_long_real = min(f_long_real, wheel_force)
    #         f_long_tot = sum(f_long_real)

    #         # add aero forces
    #         # f_long_tot -= aero_forces
    #         prev_accel = accel
    #         accel = f_long_tot / car.mass

    #         power_lim_speed[i + 1] = np.sqrt(
    #             power_lim_speed[i] ** 2 + 2 * accel * (track[i + 1] - track[i])
    #         )

    #         prev_accel = 0
    #     if max_corner_speed > 80:
    #         pass

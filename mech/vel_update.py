import numpy as np
import math as mt
import matplotlib.pyplot as plt


def deg_to_rad(a):
    """[turns an angle in degrees into an angle in radians]

    Args:
        a ([float]): [input in radians]
    """
    return a * np.pi / 180


def forces(mass, wheelbase, cog_height, acceleration, front_weight_distrib, g):
    """This defines the forces at the 4 wheels at each time interval
    

    Args:
        mass ([integer]): [mass of the car]
        wheelbase ([float]): [car wheelbase length]
        cog_height ([float]): [height of the car's centre of gravity]
        acceleration ([float]): [the acceleration of the car]
        front_weight_distrib ([float]): [percentage of weight acting over the front wheels]
    
    Returns:
        Array of the 4 forces in z direction
        [force front left, force front right, force rear left, force rear right] 
    """

    force_z = np.zeros(4)
    force_z_front = (
        mass
        * (g * front_weight_distrib * wheelbase - acceleration * cog_height)
        / wheelbase
    )
    force_z[0] = force_z[1] = force_z_front / 2
    force_z[2] = force_z[3] = (mass * g - force_z_front) / 2
    print(force_z)
    return force_z


def pacejka(sa, sl, fz):
    """[this function applies the pacejka model to the tyres]

    Args:
        sa ([array]): [array of slip angles]
        sl ([array]): [array slip ratio]
        fz ([array]): [array of vertical forces on all tyres]

    Returns:
        Array of floating points, forces on all 4 tyres
    """
    # multiply sl by the maximum slip angle input  to get sa, sl circle
    sl = sl * max(sa)

    # combined slip parameter
    sm = np.sqrt(sa ** 2 + sl ** 2)

    # b is the stiffness factor
    b = 18.6206
    # c is the shape factor
    c = 0.0180
    # d is the peak force
    d = 3.5223 * 10 ** 4 * np.asarray(fz) / 180 * 0.6

    # e is the curvature factor
    e = 1.1095

    # horizontal shift
    # force due to resistance in longitudinal data @ 0 slip angle
    sh = 0

    x = 0.0174533 * sm + sh

    forces = []
    for i in d:
        y = i * np.sin(c * np.arctan(b * x - e * (b * x - np.arctan(b * x))))
        forces.append(y)

    theta = np.arctan((np.divide(sl, sa)))
    for i in range(len(theta)):
        if mt.isnan(theta[i]):
            theta[i] = -90
    print("theta: ", theta)

    f_lat_list = []
    f_long_list = []
    for f in forces:
        f_long_list.append(
            abs(np.multiply(f, (np.sin(deg_to_rad(theta))))) * np.sign(sl)
        )
        f_lat_list.append(
            abs(np.multiply(f, (np.cos(deg_to_rad(theta))))) * np.sign(sa)
        )

    print(f_long_list)
    print(f_lat_list)

    # mz = zeros(len(sa))

    return f_long_list, f_lat_list


def torque(velocity, tyre_radius, drive_ratio, torque, power):
    """[summary]

    Args:
        velocity ([float]): [velocity of car at current instance]
        tyre_radius ([float]): [radius of the tyres]
        drive_ratio ([float]): [gives the value of the drive_ratio of the gears]
        torque ([integer]): [the maximum torque produced by the motor]
        power ([integer]): [the maximum power produced by the motor]
    
    Returns:
        Returns the torque at all 4 wheels
    """

    wheel_ang_speed = velocity / radius
    motor_speed = wheel_ang_speed * drive_ratio
    motor_torque = min(torque, power / motor_speed)

    torque_fr = torque_fl = 0
    torque_br = torque_bl = motor_torque * drive_ratio / 2

    return torque_fl, torque_fr, torque_bl, torque_br


if __name__ == "__main__":
    track = np.linspace(0, 1200, 600)
    g = 9.81
    mass = 300
    wheelbase = 1.55
    cog_height = 0.3
    weight_distrib = 0.5
    force_array = np.zeros((len(track), 4))
    wheel_radius = 0.175
    drive_ratio = 3
    motor_torque = 240
    motor_power = 80000

    force_lim_speed = np.zeros(len(track))
    power_lim_speed = np.zeros(len(track))
    brake_lim_speed = np.zeros(len(track))
    for i in range(len(track) - 1):
        accel = 0
        # arbitrary value that is just to start loop
        prev_accel = 50
        while abs(accel - prev_accel) / abs(prev_accel) > 0.01:
            fz_fl, fz_fr, fz_bl, fz_br = forces(
                mass, wheelbase, cog_height, accel, weight_distrib, g
            )

            # finding the max lateral force

            slip_angles = np.linspace(-15, 15, 30)
            slip_ratios = np.zeros(30)

            fx_lat, fy_lat = pacejka(
                slip_angles, slip_ratios, [fz_fl, fz_fr, fz_bl, fz_br]
            )
            fy_lat_array = np.array(fy_lat)
            # fl_f_lat_max represents the maximum lateral force on the front left tyre
            fl_f_lat_max, fr_f_lat_max, bl_f_lat_max, br_f_lat_max = fy_lat_array.max(
                axis=1
            )

            # finding max longitudinal force

            slip_angles = np.zeros(30)
            slip_ratios = np.linspace(-1, 1, 30)
            fx_long, fy_long = pacejka(
                slip_angles, slip_ratios, [fz_fl, fz_fr, fz_bl, fz_br]
            )
            fx_long_array = np.array(fx_long)
            (
                fl_f_long_max,
                fr_f_long_max,
                bl_f_long_max,
                br_f_long_max,
            ) = fx_long_array.max(axis=1)
            print(fl_f_long_max)

            total_f_lat = sum(fy_lat_array.max(axis=1))

            force_lim_vel = np.zeros(len(track))

            # still to define corner radius
            max_corner_speed = np.sqrt(abs((total_f_lat * corner_radius) / mass))

            power_lim_speed[i] = min(power_lim_speed, max_corner_speed)
            max_real_lat_force = (mass * power_lim_speed[i] ** 2) / corner_radius

            fz_sum = sum(fz_fl, fz_fr, fz_bl, fz_br)

            fl_f_lat_real = fz_fl / fz_sum * max_real_lat_force
            fl_f_long_real = np.sqrt(
                (1 - fl_f_lat_real ** 2 / fl_f_lat_max ** 2) * fl_f_long_max ** 2
            )

            fr_f_lat_real = fz_fr / fz_sum * max_real_lat_force
            fr_f_long_real = np.sqrt(
                (1 - fr_f_lat_real ** 2 / fr_f_lat_max ** 2) * fr_f_long_max ** 2
            )

            bl_f_lat_real = fz_bl / fz_sum * max_real_lat_force
            bl_f_long_real = np.sqrt(
                (1 - bl_f_lat_real ** 2 / bl_f_lat_max ** 2) * bl_f_long_max ** 2
            )

            br_f_lat_real = fz_br / fz_sum * max_real_lat_force
            br_f_long_real = np.sqrt(
                (1 - br_f_lat_real ** 2 / br_f_lat_max ** 2) * br_f_long_max ** 2
            )

            f_long_real = [
                fl_f_long_real,
                fr_f_long_real,
                bl_f_long_real,
                br_f_long_real,
            ]

            wheel_torque = torque(
                power_lim_speed[i], wheel_radius, drive_ratio, motor_torque, motor_power
            )
            wheel_force = wheel_torque / wheel_radius

            f_long_real = min(f_long_real, wheel_force)
            f_long_tot = sum(f_long_real)
            # add aero forces
            # f_long_tot -= aero_forces

            prev_accel = accel
            accel = f_long_tot / mass

            power_lim_speed[i + 1] = np.sqrt(
                power_lim_speed[i] ** 2 + 2 * accel * (track[i + 1] - track[i])
            )

            prev_accel = 0
        if max_corner_speed > 80:
            pass

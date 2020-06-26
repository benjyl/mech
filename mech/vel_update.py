import numpy as np
import math as mt

def forces(mass, wheelbase, cog_height, acceleration, weight_distrib, g):
    """This defines the forces at the 4 wheels at each time interval
        returns an array of the 4 forces
cd
    Args:
        mass ([integer]): [mass of the car]
        wheelbase ([float]): [car wheelbase length]
        cog_height ([float]): [height of the car's centre of gravity]
        acceleration ([float]): [the acceleration of the car]
        weight_distrib ([float]): [how much of the weigth is towards the front of the car]
    """

    force_z = np.zeros(4)
    force_z_front = (
        mass * (g * weight_distrib * wheelbase - acceleration * cog_height) / wheelbase
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
    """
    sl = sl * 30
    sm = mt.sqrt(sa**2 + sl**2)
    b = 18.6206
    c = 0.0180
    d = 3.5223*10**4 * (-fz/180) * 0.6
    e = 1.1095

#horizontal shift
    sh = 0

    x = 0.0174533 * sm + sh
    y = d*np.sin(c*np.arctan(b*x - e*(b*x - np.arctan(b*x))))



if __name__ == "__main__":
    acceleration = 0.3
    g = 9.81
    mass = 300
    wheelbase = 1.55
    cog_height = 0.3
    weight_distrib = 0.5
    fz_fl, fz_fr, fz_bl, fz_br = forces(
        mass, wheelbase, cog_height, acceleration, weight_distrib, g
    )



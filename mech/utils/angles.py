import numpy as np


def deg_to_rad(theta: float) -> float:
    """
    Turns an angle in degrees into an angle in radians

    Args:
        theta (float): Input in radians

    Returns: Theta converted to degrees
    """
    return theta * np.pi / 180

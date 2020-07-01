import sys

import numpy as np

from mech.utils import deg_to_rad

sys.path.append("..")


def test_deg_to_rad():
    assert deg_to_rad(0) == 0
    assert deg_to_rad(90) == np.pi / 2
    assert deg_to_rad(180) == np.pi

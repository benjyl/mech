from collections import namedtuple
from dataclasses import dataclass


@dataclass
class ReactionSet:
    normal_reaction: float
    lateral_reaction: float
    longitudinal_reaction: float


WheelReactionSet = namedtuple(
    "WheelReactionSet", ["front_right", "front_left", "rear_right", "rear_left"],
)

from typing import Optional

class Trackpoint:

    x: float
    y: float
    distance: float
    radius_curve: float
    time: Optional[float] = None
    speed: Optional[float] = None
    acceleration: Optional[float] = None
    longitudinal_force: Optional[float] = None
    lateral_force: Optional[float] = None
    normal_force: Optional[float] = None
    
    
    @staticmethod
    def from_csv(file_path):
        pass

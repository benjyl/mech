import argparse
from typing import List, Tuple

from ..models.car import Car
from ..models.track import Trackpoint
from .model_loader import load_car_model
from .track_loader import load_track

parser = argparse.ArgumentParser(description="Simulate ")
parser.add_argument("-c", "--car-model", help="", required=False)
parser.add_argument("-a", "--arc-length", help="", required=True)
parser.add_argument("-r", "--radius-of-curvature", help="", required=True)


def load_config() -> Tuple[Car, List[Trackpoint]]:
    cli_arguments = vars(parser.parse_args())

    car_model_yaml = cli_arguments["car_model"]
    arc_length_csv = cli_arguments["arc_length"]
    radii_of_curvature_csv = cli_arguments["radius_of_curvature"]

    car_model = load_car_model(car_model_yaml) if car_model_yaml else Car()
    trackpoints = load_track(arc_length_csv, radii_of_curvature_csv)
    return car_model, trackpoints

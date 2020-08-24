from __future__ import annotations

import argparse
import os
from dataclasses import dataclass
from typing import Iterator, TypeVar

from ..models.car import Car
from ..models.track import Trackpoint
from .car_parser import parse_car
from .trackpoints_parser import parse_trackpoints

T = TypeVar("T")

parser = argparse.ArgumentParser(description="Simulate ")
parser.add_argument("-c", "--car-model", required=False)
parser.add_argument("-a", "--arc-length", required=True)
parser.add_argument("-r", "--radius-of-curvature", required=True)
parser.add_argument("-o", "--output-path", required=False)


@dataclass
class CliInput:
    car: Car
    trackpoints: Iterator[Trackpoint]
    output_path: str

    @classmethod
    def parse_cli(cls) -> CliInput:
        raw_arguments = vars(parser.parse_args())

        car_model_yaml = raw_arguments["car_model"]
        car = parse_car(car_model_yaml) if car_model_yaml else Car()

        arc_length_csv = raw_arguments["arc_length"]
        radii_of_curvature_csv = raw_arguments["radius_of_curvature"]
        trackpoints = parse_trackpoints(arc_length_csv, radii_of_curvature_csv)

        output_path = raw_arguments["output_path"] or os.path.join(
            os.getcwd(), "snapshots.yml"
        )
        return cls(car, trackpoints, output_path)

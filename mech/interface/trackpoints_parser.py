import csv
from typing import Iterator

from ..models.track import Trackpoint


def parse_trackpoints(
    arc_length_csv: str, radius_of_curvature_csv: str
) -> Iterator[Trackpoint]:
    with open(arc_length_csv, "r") as arc_lengths, open(
        radius_of_curvature_csv, "r"
    ) as radii_of_curvature:

        arc_length_reader = csv.reader(arc_lengths, delimiter=",")
        radius_of_curvature_reader = csv.reader(radii_of_curvature, delimiter=",")

        for index, (arc_length, radius_of_curvature) in enumerate(
            zip(*arc_length_reader, *radius_of_curvature_reader)
        ):
            yield Trackpoint(index, arc_length, radius_of_curvature)

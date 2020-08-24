from typing import Iterator

from yummy_cereal import AnnotationsSerializer

from ..models.snapshots import Snapshot


def serialize_snapshots(snapshots: Iterator[Snapshot], output_path: str) -> None:
    with open(output_path, "w") as stream:
        snapshot_serializer = AnnotationsSerializer(Snapshot)
        stream.write("\n".join(snapshot_serializer(snapshot) for snapshot in snapshots))

from typing import Iterator

from yummy_cereal import AnnotationsSerializer

from ..models.snapshots import Snapshot, KinemeaticSnapshot, DynamicSnapshot
from ..models.track import Trackpoint


def serialize_snapshots(snapshots: Iterator[Snapshot], output_path: str) -> None:
    with open(output_path, "w") as stream:
        snapshot_serializer = AnnotationsSerializer(
            Snapshot,
            specified_serializers={
                "trackpoint": AnnotationsSerializer(Trackpoint),
                "dynamics": AnnotationsSerializer(DynamicSnapshot),
                "kinemeatics": AnnotationsSerializer(KinemeaticSnapshot),
            },
        )
        stream.write("\n".join(snapshot_serializer(snapshot) for snapshot in snapshots))

from .interface.cli_parser import CliInput
from .interface.snapshot_serializer import serialize_snapshots
from .simulate import simulate


def entrypoint() -> None:
    cli_input = CliInput.parse_cli()
    snapshots = simulate(cli_input.car, cli_input.trackpoints)
    serialize_snapshots(snapshots, cli_input.output_path)

    for i in snapshots:
        print(i.time, i.trackpoint.arc_length)

if __name__ == "__main__":
    entrypoint()

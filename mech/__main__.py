from .interface.cli_parser import CliInput
from .interface.snapshot_serializer import serialize_snapshots
from .simulate.optimise import optimal_velocity


def entrypoint() -> None:
    cli_input = CliInput.parse_cli()
    snapshots = optimal_velocity(cli_input.car, cli_input.trackpoints)
    serialize_snapshots(snapshots, cli_input.output_path)


if __name__ == "__main__":
    entrypoint()

import argparse

parser = argparse.ArgumentParser(description="Simulate ")
parser.add_argument("-c", "--car-model", help="", required=False)
parser.add_argument("-a", "--arc-length", help="", required=True)
parser.add_argument("-r", "--radius-of-curvature", help="", required=True)

cli_arguments = vars(parser.parse_args())
car_model = cli_arguments["car_model"]
arc_length_csv = cli_arguments["arc_length"]
radius_of_curvature_csv = cli_arguments["radius_of_curvature"]

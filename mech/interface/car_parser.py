import ruamel.yaml
from yummy_cereal import AnnotationsParser

from ..models.car import Car


def parse_car(car_yaml: str) -> Car:
    car_parser = AnnotationsParser(Car)

    with open(car_yaml, "r") as stream:
        car_model = ruamel.yaml.load(stream, Loader=ruamel.yaml.Loader)
        return car_parser(car_model)

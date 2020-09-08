import ruamel.yaml
from yummy_cereal import AnnotationsParser

from ..models.car import Car, WheelSet
from ..models.engine import Engine
from ..models.brakes import Brakes


def parse_car(car_yaml: str) -> Car:
    car_parser = AnnotationsParser(
        Car,
        specified_parsers={
            "engine": AnnotationsParser(Engine),
            "brakes": AnnotationsParser(Brakes),
            "wheels": AnnotationsParser(WheelSet),
        },
    )

    with open(car_yaml, "r") as stream:
        car_model = ruamel.yaml.load(stream, Loader=ruamel.yaml.Loader)
        return car_parser(car_model)

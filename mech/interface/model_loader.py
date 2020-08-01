import ruamel.yaml
from yummy_cereal import AnnotationsParser

from ..models.car import Car


def load_car_model(car_model_yaml: str) -> Car:
    
    # TODO Debug Car's AnnotationsParser
    car_parser = AnnotationsParser(Car)

    with open(car_model_yaml, "r") as car_model:
        return car_parser(ruamel.yaml.load(car_model, Loader=ruamel.yaml.Loader))

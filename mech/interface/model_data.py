import ruamel.yaml

from models.car import Car
from models.engine import Engine
from models.brakes import Brakes
from models.wheel import Wheel


def get_car_model(car_model_yaml: str) -> Car:
    with open(car_model_yaml, "r") as car_model:
        pass

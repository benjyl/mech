from copy import copy
from typing import TypeVar
from typing_extensions import Protocol

T = TypeVar("T")


class Scalable(Protocol[T]):
    def scale(self, scale_factor: float) -> None:
        ...

    def scaled(self: T, scale_factor: float) -> T:
        ...


@dataclass
class Vector:
    normal: float
    lateral: float
    longitudinal: float

    def scale(self, scale_factor: float) -> None:
        self.normal *= scale_factor
        self.lateral *= scale_factor
        self.longitudinal *= scale_factor

    def scaled(self: T, scale_factor: float) -> T:
        clone = copy(self)
        clone.scale(scale_factor)
        return clone


@dataclass
class QuadrigeminalSet(Generic[T]):
    front_right: T
    front_left: T
    rear_right: T
    rear_left: T

    @classmethod
    def equal_load(cls: U, load: T) -> U[T]:
        return cls(load, load, load, load)

    @classmethod
    def shared_load(cls: U, load: Scalable[T]) -> U[T]:
        return cls.equal_load(reaction.scaled(0.25))

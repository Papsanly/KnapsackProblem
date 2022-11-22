from __future__ import annotations
from abc import ABC, abstractmethod


class Creature(ABC):

    def __lt__(self, other: Creature) -> bool:
        return self.value < other.value

    @property
    @abstractmethod
    def value(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def mutation_probability(self):
        raise NotImplementedError

    @abstractmethod
    def crossover(self, other: Creature) -> Creature:
        raise NotImplementedError

    @abstractmethod
    def mutate(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def make_local_improvement(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError

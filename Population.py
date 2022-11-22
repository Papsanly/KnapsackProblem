import random
from typing import Sequence
from Creature import Creature


class Population(list[Creature]):

    def __init__(self, creatures: Sequence[Creature], reverse: bool = False):
        if not creatures:
            raise ValueError('Population cannot be empty')
        self.reverse = reverse
        super().__init__(sorted(creatures, reverse=reverse))

    @property
    def best(self) -> Creature:
        return self[0]

    def kill_worst(self) -> Creature:
        return super().pop()

    def make_selection(self) -> tuple[Creature, Creature]:
        parent1 = self.best
        parent2 = random.choice([creature for creature in self if creature is not parent1])
        return parent1, parent2

    def add(self, creature: Creature) -> None:
        low = 0
        insert_index = 0
        high = len(self) - 1
        while low <= high:
            insert_index = (high + low) // 2
            if (
                self[insert_index] < creature and self.reverse or
                self[insert_index] > creature and not self.reverse
            ):
                high = insert_index - 1
            else:
                low = insert_index + 1
        if (
            self[insert_index] < creature and self.reverse or
            self[insert_index] > creature and not self.reverse
        ):
            super().insert(insert_index, creature)
        else:
            super().insert(insert_index + 1, creature)

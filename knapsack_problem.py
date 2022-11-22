from __future__ import annotations
from collections import namedtuple
from dataclasses import dataclass
from random import randint, random, choices, sample
from typing import Iterable
from Creature import Creature
from Population import Population

Item = namedtuple('Item', 'cost weight')


@dataclass
class KnapsackProblem:

    capacity: int
    cost_range: tuple[int, int]
    weight_range: tuple[int, int]

    def __init__(
            self,
            capacity: int,
            items_count: int,
            cost_range: tuple[int, int],
            weight_range: tuple[int, int]
    ):
        self.capacity = capacity
        self.items_count = items_count
        self.items = self._generate_items(cost_range, weight_range)

    def _generate_items(
            self,
            cost_range: tuple[int, int],
            weight_range: tuple[int, int]
    ) -> list[Item]:
        return [
            Item(randint(*cost_range), randint(*weight_range))
            for _ in range(self.items_count)
        ]

    def __str__(self) -> str:
        result = [
            f'Knapsack capacity: {self.capacity}',
            f'Items ({len(self.items)}):\n',
            '| Number | Cost | Weight |',
            *[
                26 * '-' + '\n' + '| {:-6} | {:-4} | {:-6} |'.format(i, item.cost, item.weight)
                for i, item in enumerate(self.items)
            ]
        ]
        return '\n'.join(result)


class KnapsackCreature(Creature):

    def __init__(self, array: Iterable[bool], problem: KnapsackProblem, mutation_probability: float):
        self.bytes = bytearray(array)
        self._problem = problem
        self._mutation_probability = mutation_probability

    @property
    def mutation_probability(self):
        return self._mutation_probability

    @property
    def value(self):
        total_cost = 0
        for i, byte in enumerate(self.bytes):
            if byte:
                total_cost += self._problem.items[i].cost
        return total_cost if self.weight <= self._problem.capacity else 0

    @property
    def weight(self) -> int:
        total_weight = 0
        for i, byte in enumerate(self.bytes):
            if byte:
                total_weight += self._problem.items[i].weight
        return total_weight

    def __str__(self) -> str:
        return ''.join(map(str, self.bytes))

    def crossover(self, other: KnapsackCreature) -> Creature:
        chromosome = [
            byte if (i // (len(self.bytes) // 4)) % 2 else other_byte
            for i, (byte, other_byte) in enumerate(zip(self.bytes, other.bytes))
        ]
        return KnapsackCreature(chromosome, self._problem, self._mutation_probability)

    def _get_item_idx(self, item: Item) -> int:
        return self._problem.items.index(item)

    def __contains__(self, item: Item) -> bool:
        item_idx = self._get_item_idx(item)
        return bool(self.bytes[item_idx])

    def _add_item(self, item: Item) -> None:
        item_idx = self._get_item_idx(item)
        self.bytes[item_idx] = 1

    def mutate(self) -> None:
        if random() < self._mutation_probability:
            randint1, randint2 = sample(tuple(range(0, len(self.bytes) - 1)), k=2)
            self.bytes[randint1], self.bytes[randint2] = self.bytes[randint2], self.bytes[randint1]

    def make_local_improvement(self) -> None:
        items_sorted = sorted(self._problem.items, key=lambda x: x.cost / x.weight, reverse=True)
        for item in items_sorted:
            if item not in self:
                self._add_item(item)
                break


def print_iteration_info(iteration: int, iteration_limit: int, best: Creature):
    if iteration == 0:
        print('\nIterating...\n')
        print('| Iteration', 'Best cost', 'Best creature |'.rjust(102), sep=' | ')

    if iteration % 20 == 0:
        print(128 * '-')
        print('|', end='')
        print('{:-10}'.format(iteration), '{:-9}'.format(best.value), best, sep=' | ', end='')
        print(' |')

    if iteration == iteration_limit - 1:
        print('\nIteration limit reached\n')


def generate_initial_population(population_count: int, problem: KnapsackProblem) -> Population:
    return Population(
        [
            KnapsackCreature(
                [
                    True if i == j else False
                    for j, _ in enumerate(problem.items)
                ],
                problem,
                mutation_probability=0.05
            )
            for i in range(population_count)
        ],
        reverse=True
    )

from Creature import Creature
from Population import Population
from knapsack_problem import print_iteration_info


class GeneticAlgorithm:

    def __init__(
            self,
            initial_population: Population,
            iteration_limit: int = 1000,
            print_info: bool = True
    ):
        self.population = initial_population
        self.iteration_limit = iteration_limit
        self._print_info = print_info

    def solve(self) -> Creature:
        for i in range(self.iteration_limit):
            parent1, parent2 = self.population.make_selection()

            new_creature = parent1.crossover(parent2)
            new_creature.mutate()
            new_creature.make_local_improvement()

            self.population.add(new_creature)
            self.population.kill_worst()

            if self._print_info:
                print_iteration_info(i, self.iteration_limit, self.population.best)

        return self.population.best

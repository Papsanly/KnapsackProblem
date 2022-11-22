from knapsack_problem import KnapsackProblem, generate_initial_population
from GeneticAlgorithm import GeneticAlgorithm
from utils import get_optimal_solution


def main():
    problem = KnapsackProblem(
        capacity=250,
        items_count=100,
        cost_range=(2, 30),
        weight_range=(1, 25)
    )
    print(problem)
    population = generate_initial_population(100, problem)
    solution = GeneticAlgorithm(population).solve()
    print(f'Best solution: {solution}')
    print(f'Cost: {solution.value}')
    print(f'Optimal cost: {get_optimal_solution(problem)}')


if __name__ == '__main__':
    main()

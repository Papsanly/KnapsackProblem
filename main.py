from knapsack_problem import KnapsackProblem, generate_initial_population
from GeneticAlgorithm import GeneticAlgorithm
from utils import get_optimal_solution, graph_evolution


def main():
    problem = KnapsackProblem(
        capacity=250,
        items_count=100,
        cost_range=(2, 30),
        weight_range=(1, 25)
    )
    print(problem)
    population = generate_initial_population(100, problem)
    algorithm = GeneticAlgorithm(population)

    solution = algorithm.solve()
    print(f'Execution time: {algorithm.execution_time}s')
    print(f'Best solution: {solution}')
    print(f'Cost: {solution.value}')

    optimal = get_optimal_solution(problem)
    print(f'Optimal cost: {optimal}')
    graph_evolution(algorithm, optimal)


if __name__ == '__main__':
    main()

import sys

from data_reading import data_reading
from genetic import pc_max_genetic_algorithm
from greedy import pc_max_greedy_algorithm


def main():
    if len(sys.argv) < 3:
        raise RuntimeError("Not enough arguments")
    (number_of_processors, tasks) = data_reading(sys.argv[2])

    result = 0
    if sys.argv[1] == "genetic":
        size_of_population = 50
        num_of_generations = 20000
        chance_for_mutation = 0.004
        chance_for_crossover = 0.65
        num_of_elites = 4
        max_running_time = 300
        percent_of_greedy = 0.5
        result = pc_max_genetic_algorithm(number_of_processors, tasks, len(tasks), size_of_population,
                                          num_of_generations, chance_for_mutation, chance_for_crossover, num_of_elites,
                                          percent_of_greedy, max_running_time)
    elif sys.argv[1] == "greedy":
        result = pc_max_greedy_algorithm(number_of_processors, tasks)
    print(result)


if __name__ == '__main__':
    main()
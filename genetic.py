import random
import time


def greedy_algorithm(number_of_processors, tasks, num_of_tasks, instance):
    schedule = [0 for _ in range(number_of_processors)]
    chromosome = [0 for _ in range(num_of_tasks)]

    for i in range(num_of_tasks):
        free_processor = min(enumerate(schedule), key=lambda t: t[1])[0]
        schedule[free_processor] += tasks[instance[i]]
        chromosome[instance[i]] = free_processor + 1

    return chromosome


def generate_initial_population(number_of_processors, tasks, size, num_of_tasks, percent_of_greedy):
    population = []
    instance = [x for x in range(num_of_tasks)]
    num_of_greedy = int(percent_of_greedy * size)
    for _ in range(num_of_greedy):
        random.shuffle(instance)
        population.append(greedy_algorithm(number_of_processors, tasks, num_of_tasks, instance))
    for i in range(size - num_of_greedy):
        current = [random.randint(1, number_of_processors) for _ in range(num_of_tasks)]
        population.append(current)
    return population


def crossover(first_parent, second_parent, number_of_tasks, chance_for_crossover):
    if random.random() >= chance_for_crossover:
        return first_parent, second_parent
    to_cross = number_of_tasks // 2
    first_child = first_parent[:to_cross] + second_parent[to_cross:]
    second_child = second_parent[:to_cross] + first_parent[to_cross:]
    return [first_child, second_child]


def get_fitness(number_of_processors, tasks, chromosome):
    result = [0 for _ in range(number_of_processors)]
    for i in range(len(chromosome)):
        result[chromosome[i] - 1] += tasks[i]
    return max(result)


def select_parents(population, fitness, size_of_population):
    new_fitness = list(map(lambda x: 1000000 / x, fitness))
    if any(map(lambda x: x < 1, new_fitness)):  # TODO usunac, gdy znajdziemy dobry wspolczynnik
        print("increase coefficient for fitness")
    new_fitness = list(map(lambda x: int(x), new_fitness))
    wheel = sum(new_fitness)
    first_point_wheel = random.randint(1, wheel // 2)
    second_point_wheel = first_point_wheel + wheel // 2
    sum_of_fitness = 0
    first_parent = None
    stop = 0
    for i in range(size_of_population):
        if sum_of_fitness >= first_point_wheel:
            first_parent = population[i - 1]
            stop = i
            break
        sum_of_fitness += new_fitness[i]
    for i in range(stop, size_of_population):
        if sum_of_fitness >= second_point_wheel:
            return first_parent, (population[i - 1])
        sum_of_fitness += new_fitness[i]
    return first_parent, (population[-1])


def mutate(chromosome, number_of_processors, number_of_tasks, chance_of_mutation):
    if random.random() >= chance_of_mutation:
        return chromosome
    chromosome[random.randint(0, number_of_tasks - 1)] = random.randint(1, number_of_processors)
    return chromosome


def find_best_chromosomes(fitness, num_of_elites):
    best = [i[0] for i in sorted(enumerate(fitness), key=lambda x: x[1])][:num_of_elites]
    return best


def pc_max_genetic_algorithm(number_of_processors, tasks, number_of_tasks, size_of_population, num_of_generations,
                             chance_for_mutation, chance_for_crossover, num_of_elites, percent_of_greedy,
                             max_running_time):
    population = generate_initial_population(number_of_processors, tasks, size_of_population, number_of_tasks,
                                             percent_of_greedy)
    (best_subject, min_time) = population[0], get_fitness(number_of_processors, tasks, population[0])
    start_time = time.time()
    generation_counter = 0
    while time.time() - start_time < max_running_time and generation_counter < num_of_generations:
        generation_counter += 1
        fitness = [get_fitness(number_of_processors, tasks, population[i]) for i in range(size_of_population)]
        for i in range(size_of_population):
            if fitness[i] < min_time:
                print(min_time)
                best_subject, min_time = population[i], fitness[i]
        parents = [select_parents(population, fitness, size_of_population) for _ in
                   range(size_of_population // 2)]
        elitism = find_best_chromosomes(fitness, num_of_elites)
        children = [population[x] for x in elitism]
        for i in range(size_of_population // 2):
            child_1, child_2 = crossover(parents[i][0], parents[i][1], number_of_tasks, chance_for_crossover)
            mutate(child_1, number_of_processors, number_of_tasks, chance_for_mutation)
            mutate(child_2, number_of_processors, number_of_tasks, chance_for_mutation)
            children.append(child_1)
            children.append(child_2)
        population = children
    print(time.time() - start_time)
    print(generation_counter)
    return best_subject, min_time


def main():
    number_of_processors = int(input("Number of processors: "))
    tasks = [int(x) for x in input("Tasks: ").strip().split(" ")]
    print(pc_max_genetic_algorithm(number_of_processors, tasks, len(tasks), 50, 100, 0.001, 0.65, 2, 0.5, 1))


if __name__ == '__main__':
    main()

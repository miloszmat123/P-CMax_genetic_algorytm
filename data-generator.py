import random
import sys


def interactive_generator():
    filename = input("Enter output filename: ")
    processors = int(input("Enter the number of processors: "))
    n_tasks = 0
    while n_tasks <= processors:
        n_tasks = int(input("Enter the number of tasks: "))
        if n_tasks <= processors:
            print("Number of tasks have to be higher than number of processors")
    min_time = int(input("Enter min time of one task: "))
    max_time = 0
    while max_time < min_time:
        max_time = int(input("Enter the max time of one task: "))
        if max_time < min_time:
            print("Max time have to be higher than min time")
    generate(filename, processors, n_tasks, min_time, max_time)


def generate(filename, processors, n_tasks, min_time, max_time):
    file = open(filename, "w")
    print(processors, file=file)
    print(n_tasks, file=file)
    for i in range(n_tasks):
        print(random.randint(min_time, max_time), file=file)
    file.close()


def optimum_generate(filename, processors, n_tasks, max_ovr_time):
    file = open(filename, "w")
    print(processors, file=file)
    print(n_tasks * processors, file=file)
    tasks = []

    for i in range(processors):
        tasks_on_processor = [random.randint(1, max_ovr_time - 1)]
        while len(tasks_on_processor) != n_tasks - 1:
            task = random.randint(1, max_ovr_time - 1)
            if task not in tasks_on_processor:
                tasks_on_processor.append(task)
        tasks_on_processor.sort()
        tasks.append(tasks_on_processor[0])
        for j in range(1, n_tasks - 1):
            temp = tasks_on_processor[j] - tasks_on_processor[j - 1]
            tasks.append(temp)
        tasks.append(max_ovr_time - tasks_on_processor[-1])
    for i in range(n_tasks * processors):
        print(tasks[i], file=file)
    file.close()


"""
Usage: 
python data-generator.py
python data-generator.py [filename] [num_of_processors] [num_of_tasks_per_processor] [overall_time]
python data-generator.py [filename] [num_of_processors] [num_of_tasks] [min_task_time] [max_task_time]
"""


def main():
    if len(sys.argv) == 5:
        optimum_generate(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
        return
    if len(sys.argv) == 6:
        generate(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
        return
    interactive_generator()


if __name__ == '__main__':
    main()
